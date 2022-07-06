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
The module file for sfs_route_maps
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sfs_route_maps
short_description: Configure route maps on Dell SmartFabric Services.
description:
  - This module is used to manage route maps.
author: Ranjith Sunkesula <Ranjith_Senkesula@Dellteam.com>
options:
  map_id:
    description:
      - Configures the route map ID.
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
        - name: Route Maps
          dellemc.sfs.sfs_route_maps:
            map_id: "route-map-1"
            state: present
          register: result

    - name: Debug the result
      debug: var=result

'''


from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class SFSRouteMaps(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            },
            'map_id': {
                'type': 'str',
                'required': False
            }

        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            'MapId': 'map_id'
        }

        self.path = "RouteMaps"
        self.resource_id = self.module.params['map_id']


if __name__ == "__main__":
    SFSRouteMaps().execute_module()