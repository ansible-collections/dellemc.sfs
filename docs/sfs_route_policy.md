Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_route_policy
================
This module facilitates the configuration of route policies and its attributes through REST calls. It supports CREATE and DELETE operations. The route policy must be associated with a node through the sfs-node-policy-mapping.

The sfs_route_policy role uses REST APIs to configure Dell EMC SmartFabric Services.

Installation
------------
The collections tarball built can be installed locally using the following commands:
ansible-galaxy collection build

Once the collections tarball get published locally, install your collection from the tarball using the command
ansible-galaxy collection install dellemc-sfs-1.0.0.tar.gz

module variables
----------------
Variables and values are case-sensitive

sfs_route_policy keys
--------------------------
Key		      	     |	Type			|	Description			    		|	Support  |
-----------------------------|--------------------------|-------------------------------------------------------|----------------|
policy_id	      	     |	string			| Configures the policy ID as an unique ID      	|Dell solutions	 |
policy_name	             |	string			| Configures the policy name as a string	    	|Dell solutions	 |
policy_description    	     |	string			| Configures the policy description   			|Dell solutions	 |
policy_type     	     |	string			| Configures the policy type   				|Dell solutions	 |
address_family_type          |	string			| Configures address_family_type as a string    	|Dell solutions	 |
remote_address               |	string			| Configures remote_address as a string			|Dell solutions  |
remote_loopback_address      |	string  		| Configures remote_loopback_address as a string	|Dell solutions	 |
remote_as		     |	integer 		| Configures remote_as as an integer	    		|Dell solutions	 |
sender_side_loop_detection   |	bool			| Configures sender_side_loop_detection as an integer	|Dell solutions	 |
route_filter_enable	     |	bool			| Configures route_filter_enable as an integer		|Dell solutions	 |
ipv4_nexthop_ip		     |	string			| Configures ipv4_nexthop_ip as a string		|Dell solutions  |
ipv4_address_prefix          |	string			| Configures ipv4_address_prefix as a string		|Dell solutions  |
ipv4_prefix_len		     |	integer			| Configures ipv4_prefix_len as an integer		|Dell solutions  |
ebgpMulti_hop_count| integer    | Configures ebgpMulti_hop_count as an integer  |  Dell solutions       |
bfd_neighbor_enable     |  integer      |  Configures  bfd_neighbor_enable  as an integer       |  Dell solutions       |
advertise_VTEPs    |  integer      |  Configures AdvertiseVTEPs as an integer       |  Dell solutions       |
interconnect_routePolicy    |  integer      |  Configures interconnect_routePolicy as an integer       |  Dell solutions       |
state			     |	string: absent,present*	| Removes the SFS route policy if set to absent		|Dell solutions  |

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
              - name: Route Policy
                dellemc.sfs.sfs_route_policy:
                   policy_id: "policybgp100"
                   policy_name: "policybgp100"
                   policy_description: "description"
                   address_family_type: "ipv4"
                   remote_address: "100.100.100.22"
                   remote_loopback_address: "100.100.100.2"
                   remote_as: 65004
                   policy_type: RoutePolicyEbgp
                   sender_side_loop_detection: 1
                   route_filter_enable: 0
                   ebgpMulti_hop_count: 2
                   bfd_neighbor_enable: 1
                   advertise_VTEPs: 1
                   interconnect_routePolicy: 1
                   state: present 
                 register: result

          - name: Debug the result
            debug: var=result
 	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml

