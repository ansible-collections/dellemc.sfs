Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_uplink
==========
This module facilitates the configuration of SFS uplinks and its attributes through REST calls. It supports CREATE, UPDATE, and DELETE operations. The sfs-uplink uses REST APIs to configure Dell EMC SmartFabric Services.

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

sfs_uplink keys
---------------
Key		      	|	Type	|	Description			    |	Support        |
------------------------|---------------|-------------------------------------------|------------------|
uplink_name	      	|   string	| Configures the SFS uplink name |	Dell Solutions |
uplink_description    	|   string	| Configures the SFS uplink description |	Dell Solutions |
uplink_id 	      	|   string	| Configures the SFS uplink identification as a unique ID |	Dell Solutions |
media_type    	      	| string: Ethernet| Configures the media type as a string (default Ethernet) |	Dell Solutions |
Node                  	|   string	| Configures the device service tag |	Dell Solutions |
configuration_interfaces|   list	| Configures the interface list |	Dell Solutions |
tagged_networks   	|   list	| Configures the tagged networks list |	Dell Solutions |
untagged_network	|   string	| Configures the untagged network |	Dell Solutions |
lag_type		|string: Static,Dynamic,None*| Configures the LAG type |  Dell Solutions |
uplink_type		|string: JumpBox,Normal*| Configures the uplink type |  Dell Solutions |
native_vlan	|  integer	|  Configures the NativeVlan	|  Dell Solutions	|
ingress_ipacl	|  string	|  Configures the IngressIpAcl	|  Dell Solutions  	|
State			|string: absent,present*| Removes the SFS uplink if set to absent |  Dell Solutions |

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
              - name: Update uplink
                dellemc.sfs.sfs_uplink:
                  uplink_id: 1
                  node: 97JBJ23
                  uplink_name: New Uplink
                  uplink_description: New Uplink description 2
                  configuration_interfaces:
                    - 97JBJ23:ethernet1/1/41
                    - 97K5J23:ethernet1/1/41
                  tagged_networks:
                    - VLAN1200
                  untagged_network: VLAN 1
                  native_vlan: 100
                  lag_type: "None"
                  uplink_type: "Normal"
                  ingress_ipacl: "UplinkIngressIpACL"
                  state: "present"
                register: result

          - name: Debug the result
            debug: var=result
 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml




