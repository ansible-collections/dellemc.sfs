Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_fabric_replace
==================
This task facilitates the configurations replace the switch because the Service Tag provided for the old to new switch and its attributes through REST calls. The sfs-fabric-replace uses the REST API to configure a Dell EMC SmartFabric Services. 

PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
1) The Service Tag entered for the old and new switch is valid. 
2) The old switch has physically been removed. 
3) The new switch is online in full-switch mode and at the same version of OS10 as the other switch in the SmartFabric. 
4) The new switch was not part of another SmartFabric in the same Multi-Chassis Management group as the old switch.

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
Note: Community sfs versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated with community versions, nor is it supported.

module variables
----------------
Variables and values are case-sensitive

sfs_fabric_replace keys
--------------------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
old_service_tag |	string	| Configures fabric replace on valid old_service tag   |	Dell Solutions |
new_service_tag  |	string	| Configures new_service_tag     |	Dell Solutions |

Connection variables
--------------------
Ansible Dell EMC SmartFabric Services require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible directories, or inventory or in the playbook itself.

Key		    |	Required   |            	Choices	Description								    |
--------------------|--------------|--------------------------------------------------------------------------------------------------------|
ansible_host	    |	yes	   |	Specifies the hostname or IP address to connect to the remote device over the specified transport  |
ansible_user	    |	yes	   |	Specifies the username that authenticates the connection to the remote device			    |	
ansible_password    |	yes	   |	Specifies the password that authenticates the connection to the remote device			    |
ansible_network_os  |	yes	   |	Specifies the network type for the connection to the remote device			            |
ansible_connection  |	yes	   |	Specifies the connection plugin                                                                     |

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
              - name: Fabric Replace Nodes
                dellemc.sfs.sfs_fabric_replace:
                  old_service_tag: "HMXBPK2"
                  fabric_id: "66e7c2b7-78b7-4be2-ab3c-36fababee4d9"
                  new_service_tag: "97JBJ23"
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result
	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml



