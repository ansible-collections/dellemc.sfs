Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_node_policy_mapping
=======================
This module facilitates the configuration of SFS node-policy-mapping and its attributes through REST calls. It supports CREATE,  DELETE operations. Route policy must be created using the sfs-route-policy before the policy mapping is invoked.

The sfs-node-policy-mapping uses REST APIs to configure Dell EMC SmartFabric Services.

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

sfs_node_policy_mapping  keys
-----------------------------

Key	        |	Type			|	Description			    	|    Support      |
----------------|-------------------------------|-----------------------------------------------|-----------------|
node     	| string			| Configures the node as string    		|  Dell Solutions |
policy_list   	| list				| Configures the policy list	    		|  Dell Solutions |
state		| string: absent,present*	|  Removes the SFS network if set to absent	|  Dell Solutions |

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
              - name: Node Policy Mapping
                dellemc.sfs.sfs_node_policy_mapping:
                  node: 19HQXC2
                  policy_list:
                    - policybgp100
                    - policybgp101
                  state: "present"  
                register: result

          - name: Debug the result
            debug: var=result
	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml




