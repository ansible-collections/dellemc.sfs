# Copyright (c) 2018 Cisco and/or its affiliates.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
# pylint: disable=redundant-u-string-prefix, bare-except

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
author: Ansible Networking Team
httpapi: sfs
short_description: HttpApi Plugin for devices Dell EMC SmartFabric Services
description:
- This HttpApi plugin provides methods to connect to Dell EMC SmartFabric Services
version_added: 1.0.0
options:
  root_path:
    type: str
    description:
    - Specifies the location of the Restconf root.
    default: ''
    vars:
    - name: ansible_httpapi_sfs_root
"""


import json

from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.plugins.httpapi import HttpApiBase

CONTENT_TYPE = "application/yang-data+json"


class HttpApi(HttpApiBase):
    def __init__(self, connection):
        super(HttpApi, self).__init__(connection)
        self._device_info = None

    def send_request(self, data, **message_kwargs):
        if data:
            data = json.dumps(data)

        path = '/'.join([self.get_option('root_path').rstrip('/'), message_kwargs.get('path', '').lstrip('/')])
        path = '/' + message_kwargs.get('path', '').lstrip('/')

        headers = {
            'Content-Type': message_kwargs.get('content_type') or CONTENT_TYPE,
            'Accept': message_kwargs.get('accept') or CONTENT_TYPE,
        }
        response, response_data = self.connection.send(path, data, headers=headers, method=message_kwargs.get('method'))

        return handle_response(response, response_data, message_kwargs)

    def get_device_info(self):
        if self._device_info:
            return self._device_info

        device_info = {}
        device_info["system-sw-state"] = self.get_system_state()
        device_info["smartfabric-cluster"] = self.get_smartfabric_cluster()
        self._device_info = device_info
        return self._device_info

    def get_system_state(self):
        try:
            result = self.send_request(None, path='/restconf/data/system-sw-state', method="GET")
            if 'dell-system-software:system-sw-state' in result:
                return result['dell-system-software:system-sw-state']
        except:   # nopep8
            return None
        return None

    def get_smartfabric_cluster(self):
        try:
            result = self.send_request(None, path='/restconf/data/dell-smart-fabric:cluster', method="GET")
            if 'dell-smart-fabric:cluster' in result:
                return result['dell-smart-fabric:cluster']
        except:    # nopep8
            return None
        return None

    def send_request_with_header(self, data, headers, **message_kwargs):
        if data:
            data = json.dumps(data)

        path = '/'.join([self.get_option('root_path').rstrip('/'), message_kwargs.get('path', '').lstrip('/')])
        path = '/' + message_kwargs.get('path', '').lstrip('/')
        response, response_data = self.connection.send(path, data, headers=headers, method=message_kwargs.get('method'))
        return handle_response(response, response_data, data)


def handle_response(response, response_data, request_data):
    response_data = response_data.read()
    try:
        if not response_data:
            response_data = ""
        else:
            response_data = json.loads(response_data.decode('utf-8'))
    except ValueError:
        pass

    if isinstance(response, HTTPError):
        if response_data:
            if 'errors' in response_data:
                errors = response_data['errors']['error']
                error_text = '\n'.join((error['error-message'] for error in errors))
            else:
                error_text = response_data
            error_text.update({u'code': response.code})
            error_text.update({u'request_data': request_data})
            raise ConnectionError(error_text, code=response.code)
        raise ConnectionError(to_text(response), code=response.code)
    return response_data
