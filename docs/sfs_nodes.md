Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_nodes
=========
This module facilitates the configuration of SFS nodes and its attributes through REST calls. 'nodehandler', 'blink', 'unblink', 'reboot', 'rollback', 'factorydefault' types are supported. The sfs-nodes uses REST APIs to configure Dell EMC SmartFabric Services.


PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
Make sure NODE in the setup are up & in good state and part of cluster.
IP address in the URL is master node IP.
The NODE will be rebooted automatically once these configurations are applied through REST API. Changes will be effective for 'reboot', 'rollback', 'factorydefault'.
The NODE Hostname will be changed automatically once configuration are applied through REST API. Changes will be effective for 'nodehandler'

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

sfs_nodes keys
--------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
node_id |	string	| Configures node_id   |	Dell Solutions |
name|	string  | Configures the Hostname   |        Dell Solutions |
description|	string  | Configures the description   |        Dell Solutions |

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
              - name: Nodes Handler
                dellemc.sfs.sfs_nodes:
                  action:  "nodehandler"        # ['nodehandler', 'blink', 'unblink', 'reboot', 'rollback', 'factorydefault']
                  node_id: "VB9D06E"
                  name: "Leaf01"
                  description: "Ansible_test"
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result


       - hosts: all
        gather_facts: false
        collections:
          - dellemc.sfs
        tasks:
          - name: Provision Configs
            block:
              - name: Nodes Handler
                dellemc.sfs.sfs_nodes:
                  action:  "reboot"        # ['nodehandler', 'blink', 'unblink', 'reboot', 'rollback', 'factorydefault']
                  node_id: "VB9D06E"
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result

**Run**

ansible-playbook -i inventory Playbook.yaml

