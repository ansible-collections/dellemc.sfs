Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================

Collection contents
-------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

sfs_acl_rules
=============
This task facilitates the configuration of ACL rules and its attributes through REST calls. The sfs-acl-rules uses the REST API to configure a Dell EMC SmartFabric Services.

PLEASE READ NOTES BEFORE CONFIGURING
------------------------------------
MUST configure ACL using ACL Post URL before configuring ACL Rules. Refer sfs_acl for configuring ACL container first.

Assuming that uplink-acl is already configured through ACL POST REST API by the user, proceed for ACL Rule configuration.

ACL Rules are CREATE and DELETE ONLY operation.

Payload given in next column are for below examples:

seq 1 deny ip any 10.10.0.33 255.255.255.255

seq 2 permit tcp any 10.10.0.64 255.255.255.224 eq 443

SeqNo is mandatory and it MUST be unique for every rule to be configured

If DestinationAny or SourceAny is true, then corresponding source or destination prefix and mask attribute is ignored and user don't need to give those attributes as part of POST  Payload.

IpProtocol: 4 for IP, 6 for TCP, 17 for UDP

Source and Destination Port numbers shall be valid non zero values

Counter enabled automatically for all ACL Rules configured

Comparator values supported for ACL are one of these values: "eq" , "ne", "ge", "le"

Comparator Port attributes are applicable ONLY for TCP or UDP Protocols.

PacketHandling is either "permit" or "deny".

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

sfs_acl_rules keys
------------------
Key		      |	Type	|	Description			    |	Support        |
----------------------|---------|-------------------------------------------|------------------|
name	      |	string	| Configures the name      |	Dell Solutions |
seq_no	      |	integer	| Configures SeqNo value	    |	Dell Solutions |
destination_prefix |	string	| Configures DestinationPrefix IP addressing   |	Dell Solutions |
destination_mask   |	string	| Configures the DestinationMask   |	Dell Solutions |
source_prefix  |	string	| Configures SourcePrefix IP addressing    |	Dell Solutions |
source_mask     |	string	| Configures SourceMask    |	Dell Solutions |
destination_any   |	bool	| Configures DestinationAny	    |	Dell Solutions |
source_any|	bool	| Configures SourceAny    |	Dell Solutions |
ip_protocol	| integer| Configures IpProtocol | Dell Solutions |
source_port_range_comparator_port | integer | Configures SourcePortRangeComparatorPort | Dell Solutions |
destination_port_range_comparator_port | integer | Configures DestinationPortRangeComparatorPort | Dell Solutions |
source_port_range_comparator	|  string	| Configures SourcePortRangeComparator	| Dell Solutions |
dest_port_range_comparator	|  string	| Configures SourcePortRangeComparator	| Dell Solutions |
packet_handling		| string	| Configures PacketHandling	| Dell Solutions	|
remark	| string	| Configures remark	| Dell Solutions        |

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
              - name: ACLRules configurations
                dellemc.sfs.sfs_acl_rules:
                  name: "uplink-acl"
                  seq_no: 9
                  destination_prefix: "10.10.0.33"
                  destination_mask: "255.255.255.255"
                  source_prefix: "10.1.1.1"
                  source_mask: "255.255.255.255"
                  destination_any: false
                  source_any: true
                  ip_protocol: 4
                  source_port_range_comparator_port: 200
                  destination_port_range_comparator_port: 8000
                  source_port_range_comparator: "ge"
                  dest_port_range_comparator: "eq"
                  packet_handling: "deny"
                  remark: "ipacl9remark"            ## Remark must be configured without any other additional attributes other than SeqNo. ##
                  state: 'present'
                register: result

          - name: Debug the result
            debug: var=result
	 	
             	
**Run**

ansible-playbook -i inventory Playbook.yaml

