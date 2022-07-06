Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
==================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_virtual_network
===================
This module  facilitates the configuration of SFS virtual networks and its attributes through REST calls. It supports CREATE, UPDATE, and DELETE operations. The sfs-virtual-network role uses REST APIs to configure Dell EMC SmartFabric Services.

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

sfs_virtual_network keys
--------------------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
virtual_network_name      |string| Configure the SFS virtual network name    |	Dell Solutions |
virtual_network_description    |string| Configure the SFS virtual network description	    |	Dell Solutions |
vxlanvni |integer| Configure the virtual network VNI value   |	Dell Solutions |
vltvlanid    |	integer	| Configures the virtual network VLT VLAN ID value   |	Dell Solutions |
virtual_network_type  |	string	| Configure the virtual network type; General Purpose (Bronze)/General Purpose (Silver), General Purpose (Gold), General Purpose (Platinum), Cluster Interconnect, Hypervisor Management, Storage - iSCSI, Storage - FCoE, Storage - Data Replication, VM Migration, VMWare FT Logging    |	Dell Solutions |
gateway_ip_address     |string	| Configures virtual network gateway IP address    |	Dell Solutions |
gateway_mac_address   |string	| Configures virtual network gateway MAC address    |	Dell Solutions |
prefix_length  |integer	| Configure the prefix length    |	Dell Solutions |
address_family	|string: inet|Configures virtual network address family|Dell Solutions|
helper_address	|list|Configures virtual network helper address|Dell Solutions|
ip_address_list|list|Configures list of virtual network IPv4 addresses|Dell Solutions|
tenant_name|str|Configures tenant_name|Dell Solutions|
state|string: absent,present*|Removes the SFS virtual network if set to absent|Dell Solutions |

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
              - name: Virtual Network
                dellemc.sfs.sfs_virtual_network:
                  virtual_network_name: "vnet604"
                  virtual_network_description: "vnet604 Create"
                  virtual_network_type: "VXLAN"
                  vxlanvni: 1604
                  vltvlanid: 604
                  gateway_ip_address: "172.17.105.1"
                  gateway_mac_address: "00:11:12:01:23:36"
                  prefix_length: 24
                  address_family: "inet"
                  tenant_name: "tenantname_1"
                  ip_address_list:
                      - "172.17.105.2"
                      - "172.17.105.3"
                      - "172.17.105.4"
                  helper_address: ["10.10.10.10","11.11.11.11","12.12.12.12"]
                  state: present
                register: result

          - name: Debug the result
            debug: var=result
	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml




