#!/bin/bash


venv_path="$(pwd)/venv_secwin"

root_path="$(pwd)"
pydeploy_path="$(pwd)/pydeploy"


for var in pydeploy_path venv_path; do
    dir="${!var}"
    echo "$var: $dir"
    if [ ! -d "$dir" ]; then
        echo "$var ($dir) is NOT a directory"
        exit 1
    fi
done

export PYTHONPATH="$root_path:$PYTHONPATH"
hosts_file="tmp_hosts.txt"
inventory_file="provisioning/tmp_inventory.ini"
tmp_out=/tmp/pipeline_out.txt

# Activate venv once at the beginning
source "$venv_path/bin/activate"

# 1 fill db
python3 -m connector --directory data/sample_lab
# 2 generate attack graph
python -m attack_graph --hosts-file "$hosts_file" b human h0 u0 h3 ugSci -lp

# 3 deploy VMs
read -p "Press Enter to deploy VMs..."
cd "$pydeploy_path"
python -m digitaltwin -i "$root_path/$hosts_file"  -d todell create

# 4 provision VMs
echo "Starting provisioning of VMs..."
cd "$root_path"
# generate inventory file
python provisioning/prepare_deploy.py --out-inventory "$inventory_file" --in-modeljson "$root_path/$hosts_file.json" --in-env "$pydeploy_path/.env"
# provision VMs
python -m provisioning exec -i "$inventory_file" --batch-createAD
