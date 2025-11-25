# Security Twin Documentation

## Table of Contents

- [Overview](#overview)
- [Basic usage: build and analyze attack position graph](#basic-usage)
- [Advanced usage: deployment of the security twin using libvirt VMs and provisioning with Ansible](#advanced-usage-deployment-of-the-security-twin-using-libvirt-vms-and-provisioning-with-ansible)
- [Prerequisites](#prerequisites)
- [Attack agent](#attack-agent)
- [Extra](#Extra)


---

## Overview

Security Twin is a comprehensive security analysis and deployment pipeline that:
1. Populates a data model with information system data
2. Generates attack position graphs for security analysis
3. Deploys virtual machines (VMs) using libvirt and provisions VMs with Windows/Linux configurations using Ansible

Follow basic usage or advanced usage


## Basic usage

You can either collect the data yourself or skip directly to populating the data model.

- If you want to **collect data**, see [Step 1](#1--data-collection-on-the-is_lab).
- If you prefer to **skip data collection**, go to [Step 2](#2--populate-the-data-model).

### 0- install prerequisites and setup the database.

See [Prerequisites](#prerequisites)

### 1- Data collection on the IS_LAB

Collecting data from the Active Directory domain:

```bash
python3 collector.py --output-directory collect --domain lab.local -dc-ip <TODO_UPDATE> -u "Administrateur@lab.local" -p "234P@ss"
```
the command uses our data collector to query ISLAB, an example information system made of 8 VMs configured as described in the paper.


Collecting data from a Linux server:

```bash
python3 collector.py --output-directory collect --hostname <TODO_UPDATE> -u root --key-path <TODO_UPDATE_RSA>
```

To see more details see [Readme](collector_agent/README.md).
### 2- Populate the data model

To populate the database with the collected data, run the following command:

```bash
python3 -m connector --directory sample_lab
```

If the operation is successful, you should see an output similar to:

```text
reseting db model in  ['information_schema', 'model', 'mysql', 'performance_schema', 'sys', 'test']
Success !
```

### 3- Build the attack position graph

Once the database is populated, you can generate an attack position graph by running:

```bash
python3 -m attack_graph b --graph-path MyGraph
```

The output will display general statistics about the generated graph:

```text
Graph 'MyGraph' has 401 nodes and 15384 edges
Edge labels count:
  CVE_2020_1472_zerologon: 9700
  CVE_2021_44228_log4j: 2328
  RDP: 36
  wmic: 90
  PSRemote: 114
  CVE_2023_38831_winrar: 3080
  ServiceExeModify: 36
```


### 4- Analyze paths in the attack position graph


Search attack path in the graph starting from `h0 u0` (attack position with user `u0` on host `h0`)

```bash
python -m attack_graph l --graph-path myGraph human c0 u0
```
Output all path found. 
```text
...
[360] path length 5, dst: (h0,NT Authority@h0)
        (dc0,u04@lab.local) CVE_2020_1472_zerologon
        (dc0,Administrateur@lab.local) wmic
        (h0,Administrateur@lab.local) ServiceExeModify
        (h0,Local System@h0) ServiceExeModify
        (h0,NT Authority@h0) 

[361] path length 5, dst: (h0,NT Authority@h0)
        (dc0,u04@lab.local) CVE_2020_1472_zerologon
        (dc0,Administrateur@lab.local) PSRemote
        (h0,Administrateur@lab.local) ServiceExeModify
        (h0,Local System@h0) ServiceExeModify
        (h0,NT Authority@h0) 

[362] path length 5, dst: (h5,NT Authority@h5)
        (dc0,u04@lab.local) CVE_2020_1472_zerologon
        (dc0,Administrateur@lab.local) wmic
        (h5,Administrateur@lab.local) ServiceExeModify
        (h5,Local System@h5) ServiceExeModify
        (h5,NT Authority@h5) 

[363] path length 5, dst: (h5,NT Authority@h5)
        (dc0,u04@lab.local) CVE_2020_1472_zerologon
        (dc0,Administrateur@lab.local) wmic
        (h5,Administrateur@lab.local) ServiceExeModify
        (h5,Local System@h5) ServiceExeModify
        (h5,NT Authority@h5) 

[364] path length 5, dst: (h5,NT Authority@h5)
        (dc0,u04@lab.local) CVE_2020_1472_zerologon
        (dc0,Administrateur@lab.local) PSRemote
        (h5,Administrateur@lab.local) ServiceExeModify
        (h5,Local System@h5) ServiceExeModify
        (h5,NT Authority@h5) 

all 365 path(s) displayed
```

Prompt user to choose which path to analyse. 

```text
choose which path to reproduce (0 - 364): 363
```

Display security characteristics related to this path.
```text
- dc0 is a DC in AD domain lab.local with version Windows Server 2019 Datacenter Evaluation  10.0 (17763), CVE zerologon
- User Administrateur@lab.local in AD domain lab.local
- machine h5 localgroup Performance Log Users member: Administrateur@lab.local
- machine h5: rootcimv2rights ('Administrateur@lab.local', 'Enable,MethodExecute,FullWrite,PartialWrite,ProviderWrite,RemoteAccess,ReadSecurity,WriteSecurity')
- machine h5: service MicrosoftEdgeElevationService-1 executed by Local System@h5 executes file at C:\Program Files (x86)\Microsoft\Edge\Application\142.0.3595.90\elevation_service.exe
- machine h5: Administrateur@lab.local has rights FullControl on file at C:\Program Files (x86)\Microsoft\Edge\Application\142.0.3595.90\elevation_service.exe
- machine h5: service WdNisSvc-1 executed by NT Authority@h5 executes file at C:\ProgramData\Microsoft\Windows Defender\platform\4.18.25100.9008-0\NisSrv.exe
- machine h5: Local System@h5 has rights FullControl on file at C:\ProgramData\Microsoft\Windows Defender\platform\4.18.25100.9008-0\NisSrv.exe
- u04 and dc0 in same ad domain
- machine dc0, GPO SeDenyInteractiveLogonRight is undefined
- machine dc0, GPO SeInteractiveLogonRight is undefined
- Administrateur and dc0 in same ad domain
- machine dc0, GPO SeDenyInteractiveLogonRight is undefined
- machine dc0, GPO SeInteractiveLogonRight is undefined
- machine h5, GPO SeDenyInteractiveLogonRight is undefined
- Administrateur and h5 in same ad domain
- machine h5, GPO SeInteractiveLogonRight is undefined
- Local System local user of h5
- machine h5, GPO SeDenyInteractiveLogonRight is undefined
- machine h5, GPO SeInteractiveLogonRight is undefined
- NT Authority local user of h5
- machine h5, GPO SeDenyInteractiveLogonRight is undefined
- machine h5, GPO SeInteractiveLogonRight is undefined
```

You can also search all path between 2 vertices
```bash
python -m attack_graph l --graph-path MyGraph human h0 u0 h2 "Local System"
```

### 5 Visualize graph in GUI using Gephi

- **Option A** In bellow commands, argument `--graph-path` takes `data/graph/ISLAB` 
- **Option B** In bellow commands, argument `--graph-path` takes the same value as the one used in step 3 (`data/graph/myGraph` in the example) 

```bash
python -m attack_graph l --graph-path MyGraph gui
```

Output `gephi graph saved in myGraph.gexf`, then open the generated file with gephi

----

## Advanced usage: deployment of the security twin using libvirt VMs and provisioning with Ansible

The main pipeline script (`pipeline.sh`) automates the entire workflow:

```bash
./pipeline.sh
```

The pipeline executes the following steps:

### Step 1: Fill data model
Resets and populates the database with infrastructure data from raw data file.

### Step 2: Generate Attack Graph
Builds an attack graph based on the database contents and performs analysis.

The attack path from `(c0,u0)` to `(c2,SYSTEM)` is selected and only 4 VMs are deployed at step 3


### Step 3: Deploy and provision VMs

Deploys virtual machines using libvirt and executes provisioning playbooks

### How to use the pipeline.sh script?

- Modify the first line with the path to your python virtual environment (`venv_path="$(pwd)/venv_secwin"`)
- Deployed VMs will be in the network range `192.168.X.0/24` where `X` is the value of `SUBNET` in [./pydeploy/.env](./pydeploy/.env)
- When used as is (path from `(c0,u0)` to `(c2,SYSTEM)`), 4 VMs are deployed, using 160Go of disk space

### Clean up: delete libvirt VM, pool, network

Use [./pydeploy/delete_vm.sh](./pydeploy/delete_vm.sh) and give it the suffix used in [./pydeploy/.env](./pydeploy/.env) (currently `76`)


### Additionnal system Requirements for security twin deployment and provisionning

- libvirt and QEMU/KVM for VM deployment
- Ansible for VM provisioning
- mkisofs (genisoimage package) for CloudInit ISO creation



## Prerequisites

### System Requirements for attack position graph generation and analysis
- Python 3.8+
- MySQL/MariaDB database server
- Docker
- Node JS
- Terraform and CDKTF CLI (https://developer.hashicorp.com/terraform/tutorials/cdktf/cdktf-install)
- xsltproc (for XML processing)

### Python Dependencies

Install all required packages (inside a virtual environment):
```bash
pip install -r requirements.txt
```

Key dependencies include:
- `networkx` - Graph analysis
- `SQLAlchemy` - Database ORM
- `pymysql` - MySQL driver
- `cdktf` - Infrastructure as Code
- `ansible` - VM provisioning
- `PyYAML` - YAML processing
- And more (see `requirements.txt`)

### Database Setup

Start MySQL database server:
```bash
# Remove existing container, docker network, process with the same name
docker container rm -f model-db-1 >/dev/null 2>&1 || true
docker network rm model_app_net >/dev/null 2>&1 || true
sudo pkill mysql >/dev/null 2>&1 || true
# Start database container
docker compose -f model/compose.yaml up -d db
```

Wait until the container (`model-db-1`) status shows `(healthy)`:
```bash
docker container ls | grep model-db-1
```

Note: If you encounter IP address conflicts, modify `model/compose.yaml` to use a different subnet (e.g., `172.99.0.0/16` instead of `172.20.0.0/16`).


## Attack agent

Due to security and ethical considerations, the threat emulation platform we used to run the attacks against the deployed security twin will not be made available publicly. 
However, this tool will be available upon request for research purposes to verified academic institutions and security professionals who demonstrate a legitimate need for its use.

Indeed, we do not want to support the sharing of exploitation tools that could be misused and cause harm.
Since this agent is not a contribution to the security twin project and could easily be replaced by any other similar tool, we decided to keep it on-request only.


# Extra

## Command-Line Tools

#### 1. Database Management (`model.fill_db`)

**Usage**
```bash
python -m model.fill_db {s,reset} [options]
```

**Subcommands**

**Reset database (`reset`)**
```bash
python -m model.fill_db reset [information_system]
```
- **Description:** Reset and optionally fill the database
- **Arguments:**
  - `information_system` (optional): Path to the information system description file (e.g., `data/lab_surprise.py`)
  - If omitted, the database will be reset without any data

**Examples**
```bash
# Reset and fill database
python -m model.fill_db reset data/lab_surprise.py
```

#### 2. Attack Graph (`attack_graph`)

**Usage**
```bash
python -m attack_graph MODE [ANALYSIS] [SRC_DST_NODES]
```

**Arguments**

**Positional Arguments:**
- `mode` (required): 
  - `b` - Build graph from database
  - `l` - Load existing graph from file

- `analysis` (optional):
  - `human` - Interactive human-readable analysis
  - `gui` - Visual graph in browser/Gephi

- `src_dst_nodes` (optional, requires analysis):
  - Format: `srcM srcU [dstM dstU]`
  - Source machine and user (required)
  - Destination machine and user (optional)

**Examples**
```bash
# Build graph
python -m attack_graph b

# Build and analyze path from c0/u0 to c2/SYSTEM
python -m attack_graph b human c0 u0 c2 SYSTEM --hosts-file tmp_hosts.txt

# Load existing graph and show in GUI
python -m attack_graph l gui
```

#### 3. VM Deployment (`digitaltwin`)

**Usage**
```bash
python -m digitaltwin ACTION -i INPUT -d DIRECTORY
```

**Arguments**

**Positional Arguments:**
- `action` (required):
  - `create` - Deploy VMs
  - `destroy` - Remove VMs

**Options:**
- `-i, --input PATH` (required): Path to JSON or hosts input file
- `-d, --directory PATH` (required): Directory where Terraform state will be stored

**Examples**
```bash
# Deploy VMs from hosts file
python -m digitaltwin create -i tmp_hosts.txt -d todell

# Destroy deployed VMs
python -m digitaltwin destroy -i tmp_hosts.txt -d todell
```

**Configuration**

The deployment uses environment variables from `pydeploy/.env`:
- `POOL_PATH` - Storage pool path (relative paths resolved from pydeploy directory)
- `IMAGES_LOCATION` - Path to OS images (relative paths resolved from pydeploy directory)
- `VIRTIO_LOCATION` - Path to virtio drivers
- `SUBNET` - Network subnet number (default: 100)
- `NETWORK_NAME` - Network name (default: intnet0)
- `PREFIX_VM_NAME` - Prefix for VM names
- `INFRA_ID` - Infrastructure identifier
- `SSH_USERNAME` - SSH username for remote libvirt (optional)
- `SSH_KEY` - SSH key path for remote libvirt (optional)
- `VIRT_PARAM` - Additional libvirt URI parameters (optional)

#### 4. Prepare Deployment (`provisioning/prepare_deploy.py`)

**Usage**
```bash
python provisioning/prepare_deploy.py [OPTIONS]
```

**Arguments**

**Mutually Exclusive Groups (one required):**

**Option 1: Generate hosts file**
- `--allhosts-file PATH`: Generate hosts file for all computers in database
  - When used, no other arguments allowed

**Option 2: Generate inventory**
- `--out-inventory PATH` (required): Path to output inventory file
- `--in-modeljson PATH` (required): Path to input model JSON file
- `--in-env PATH` (optional): Path to .env file (default: `.env`)
- `--in-ipmatch PATH` (optional): Path to IP match text file

**Examples**
```bash
# Generate hosts file for all computers
python provisioning/prepare_deploy.py --allhosts-file tmp_hosts.txt

# Generate inventory from model JSON
python provisioning/prepare_deploy.py \
  --out-inventory tmp_inventory.ini \
  --in-modeljson tmp_hosts.txt.json \
  --in-env pydeploy/.env
```

#### 5. Provisioning (`provisioning`)

**Usage**
```bash
python -m provisioning ACTION [OPTIONS]
```

**Arguments**

**Positional Arguments:**
- `action` (required):
  - `exec` - Execute all playbooks
  - `show` - Show all playbooks that will be executed

**Options:**
- `-i, --inventory PATH`: Path to inventory file (default: `provisioning/inventory.ini`)
- `-range`: Specify a range of commands to execute (interactive)
- `--batch-createAD`: Use 15-minute sleep instead of user prompt when creating AD

**Examples**
```bash
# Show all playbooks
python -m provisioning show -i tmp_inventory.ini

# Execute all playbooks
python -m provisioning exec -i tmp_inventory.ini --batch-createAD

# Execute with range selection
python -m provisioning exec -i tmp_inventory.ini -range
```

### Configuration Files

#### Database Configuration (`model/db_connect.py`)

Database connection settings are configured in `model/db_connect.py`:
- Host, port, username, password
- Database name

#### Environment Variables

**For pydeploy** (`pydeploy/.env`):
- `POOL_PATH` - Storage pool path (can be relative to pydeploy directory)
- `IMAGES_LOCATION` - OS images location (can be relative)
- `VIRTIO_LOCATION` - Virtio drivers location
- `SUBNET` - Network subnet (e.g., "100" for 192.168.100.0/24)
- `NETWORK_NAME` - Libvirt network name
- `PREFIX_VM_NAME` - VM name prefix
- `INFRA_ID` - Infrastructure identifier

**For provisioning**:
- Ansible inventory file contains VM IPs, usernames, and passwords

### Host Factory Configuration

The `host_factory.py` supports the following OS configurations:

**Windows:**
- `windows,windows10,21H2`
- `windows,windows10,22H2`
- `windows,server19,17763.737`
- `windows,server22,20348.3207`

**Linux:**
- `linux,debian,20250811-2201` (Debian 13)
- `linux,debian,20250210-2019` (Debian 12)

#### Network Configuration

**Windows hosts:**
- Interface: `Ethernet Instance 0`
- DHCP: `False`
- IP: `192.168.{SUBNET}.254/24`
- Gateway: `192.168.1.254`

**Linux hosts:**
- Interface: `ens3`
- DHCP: `True`
- IP: `192.168.{SUBNET}.{100+host_count}/24`
- Gateway: `192.168.{SUBNET}.254`

### VM Management

#### Delete VMs

Use the `delete_vm.sh` script to clean up VMs, pools, and networks:

```bash
./pydeploy/delete_vm.sh <suffix>
```

**Example:**
```bash
./pydeploy/delete_vm.sh 77
```

This will:
1. Destroy and undefine all VMs matching `manu_00<suffix>`
2. Remove storage pools matching `00<suffix>`
3. Remove networks matching `00<suffix>`



### Troubleshooting

#### Database Connection Errors

**Error:** `Lost connection to MySQL server during query`

**Solution:** This is often due to IP address conflicts. Modify `model/compose.yaml` to use a different subnet (e.g., `172.99.0.0/16`).




### Workflow Example

Complete workflow from start to finish:

```bash
# 1. Start database
docker compose -f model/compose.yaml up -d db

# 2. Run pipeline
./pipeline.sh

# The pipeline will:
# - Fill database with lab_surprise.py data
# - Generate attack graph
# - Wait for user to deploy VMs
# - Wait for user to provision VMs

# 3. Clean up (when done)
./pydeploy/delete_vm.sh 76
```