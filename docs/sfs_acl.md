Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_acl
=======
This task facilitates the configuration of acl and its attributes through REST calls. The sfs-acl uses the REST API to configure a Dell EMC SmartFabric Services. 

PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
uplink-acl is the name of ACL you would like to be configured now which is the key and mandatory for post operation
ACL name (Name) attribute MUST be unique for every ACL to be configured

Delete ACL will delete all rules associated with this ACL and delete ACL also
uplink-acl is the name of ACL you have configured already which is the key for delete operation

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

sfs_acl keys
------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
name |	string	| Configures name   |	Dell Solutions |
description_string  |	string	| Configures global subnet IP addressing    |	Dell Solutions |
interface| list | Configures interface | Dell Solutions |

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
	node1 ansible_host=100.104.35.71 
 
	[os10:vars]
	ansible_ssh_user=admin      # user mush be REST_USER for only "sfs_acl_mapping"
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
              - name: ACL configurations
                dellemc.sfs.sfs_acl:
                  name: "uplink-acl"
                  description_string: "uplinkAclDescription"
                  state: 'present'
                register: result

              - name: Apply Acl on interface
                dellemc.sfs.sfs_acl_mapping:
                  interface: [{"name":"ethernet1/1/14:1", "dell-policy:policy-acl-config":{"access-group":[{"role":"ipv4","direction":"in","vrf":"0","name":"uplink-acl"}]}}]
                register: result


          - name: Debug the result
            debug: var=result
            	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml




