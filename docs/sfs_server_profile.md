Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Solutions running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_server_profile
==================
This task facilitates the configuration of SFS server handler and server interface handler and its attributes through REST calls. The sfs-server-profiles uses the REST API to configure a Dell EMC SmartFabric Solutions. SFS Server Profile CREATE and DELETE operations are supported.
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

sfs_server_profile keys
-----------------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
server_id	      |	string	| Configures the ServerId      |	Dell Solutions |
bonding_technology	      |	string  | Configures the BondingTechnology	    |	Dell Solutions |
interface_id |	string	| Configures InterfaceId   |	Dell Solutions |
native_vlan    |	string| Configures NativeVlan   |	Dell Solutions |
untagged_network  |	dict	| Configures UntaggedNetwork    |	Dell Solutions |
nic_bonded     |	bool	| Configures NICBonded    |	Dell Solutions |
networks   |	list	| Configures Networks	    |	Dell Solutions |
bandwidth_partition | list | Configues BandwidthPartition | Dell Solutions |
staticOnboard_interface| string| Configures StaticOnboardInterface| Dell Solutions |

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
              - name: Server Profile
                dellemc.sfs.sfs_server_profiles:
                  server_id: SERVER
                  bonding_technology: LACP
                  state: present
                register: result

              - name: Server Interface Profile
                dellemc.sfs.sfs_server_interface_profiles:
                  server_id: SERVER
                  interface_id: "NIC11"
                  native_vlan: 1011
                  nic_bonded: True
                  staticOnboard_interface: "OS10SIM:ethernet1/1/16"
                  networks: [{ "NetworkId": "NETWORK1"},{ "NetworkId": "NETWORK2"}]
                  bandwidth_partition: [ {"PercentageBandwidth": 85,  "TrafficType": "iSCSI" }, {"PercentageBandwidth": 15, "TrafficType": "FC" } ]
                  untagged_network: {"NetworkId": "Network3"}
                  state: present
                register: result

            - name: Debug the result
              debug: var=result

**Run**

ansible-playbook -i inventory Playbook.yaml

