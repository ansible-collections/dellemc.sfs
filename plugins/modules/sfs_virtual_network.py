#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sfs_virtual_network
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: configure_system virtual network
short_description: Configure virtual network  on Dell SmartFabric Services.
description:
  - This module is used to manage virtual network configuration.
author: Ranjith Sunkesula <Ranjith_Senkesula@Dellteam.com>
options:
  virtual_network_name:
    description:
      - Configures the SFS virtual network name.
    type: str
    required: False
  virtual_network_description:
    description:
      - Configures the SFS virtual network description.
    type: str
    required: False
  vxlanvni:
    description:
      - Configures the the virtual network VNI value.
    type: int
    required: False
  vltvlanid:
    description:
      - Configures the the virtual network VLT VLAN ID value.
    type: int
    required: False
  virtual_network_type:
    description:
      - Configures the virtual network type.
    type: str
    required: False
  gateway_ip_address:
    description:
      - Configures virtual network gateway IP address.
    type: str
    required: False
  gateway_mac_address:
    description:
      - Configures virtual network gateway MAC address.
    type: str
    required: False
  prefix_length:
    description:
      - Configures the prefix length.
    type: int
    required: False
  address_family:
    description:
      - Configures virtual network address family.
    type: str
    required: False
  helper_address:
    description:
      - Configures virtual network helper address.
    type: list
    required: False
  ip_address_list:
    description:
      - Configures list of virtual network IPv4 addresses.
    type: list
    required: False
  state:
    description:
      - The state the configuration should be left in.
    type: str
    default: present
    required: False
"""
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inventory play.yaml
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
              ip_address_list:
                - "172.17.105.2"
                - "172.17.105.3"
                - "172.17.105.4"
              helper_address: ["10.10.10.10","11.11.11.11","12.12.12.12"]
              state: present
           register: result

    - name: Debug the result
      debug: var=result
'''

from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class SFSVirtualNetwork(SFSConfig):
    def __init__(self):
        argument_spec = {
            'virtual_network_name': {
                'type': 'str',
                'required': True
            },
            'virtual_network_description': {
                'type': 'str',
                'required': False
            },
            'vxlanvni': {
                'type': 'int',
                'required': True
            },
            'vltvlanid': {
                'type': 'int',
                'required': True
            },
            'virtual_network_type': {
                'type': 'str',
                'required': True,
            },
            'gateway_ip_address': {
                'type': 'str',
                'required': False
            },
            'gateway_mac_address': {
                'type': 'str',
                'required': False
            },
            'prefix_length': {
                'type': 'int',
                'required': False
            },
            'address_family': {
                'type': 'str',
                'required': False,
                'choices': ['inet']
            },
            'helper_address': {
                'type': 'list',
                'required': False
            },
            'state': {
                'type': 'str',
                'required': False,
                'default': 'present'
            },
            'ip_address_list': {
                'type': 'list',
                'required': False
            },
            'tenant_name': {
                'type': 'str',
                'required': False
            }
        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            "VirtualNetworkName": 'virtual_network_name',
            "VirtualNetworkType": 'virtual_network_type',
            "VxlanVni": 'vxlanvni',
            "VltVlanid": 'vltvlanid',
            "Description": 'virtual_network_description',
            "GateWayIpAddress": 'gateway_ip_address',
            "PrefixLen": 'prefix_length',
            "AddressFamily": 'address_family',
            "IpAddressList": 'ip_address_list',
            "GatewayMacAddr": 'gateway_mac_address',
            "HelperAddress": 'helper_address',
            "TenantName": 'tenant_name'}
        self.path = "VirtualNetworks"
        self.resource_id = self.module.params['virtual_network_name']


if __name__ == "__main__":
    SFSVirtualNetwork().execute_module()
