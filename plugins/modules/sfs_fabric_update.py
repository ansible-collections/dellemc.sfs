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
The module file for sfs_fabric_update
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfs_fabric_update
short_description: Configure fabric handler on Dell SmartFabric Services.
description:
  - This module is used to manage fabric handler.
author: Ranjith Sunkesula <Ranjith_Senkesula@Dellteam.com>
options:
  fabric_design_mappings:
    description:
      - Configures the fabric design mappings.
    type: str
    required: False
  name:
    description:
      - Configures a name for the fabric.
    type: str
    required: False
  description:
    description:
      - Configures description of the fabric.
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
        - name: Fabric update
          dellemc.sfs.sfs_fabric_update:
            name:  "Some New Fabric"
            description: "This is a new Fabric"
            fabric_id: "f926a2fa-124e-4558-ba11-49127426010c"
            state: 'present'
          register: result


    - name: Debug the result
      debug: var=result
'''


from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible_collections.ansible.netcommon.plugins.module_utils.network.restconf import (
    restconf,)
from ansible.module_utils.basic import AnsibleModule


class SFSFabricUpdate(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            },
            'node_id': {
                'type': 'str',
                'required': False
            },
            'fabric_design': {
                'type': 'str',
                'required': False
            },
            'name': {
                'type': 'str',
                'required': False
            },
            'design_node': {
                'type': 'str',
                'required': False
            },
            'fabric_design_mappings': {
                'type': 'list',
                'required': False
            },
            'nodes': {
                'type': 'list',
                'required': False
            },
            'fabric_id': {
                'type': 'str',
                'required': False
            },
            'description': {
                'type': 'str',
                'required': False
            },
            'physical_node': {
                'type': 'str',
                'required': False
            }

        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            'NodeId': 'node_id',
            'FabricDesignMappings': 'fabric_design_mappings',
            'Nodes': 'nodes',
            'Description': 'description',
            'FabricDesign': 'fabric_design',
            'Name': 'name',
        }
        self.path = "Fabrics"
        self.resource_id = self.module.params['fabric_id']


if __name__ == "__main__":
    SFSFabricUpdate().execute_module()
