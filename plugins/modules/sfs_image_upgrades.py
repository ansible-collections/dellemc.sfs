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
The module file for sfs_image_upgrades
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: configure_sfs_image_upgrade
short_description: Upgrades or installs software image on Dell SmartFabric Services.
description:
  - This module is used to upgrade or install the software image on switches.
author: Ranjith.S <ranjith.senkesula@Dellteam.com>
options:
  protocol:
    description:
      - Protocol for connection.
    type: str
    required: False
  image_type:
    description:
      - Type of the OS10 image.
    type: str
    required: False
  reboot_strategy:
    description:
      - Reboot strategy for image upgrade.
    type: str
    required: False
  image_url:
    description:
      - URL path to the OS10 image file.
    type: str
    required: False
  nodes:
    description:
      - Node details.
    type: str
    required: False
  download_parallel:
    description:
      - Downloads the image parallelly on the switches during upgrade.
    type: bool
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
    -  dellemc.sfs
  tasks:
    - name: Provision Configs
      block:

        - name: SFS image Upgrade
          dellemc.sfs.sfs_image_upgrades:
            image_url: '/home/Ranjith/os10_images/PKGS_OS10-Enterprise-10.5.3.0DEV.6554buster-installer-x86_64.bin'
            image_type: 'OS10-BINARY'
            reboot_strategy: 'PARALLEL'
            protocol: 'HTTP'
            download_parallel: 'True'
          register: result

    - name: Debug the result
      debug: var=result


'''


from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class SFSImageUpgrades(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            },
            'image_url': {
                'type': 'str',
                'required': False
            },
            'reboot_strategy': {
                'type': 'str',
                'required': False
            },
            'protocol': {
                'type': 'str',
                'required': False
            },
            'image_type': {
                'type': 'str',
                'required': False
            },
            'nodes': {
                'type': 'str',
                'required': False
            },
            'download_parallel': {
                'type': 'bool',
                'required': False
            }

        }

        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module)
        self.payload_arg_map = {
            'PROTOCOL': 'protocol',
            'IMAGE-TYPE': 'image_type',
            'REBOOT-STRATEGY': 'reboot_strategy',
            'IMAGE-URL': 'image_url',
            'NODES': 'nodes',
            'DOWNLOAD-PARALLEL': 'download_parallel'
        }
        self.path = "ImageUpgrades"
        self.is_get_running = False
        self.content_type = 'application/octet-stream'
        self.headers = True


if __name__ == "__main__":
    SFSImageUpgrades().execute_module()
