#!/usr/bin/env bash
#set -euo pipefail


if [[ -z "${1:-}" ]]; then
    echo "Error: Missing required argument. Usage: $0 <vm_suffix>"
    exit 1
fi

IFS=$'\n'
for vm in $(virsh list --all --name | grep -E "^manu_00$1"); do
    echo -n "Processing VM: $vm "
    sleep 5
    echo "go"
    virsh destroy "$vm" 2>/dev/null || true
    virsh undefine "$vm" --remove-all-storage || true
    virsh managedsave-remove "$vm" 2>/dev/null || true

    disk_paths=$(virsh dumpxml "$vm" | grep "source file" | sed -E 's/.*file=['"'"'"]([^"'"'"']+)["'"'"'].*/\1/')

    virsh undefine "$vm" || true

    for disk in $disk_paths; do
        if [[ -f "$disk" ]]; then
            echo "Deleting disk: $disk"
            rm -f "$disk"
        else
            echo "Disk not found: $disk"
        fi
    done

    echo ""
done

echo "Cleaning up storage pools containing 00$1 in the name..."
failed_pools=()
for pool in $(virsh pool-list --all --name | grep "00$1"); do
    echo "Destroying and deleting pool: $pool"
    # Disable autostart first
    virsh pool-autostart "$pool" --disable 2>/dev/null || true
    # Destroy the pool (stop it) with retry logic
    pool_destroyed=false
    pool_failed=false
    for attempt in {1..3}; do
        if virsh pool-destroy "$pool" 2>&1; then
            echo "Pool $pool destroyed successfully"
            pool_destroyed=true
            break
        else
            if [ $attempt -lt 3 ]; then
                echo "Warning: Failed to destroy pool $pool (attempt $attempt/3), retrying in 5 seconds..."
                sleep 5
            else
                echo "Warning: Failed to destroy pool $pool after 3 attempts (may already be inactive)"
                pool_failed=true
            fi
        fi
    done
    # Undefine the pool (remove it)
    if virsh pool-undefine "$pool" 2>&1; then
        echo "Pool $pool undefined successfully"
    else
        echo "Error: Failed to undefine pool $pool"
        pool_failed=true
    fi
    # Add to failed_pools if either destroy or undefine failed
    if [ "$pool_failed" = true ]; then
        failed_pools+=("$pool")
    fi
done

echo "Cleaning up libvirt networks containing 00$1 in the name..."
for net in $(virsh net-list --all --name | grep "00$1"); do
    echo "Destroying and deleting network: $net"
    virsh net-destroy "$net" 2>/dev/null || true
    virsh net-undefine "$net" 2>/dev/null || true
done

# Check if any pools that failed to destroy still exist
if [ ${#failed_pools[@]} -gt 0 ]; then
    echo ""
    echo -e "\033[33mChecking if failed pools still exist...\033[0m"
    still_existing_pools=()
    for pool in "${failed_pools[@]}"; do
        if virsh pool-list --all --name | grep -q "^${pool}$"; then
            still_existing_pools+=("$pool")
        fi
    done
    
    if [ ${#still_existing_pools[@]} -gt 0 ]; then
        echo -e "\033[33mThe following pools still exist and need manual cleanup:\033[0m"
        for pool in "${still_existing_pools[@]}"; do
            echo -e "\033[33m  Pool: $pool\033[0m"
            echo -e "\033[33m  Execute these commands manually:\033[0m"
            echo -e "\033[33m    virsh pool-destroy $pool && virsh pool-undefine $pool\033[0m"
            echo ""
        done
    fi
fi

echo -e "\033[33mRemember to 'rm -rf <pool_path>'\033[0m"
