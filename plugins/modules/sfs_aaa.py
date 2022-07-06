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
The module file for sfs_aaa
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfs_aaa
short_description: Configure authentication on Dell SmartFabric Services.
description:
  - This module is used to manage authentication.
author: Ranjith Sunkesula <Ranjith_Senkesula@Dellteam.com>
options:
  method_list:
    description:
      - Configures the authentication method.
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
        - name: aaa_authentication_method configurations
          dellemc.sfs.sfs_aaa:
            method_list: ["local", "radius", "tacacs"]
            state: 'present'
          register: result

    - name: Debug the result
      debug: var=result
'''

from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class SFSAAA(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            },
            'aaa_authentication_method': {
                'type': 'str',
                'required': False
            },
            'method_list': {
                'type': 'list',
                'required': False
            }


        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            'MethodList': 'method_list'
        }

        self.path = "NetworkFabricGlobalConfig/AAA"
        self.resource_id = self.module.params['aaa_authentication_method']


if __name__ == "__main__":
    SFSAAA().execute_module()
