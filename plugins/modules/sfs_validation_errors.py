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
The module file for sfs_validation_errors
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: get_sfs_validation_errors
short_description: GET Validation errors on Dell SmartFabric Services.
description:
  - This module provides validation erros on Dell SmartFabric Services.
author: Kalaivani Baskaran <kalaivanibaskaran.ba@Dellteam.com>
"""
EXAMPLES = '''
Copy below YAML into a playbook (e.g. play.yml) and run as follows:

#$ ansible-playbook -i inventory play.yaml
- hosts: all
  gather_facts: false
  collections:
    dellemc.sfs
  tasks:
    - name: Get Validation Errors
      block:
        - name: Validation Errors
          dellemc.sfs.sfs_validation_errors:
          register: result
    - name: Debug the result
      debug: var=result
'''


from ansible_collections.dellemc.sfs.plugins.module_utils.sfs.sfs import SFSConfig, extract_id_value
from ansible.module_utils.basic import AnsibleModule


class SFSValidationErrors(SFSConfig):
    def __init__(self):
        argument_spec = {
            'state': {
                'type': 'str',
                'default': "present",
                'required': False
            }
        }
        module = AnsibleModule(argument_spec=argument_spec)
        SFSConfig.__init__(self, module, False)
        self.payload_arg_map = {}
        self.path = "ValidationErrors?$expand=ValidationErrors"
        self.is_method_get_only = True


if __name__ == "__main__":
    SFSValidationErrors().execute_module()
