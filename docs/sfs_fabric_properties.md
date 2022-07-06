Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_fabric_properties
=====================
This task facilitates the configuration of SmartFabric properties and its attributes through REST calls. The sfs-fabric-properties uses the REST API to configure a Dell EMC SmartFabric Services. 

PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
 
Ensure that all the NODES in the setup are up & in good state and part of cluster.
IP address in the URL is leader node IP.
Personality level configuration should be configured carefully by making sure all the attributes are filled with required values you are interested in since it affects all the nodes
All the NODES will be rebooted automatically once these configurations are applied through REST API. Changes will be effective only after reboot.

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

sfs_fabric_properties keys
--------------------------

Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
leaf_asn	      |	integer	| Configures the fabric leaf ASN value      |	Dell Solutions |
spine_asn	      |	integer	| Configures the fabric spine ASN value	    |	Dell Solutions |
private_subnet_prefix |	string	| Configures private subnet IP addressing   |	Dell Solutions |
private_prefix_len    |	integer	| Configures private subnet prefix length   |	Dell Solutions |
global_subnet_prefix  |	string	| Configures global subnet IP addressing    |	Dell Solutions |
global_prefix_len     |	integer	| Configures global subnet prefix length    |	Dell Solutions |
client_control_vlan   |	integer	| Configures client control VLAN ID	    |	Dell Solutions |
client_management_vlan|	integer	| Configures client management VLAN ID	    |	Dell Solutions |
domain_id|integer| Configures Domain ID | Dell Solutions |
designated_leader_nodes | list | Configures Designated Leader Nodes | Dell Solutions |
designated_leader_backOff_timer | integer | Configures Designated Leader BackOff Timer | Dell Solutions |

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
              - name: Fabric properties
                dellemc.sfs.sfs_fabric_properties:
                  leaf_asn: 65012
                  spine_asn: 65013
                  private_subnet_prefix: "172.16.0.0"
                  private_prefix_len: 16
                  global_subnet_prefix: "172.30.0.0"
                  global_prefix_len: 16
                  client_control_vlan: 3939
                  client_management_vlan: 4091
                  Stp_mode: "mst"
                  designated_leader_backOff_timer: 3
                  designated_leader_nodes: [ ]
                  description: "SFS L3 Fabric Global Configurations"
                  domain_id: 100
                  mdns_publish: "disable"
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result
	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml

