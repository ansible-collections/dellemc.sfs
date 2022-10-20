Ansible Network Collection for Dell EMC SmartFabric Services by Dell Technologies
=================================================================================
Collection contents
--------------------
This collection includes Ansible core modules and plugins needed to provision and manage Dell EMC Smartfabric Services running Enterprise OS10 Distribution by Dell Technologies. Sample playbooks and documentation are also included to show how the collections can be used.

Supported connections
---------------------
The SFS Ansible collection supports network_cli and httpapi connections.

Plugins
--------
**HTTPAPI plugin**

Name | Description
---- | -----------
httpapi|Use Ansible HTTPAPI to run commands on Dell EMC SmartFabric Services

Collection core modules
------------------------
Name | Description | Connection type
---- | ----------- | ---------------
[**sfs_setup**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_setup.md)|Manage configuration of L3 Fabric setup|ansible.netcommon.httpapi
[**sfs_port_breakout**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_port_breakout.md)|Manage port breakout configuration|ansible.netcommon.httpapi
[**sfs_port_properties**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_port_properties.md)|Manage port properties configuration|ansible.netcommon.httpapi
[**sfs_fabric_properties**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_fabric_properties.md)|Manage L3 Fabric properties configuration|ansible.netcommon.httpapi
[**sfs_network**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_network.md)|Manage network configuration|ansible.netcommon.httpapi
[**sfs_uplink**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_uplink.md)|Manage uplink configuration|ansible.netcommon.httpapi
[**sfs_virtual_network**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_virtual_network.md)|Manage virtual network configuration|ansible.netcommon.httpapi
[**sfs_server_profile**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_server_profile.md)|Manage server profile configuration|ansible.netcommon.httpapi
[**sfs_server_interface_profile**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_server_profile.md)|Manage server interface profile configuration|ansible.netcommon.httpapi
[**sfs_aaa**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_aaa.md)|Manage authentication, authorization and accounting configuration|ansible.netcommon.httpapi
[**sfs_acl**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_acl.md)|Manage Access control list configuration|ansible.netcommon.httpapi
[**sfs_dns**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_dns.md)|Manage DNS configuration|ansible.netcommon.httpapi
[**sfs_ntp**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_ntp.md)|Manage NTP configuration|ansible.netcommon.httpapi
[**sfs_route_policy**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_route_policy.md)|Manage route policy configuration|ansible.netcommon.httpapi
[**sfs_node_policy_mapping**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_node_policy_mapping.md)|Manage node policy configuration|ansible.netcommon.httpapi
[**sfs_preferred_master**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_preferred_master.md)|Manage preferred master configuration|ansible.netcommon.httpapi
[**sfs_prefix_list**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_prefix_list.md)|Manage prefix list configuration|ansible.netcommon.httpapi
[**sfs_snmp**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_snmp.md)|Manage SNMP configuration|ansible.netcommon.httpapi
[**sfs_syslog**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_syslog.md)|Manage syslog configuration|ansible.netcommon.httpapi
[**sfs_validation_errors**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_validation_errors.md)|Get validation errors in L3 fabric|ansible.netcommon.httpapi
[**sfs_backup_restore**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_backup_restore.md)|Manage backup restore configuration|ansible.netcommon.httpapi
[**sfs_nodes**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_nodes.md)|Manage nodes configuration|ansible.netcommon.httpapi
[**sfs_fabric_handler**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_fabric_handler.md)|Manage fabric handler configuration|ansible.netcommon.httpapi
[**sfs_rest**](https://github.com/ansible-collections/dellemc.sfs/blob/main/docs/sfs_rest.md)|Manage rest configuration|ansible.netcommon.httpapi

Installation
------------
Install the latest version of the SFS collection from Ansible Galaxy.

      ansible-galaxy collection install dellemc.sfs

To install a specific version, specify a version range identifier. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

      ansible-galaxy collection install 'dellemc.sfs:>=1.0.0,<2.0.0'

Version compatibility
----------------------
Ansible version 2.10 or later.

Dell EMC SmartFabric Services by Dell Technologies version 10.5.4.0 or later.

Note: Community SFS versions that include the Management Framework container should work as well, however, this collection has not been tested nor validated with community versions, nor is it supported.

Sample playbooks
-----------------
**Inventory**

        [os10]
        node1 ansible_host=100.104.35.71

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

