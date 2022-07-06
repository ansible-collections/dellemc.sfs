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
[httpapi]()|Use Ansible HTTPAPI to run commands on Dell EMC SmartFabric Services

Collection core modules
------------------------
Name | Description | Connection type
---- | ----------- | ---------------
[**sfs_setup**]()|Manage configuration of L3 Fabric setup|ansible.netcommon.httpapi
[**sfs_port_breakout**]()|Manage port breakout configuration|ansible.netcommon.httpapi
[**sfs_port_properties**]()|Manage port properties configuration|ansible.netcommon.httpapi
[**sfs_fabric_properties**]()|Manage L3 Fabric properties configuration|ansible.netcommon.httpapi
[**sfs_network**]()|Manage network configuration|ansible.netcommon.httpapi
[**sfs_uplink**]()|Manage uplink configuration|ansible.netcommon.httpapi
[**sfs_virtual_network**]()|Manage virtual network configuration|ansible.netcommon.httpapi
[**sfs_server_profile**]()|Manage server profile configuration|ansible.netcommon.httpapi
[**sfs_server_interface_profile**]()|Manage server interface profile configuration|ansible.netcommon.httpapi
[**sfs_aaa**]()|Manage authentication, authorization and accounting configuration|ansible.netcommon.httpapi
[**sfs_acl**]()|Manage Access control list configuration|ansible.netcommon.httpapi
[**sfs_dns**]()|Manage DNS configuration|ansible.netcommon.httpapi
[**sfs_ntp**]()|Manage NTP configuration|ansible.netcommon.httpapi
[**sfs_route_policy**]()|Manage route policy configuration|ansible.netcommon.httpapi
[**sfs_node_policy_mapping**]()|Manage node policy configuration|ansible.netcommon.httpapi
[**sfs_preferred_master**]()|Manage preferred master configuration|ansible.netcommon.httpapi
[**sfs_prefix_list**]()|Manage prefix list configuration|ansible.netcommon.httpapi
[**sfs_snmp**]()|Manage SNMP configuration|ansible.netcommon.httpapi
[**sfs_syslog**]()|Manage syslog configuration|ansible.netcommon.httpapi
[**sfs_validation_errors**]()|Get validation errors in L3 fabric|ansible.netcommon.httpapi
[**sfs_backup_restore**]()|Manage backup restore configuration|ansible.netcommon.httpapi
[**sfs_nodes**]()|Manage nodes configuration|ansible.netcommon.httpapi
[**sfs_VSAN_stretched_cluster**]()|Manage VSAN stretched cluster configuration|ansible.netcommon.httpapi
[**sfs_fabric_handler**]()|Manage fabric handler configuration|ansible.netcommon.httpapi
[**sfs_rest**]()|Manage rest configuration|ansible.netcommon.httpapi

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

