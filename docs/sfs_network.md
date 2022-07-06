Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs-network
===========
This module facilitates the configuration of SFS networks and its attributes through REST calls. VXLAN, L3, and L3_ROUTED network types are supported. SFS network CREATE, UPDATE and DELETE operations are supported.
The sfs-network uses REST APIs to configure Dell EMC SmartFabric Services.

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

sfs_network keys
----------------

Key		        |	Type		|	Description			    			|	Support         |
------------------------|-----------------------|---------------------------------------------------------------|-----------------------|
network_id		| string		| Configures the SFS network identification as a unique ID	|   Dell Solutions     	|		
network_name		| string		| Configures the SFS network name				|   Dell Solutions     	|
network_description	| string		| Configures the SFS network description			|   Dell Solutions     	|
vlan_min		| integer		| Configures the VLAN tag start value; vlan_min and vlan_max shall be same in case of single tag VLAN| Dell Solutions      |
vlan_max 		| integer		| Configures the VLAN tag end value; vlan_min and vlan_max shall be same in case of single tag VLAN|   Dell Solutions      |
network_type 		| string:L3, L3_ROUTED,VXLAN, GeneralPurpose| Configures the type of SFS network	|   Dell Solutions	|
qos_priority 		|  string: Platinum,Gold, System,Bronze, Silver,Iron* 	| Configures qos_priority as a string|   Dell Solutions	|
address_family 		| string: inet		| Configures address_family as a string				|   Dell Solutions	|
prefix_length  		| integer		| Configures the prefix length					|   Dell Solutions	|
ip_address_list		| list			| Configures a network IP address list				|   Dell Solutions	|
helper_address		| list			| Configures the network helper address				|   Dell Solutions	|
gateway_ip_address	| list			| Configures a network gateway IP address			|   Dell Solutions	|
virtual_network		| string		| Configure a virtual network					|   Dell Solutions	|
route_map		| string		| Configure the route map					|   Dell Solutions	|
rack_settings	|list	|Configures the RackSettings	|Dell Solutions		|
originator	| string	| Configure a Originator	| Dell Solutions	|
State			| string: absent,present*| Removes the SFS network if set to absent			|   Dell Solutions	|

Connection variables
--------------------
Ansible Dell EMC SmartFabric Services require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible directories, or inventory or in the playbook itself.

Key		    |	Required   |            	Choices	Description								    |
--------------------|--------------|--------------------------------------------------------------------------------------------------------|
ansible_host	    |	yes	   |	Specifies the hostname or IP address to connect to the remote device over the specified transport  |
ansible_user	    |	yes	   |	Specifies the username that authenticates the connection to the remote device			    |	
ansible_password    |	yes	   |	Specifies the password that authenticates the connection to the remote device			    |
ansible_network_os  |   yes        |    Specifies the network type for the connection to the remote device                                  |
ansible_connection  |   yes        |    Specifies the connection plugin 	|

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
                - name: sfs_network
                  dellemc.sfs.sfs_network:
                    network_name: "sfs_network"
                    network_id: "Leaf-test-GeneralPurpose"
                    vlan_min: 752
                    vlan_max: 752
                    qos_priority: "Gold"
                    network_type: "GeneralPurpose"
                    network_description: "SFS Network Create Test From Ansible-ddddd"
                    address_family: "inet"
                    virtual_network: "vn752"
                    state: "present"
                  register: result

                - name: Update Network
                  dellemc.sfs.sfs_network:
                    network_id: "My_L3_ROUTED_Network_Id_1"
                    network_name: "My_L3_ROUTED_Network_Name_1"
                    network_description: "My_L3_ROUTED_Network_Description_1"
                    network_type: "L3_ROUTED"
                    qos_priority: "Bronze"
                    address_family: "inet"
                    prefix_length: 24
                    ip_address_list: ["192.168.1.2","192.168.1.4"]
                    helper_address: ["10.10.10.10","11.11.11.11"]
                    gateway_ip_address: ["192.168.1.3"]
                    route_map: "routemap1"
                    state: "present"
                  register: result

                - name: Update VXLAN Network
                  dellemc.sfs.sfs_network:
                    network_id: "My_VXLAN_Network_Id"
                    vlan_min: 400
                    vlan_max: 400
                    qos_priority: "Bronze"
                    network_type: "VXLAN"
                    virtual_network: "vnet1"
                    network_name: "My_VXLAN_Network_Id"
                    originator: "vCenter_user"
                    network_description: "My_VXLAN_Network_Description"
 	            state: "present"
                  register: result

	
                - name: MULTIRACK L3 VLAN
                  dellemc.sfs.sfs_network:
                    network_id: "SREEJITHNETWORK1"
                    network_name: "Network1"
                    network_description: "My_L3 VLAN_Network_Description_1"
                    vlan_max: 401
                    vlan_min: 401
                    qos_priority: "Iron"
                    network_type: "MULTIRACK_L3_VLAN"
                    rack_settings: [{ RackID: "6298f46c-b8a8-4548-8bfb-14ee34303147", AddressFamily: "inet", PrefixLen: 24, GateWayIpAddress: ["10.1.1.254"],
                    IpAddressList: ["10.1.1.1","10.1.1.2"], HelperAddress: ["10.10.10.10","10.11.11.11"] }]
                    state: "present"
                  register: result

            - name: Debug the result
              debug: var=result


             	
**Run**

ansible-playbook -i inventory Playbook.yaml




