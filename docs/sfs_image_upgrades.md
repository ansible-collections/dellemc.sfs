Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_image_upgrades
==================
This task facilitates upgrades or installation of a software image through REST calls. The sfs-image-upgrade uses the REST API to configure a Dell EMC SmartFabric Services. 

PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
The Image upgrade requires an SSH connection for connectivity to a Dell EMC OS10 device.

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

sfs_image_upgrades keys
-----------------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
protocol	      |	string	| PROTOCOL  action key for connection      |	Dell Solutions |
image_type	      |	string	| IMAGE-TYPE action key for image upgrade	    |	Dell Solutions |
reboot_strategy |	string	| REBOOT-STRATEGY action key for image upgrade   |	Dell Solutions |
image_url    |	string	| Configures the URL path to the image file   |	Dell Solutions |
nodes  |	string	| Configures NODES to the image upgrade    |	Dell Solutions |
download_parallel     |	bool	| Configures DOWNLOAD-PARALLEL to the image upgrade    |	Dell Solutions |

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
	node1 ansible_host=100.104.35.72 
 
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
              - name: SFS image Upgrade
                dellemc.sfs.sfs_image_upgrades:
                  image_url: '/home/Ranjith/os10_images/PKGS_OS10-Enterprise-10.5.3.0DEV.6554buster-installer-x86_64.bin'
                  image_type: 'OS10-BINARY'
                  reboot_strategy: 'PARALLEL'
                  protocol: 'HTTP'
                  download_parallel: 'True'
                register: result

          - name: Debug the result
            debug: var=result
	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml

