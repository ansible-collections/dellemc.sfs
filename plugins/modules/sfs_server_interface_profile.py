#!/usr/bin/env python
# pylint: disable=consider-using-f-string
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
The module file for sfs_server_profile
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfs_server_profile
short_description: Configure server interface handler on Dell SmartFabric Services.
description:
  - This module is used to manage server interfaces.
author: Ranjith Sunkesula <Ranjith_Senkesula@Dellteam.com>
options:
  server_id:
    description:
      - Configures the server interface ID.
    type: str
    required: False
  interface_id:
    description:
      - Configures the interface ID.
    type: str
    required: False
  native_vlan:
    description:
      - Configures native VLAN.
    type: str
    required: False
  untagged_network:
    description:
      - Configures the untagged network.
    type: dict
    required: False
  nic_bonded:
    description:
      - Configures NIC bonding.
    type: bool
    required: False
  networks:
    description:
      - Configures networks.
    type: list
    required: False
  bandwidth_partition:
    description:
      - Configures bandwidth partition.
    type: list
    required: False
  staticOnboard_interface:
    description:
      - Configures static onboarding interface.
    type: str
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
        - name: Server Interface Profiles
          dellemc.sfs.sfs_server_interface_profile:
            server_id: SERVER
            interface_id: "NIC11"
            native_vlan: 1012
            nic_bonded: True
            staticOnboard_interface: "OS10SIM:ethernet1/1/16"
            networks: [{ "NetworkId": "NETWORK1"},{ "NetworkId": "NETWORK2"}]
            bandwidth_partition: [ {"PercentageBandwidth": 85,  "TrafficType": "iSCSI" }, {"PercentageBandwidth": 15, "TrafficType": "FC" } ]
            untagged_network: {"NetworkId": "Network3"}
            state: 'present'
          register: result

     - name: Debug the result
       debug: var=result
'''


from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class ServerInterfaceProfile(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            },
            'server_id': {
                'type': 'str',
                'required': False
            },
            'bonding_technology': {
                'type': 'str',
                'required': False
            },
            'interface_id': {
                'type': 'str',
                'required': False
            },
            'native_vlan': {
                'type': 'int',
                'required': False
            },
            'bandwidth_partition': {
                'type': 'list',
                'required': False
            },
            'percentage_bandwidth': {
                'type': 'int',
                'required': False
            },
            'traffic_type': {
                'type': 'str',
                'required': False
            },
            'network_id': {
                'type': 'str',
                'required': False
            },
            'networks': {
                'type': 'list',
                'required': False
            },
            'untagged_network': {
                'type': 'dict',
                'required': False
            },
            'staticOnboard_interface': {
                'type': 'str',
                'required': False
            },
            'nic_bonded': {
                'type': 'bool',
                'required': False
            }
        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            'ServerId': 'server_id',
            'BondingTechnology': 'bonding_technology',
            'StaticOnboardInterface': 'staticOnboard_interface',
            'InterfaceId': 'interface_id',
            'NativeVlan': 'native_vlan',
            'NICBonded': 'nic_bonded',
            'BandwidthPartition': 'bandwidth_partition',
            'Networks': 'networks',
            'UntaggedNetwork': 'untagged_network'
        }
        self.path = "ServerProfiles('%s')/ServerInterfaceProfiles" % (self.module.params['server_id'])
        self.resource_id = self.module.params['interface_id']


if __name__ == "__main__":
    ServerInterfaceProfile().execute_module()
