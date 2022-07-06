Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_fabric_handler
==================
This task facilitates the configurations fabrics and its attributes through REST calls. The sfs-fabric-handler uses the REST API to configure a Dell EMC SmartFabric Services. It supports both the fabric create and delete operations.

Installation
------------
The collections tarball built can be installed locally using the following commands:
ansible-galaxy collection build

Once the collections tarball get published locally, install your collection from the tarball using the command
ansible-galaxy collection install dellemc-sfs-1.0.0.tar.gz

Version compatibility
---------------------
Ansible version 2.10 or later.
Enterprise sfs Distribution by Dell Technologies version 3.0 or later.
Note: Community sfs  versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated with community versions, nor is it supported.

module variables
----------------
Variables and values are case-sensitive

sfs_fabric_handler keys
-----------------------
Key                   | Type    |       Description                         |   Support        |
----------------------|---------|-------------------------------------------|------------------|
fabric_design           |string | Configures the fabric design       |   Dell Solutions |
fabric_design_mappings        | string | Configures the fabric_design_mappings     |   Dell Solutions |
name | string  | Configures name   |   Dell Solutions |
description    | string | Configures description   |   Dell Solutions |
nodes  | string  | Configures nodes    |   Dell Solutions |

Connection variables
--------------------
Ansible Dell EMC SmartFabric Services require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible directories, or inventory or in the playbook itself.

Key		    |	Required   |            	Choices	Description								    |
--------------------|--------------|--------------------------------------------------------------------------------------------------------|
ansible_host	    |	yes	   |	Specifies the hostname or IP address to connect to the remote device over the specified transport  |
ansible_user	    |	yes	   |	Specifies the username that authenticates the connection to the remote device			    |	
ansible_password    |	yes	   |	Specifies the password that authenticates the connection to the remote device			    |
ansible_network_os  |   yes        |    Specifies the network type for the connection to the remote device                                  |
ansible_connection  |   yes        |    Specifies the connection plugin                                                                     |

Sample use case
---------------

**Inventory**

        [os10]
        node1 ansible_host=100.104.97.81

        [os10:vars]
        ansible_ssh_user=admin
        ansible_ssh_pass=admin
        ansible_network_os=dellemc.sfs.sfs
        ansible_connection=ansible.netcommon.httpapi
        ansible_httpapi_use_ssl=yes
        ansible_httpapi_validate_certs=no
        ansible_command_timeout=30
        ansible_python_interpreter=/usr/bin/python3

**Playbook.yaml**

      - hosts: all
        gather_facts: false
        collections:
          - dellemc.sfs
        tasks:
          - name: Provision Configs
            block:
              - name: Fabric Handler
                dellemc.sfs.sfs_fabric_handler:
                  fabric_design: "2xMX9116n_Fabric_Switching_Engines_in_same_chassis"
                  fabric_design_mappings: [{ "DesignNode": "Switch-A","PhysicalNode": "HMXBPK2"},{"DesignNode": "Switch-B","PhysicalNode": "97JBJ23"}]
                  name:  "Some New Fabric"
                  description: "This is a new Fabric"
                  nodes: [{ "NodeId": "HMXBPK2"},{ "NodeId": "97JBJ23"}]
                  fabric_id: "f926a2fa-124e-4558-ba11-49127426010c"
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result

             	
**Run**

ansible-playbook -i inventory Playbook.yaml

