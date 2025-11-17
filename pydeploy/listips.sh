#!/usr/bin/env bash
#set -euo pipefail


if [[ -z "${1:-}" ]]; then
    echo "Error: Missing required argument. Usage: $0 <subnet>"
    echo "Example: $0 166 will list ips containing '166'"
    exit 1
fi

for vm in $(virsh list --state-running --name); do
    # Get IPs using virsh domifaddr
    e=$(virsh domifaddr "$vm")
    # echo "$vm $e"
    # echo e only lines matching 192.168.<argument>[0-9]*
    if [[ "$1" == "all" ]]; then
        ips=$(echo "$e" | awk '/192\.168\./ {print $4}' | cut -d "/" -f1)
    else
        ips=$(echo "$e" | grep "192\.168\.$1" | awk '{print $4}' | cut -d "/" -f1)
    fi
    if [[ -n "$ips" ]]; then
        echo -n "$vm "
        echo "$ips"
    fi
done
