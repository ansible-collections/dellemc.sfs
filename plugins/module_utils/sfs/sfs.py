from __future__ import (absolute_import, division, print_function)
__copyright__ = "(c) Copyright 2021 Dell Inc. or its subsidiaries. All rights reserved."

__metaclass__ = type

# pylint: disable=anomalous-backslash-in-string, singleton-comparison, use-dict-literal, consider-using-f-string, multiple-imports
from ansible.module_utils._text import to_text
from ansible.module_utils.connection import ConnectionError
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    dict_diff,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.restconf import (
    restconf,
)
from ansible.module_utils.connection import Connection
import re
import traceback

# Base url path for SFS REST API
SFS_BASE_REDFISH_PATH = '/redfish/v1/Dnv/'
SFS_BASE_RESTCONF_PATH = '/restconf/data/'


class SFSConfig:
    '''
    Base class configure a single REST Resource Type Endpoint
    To be extended to handle individual Endpoints
    '''
    def __init__(self, module, is_master_check_req=True):
        self.module = module  # AnsibleModule instance
        # Base url path common for all resources extending this class
        # If it differs for any resource type (Ex: OS10 REST endpoints) this
        # can be updated
        self.base_path = SFS_BASE_REDFISH_PATH
        self.path = None  # url path relative to the base path this resource type
        self.resource_id = None  # Id/Key of the Resource being configured
        # Mapping of keys in payload to module args
        # Used while preparing payload. Add entry here for which module arg value
        # can be directly used in payload
        self.payload_arg_map = None
        self.is_master_check_required = is_master_check_req
        self.check_master()  # Check if host is master, otherwise exit
        self.create_method = 'POST'
        self.update_method = 'PUT'
        self.delete_method = 'DELETE'
        self.patch_method = 'PATCH'
        self.patch_support = False
        self.is_method_get_only = False
        self.pass_input_payload = False
        self.post_support = True  # Set to False is POST support is not available when we configure
        # for first time and set to True when POST support is available when we configure for the first time.
        self.redfish_support = True  # Set to True if REDFISH support is available and
        # False if only RESTCONF support is present
        self.is_get_running = True  # Set to True if GET query to get the present configuration before POST/PUT
        # and set to False if GET query to get present config is not required before POST/PUT
        self.content_type = None  # For RESTCONF queries, content_type has to be included
        self.keep_input_payload = False  # For RESTCONF queries, content_type has to be included
        self.headers = None  # Include data as headers

    @property
    def resource_path(self):
        ''' URL path of a particular resource with Id/Key relative to base path '''
        return "%s('%s')" % (self.path, self.resource_id) if self.resource_id else self.path

    @property
    def fullpath(self):
        ''' Full url path including base path for this resource type '''
        return self.base_path + self.path

    @property
    def resource_fullpath(self):
        ''' FUll url path for this particular resource with Id/Key '''
        return self.base_path + self.resource_path

    def check_master(self):
        ''' Function to check if the host is an SFS Master and exit otherwise '''
        if self.is_master_check_required is False:
            return
        device_info = {}
        try:
            device_info = Connection(self.module._socket_path).get_device_info()
            if ('smartfabric-cluster' not in device_info or not device_info['smartfabric-cluster']
                    or device_info['smartfabric-cluster']['role'] != 'MASTER'):
                self.module.exit_json(skipped=True, msg="Node is not SFS master. Device info: %s" % device_info)
        except ConnectionError as exc:
            self.module.exit_json(skipped=True, msg="Connection Error. Could not determine SFS Role. Device info:%s Exception:%s" % (device_info, str(exc)))
        except Exception as exc:
            self.module.exit_json(skipped=True, msg="Could not determine SFS Role. Device info:%s Exception:%s" % (device_info, str(exc)))

    def get_fullpath_config(self, fullpath):
        ''' Get config for the given full path '''
        return restconf.get(self.module, fullpath)

    def get_path_config(self, path):
        '''
        Get config of a given path relative to base path.
        Does a GET query and returns the result
        '''
        return restconf.get(self.module, self.base_path + path)

    def get_config(self):
        '''
        Get the config for this particular resource with Id/Key
        '''
        try:
            if self.is_get_running is True:
                return restconf.get(self.module, self.resource_fullpath)
        except ConnectionError as exc:
            if exc.code >= 400:
                return None
            else:
                self.module.fail_json(msg=to_text(exc), code=exc.code)

    def running_to_payload(self, data):
        '''
        Convert running config of this resource (result of GET) to match
        the format expected by PUT/POST/PATCH
        Subclasses can override this to make any such conversion
        '''
        return data

    def candidate_to_payload(self, data):
        '''
        Converts module args to payload.
        Use payload_arg_map to form the payload from module args
        Can be overridden by subclass for any exceptions
        '''
        if self.payload_arg_map:
            if not data:
                return data
            payload = dict()
            for (f1, f2) in self.payload_arg_map.items():
                if f2 in data and data[f2] != None:     # nopep8
                    payload[f1] = data[f2]
            return payload
        else:
            return data

    def get_diff_payload(self, running, candidate):
        '''
        Find the diff between the payload formats of
        running and candidate
        '''
        return dict_diff(running, candidate)

    def update_diff_payload(self, candidate, diff):
        '''
        Return the final payload to be sent based on the diff payload
        Make any additions/deletions to payload here
        Default implementation returns the candidate
        '''
        return candidate if diff else None

    def update_config(self, data):
        '''
        Update the config for this resource as per the module args values
        in data.
        Does a GET query and creates or updates the resource based on the result
        Update is done only if there is any diff found
        '''
        result = dict(changed=False)
        running = self.running_to_payload(self.get_config())
        method = self.update_method
        path = self.resource_fullpath
        if not running:
            # Create resource
            running = dict()
            if self.patch_support is True:
                method = self.patch_method
            else:
                method = self.create_method if self.post_support is True else self.update_method
            path = self.fullpath
        result['running'] = running
        result['input'] = data
        if self.keep_input_payload is True:
            diff = data
            diff_payload = data
        else:
            candidate = self.candidate_to_payload(data)
            result['candidate'] = candidate
            if self.pass_input_payload is True:
                diff = candidate
            else:
                diff = self.get_diff_payload(running, candidate)
            diff_payload = self.update_diff_payload(candidate, diff)
        if diff:
            result['updates'] = diff
            if self.redfish_support is False:
                diff_payload = {self.path: diff_payload}
            self.edit_config(path=path, content=diff_payload, method=method, result=result)
        return result

    def delete_config(self, data=None):
        '''
        Delete the resource with it is present
        '''
        result = dict(changed=False)
        running = self.get_config()
        if not running:
            return result
        candidate = self.candidate_to_payload(data)
        result['candidate'] = candidate
        result['input'] = data
        self.edit_config(path=self.resource_fullpath, content=candidate, method=self.delete_method, result=result)
        return result

    def edit_config(self, path, content, method, result):
        ''' Wrapper on top of restconf.edit_config to handle and update result '''
        if path is None:
            raise ValueError("path value must be provided")
        try:
            connection = Connection(self.module._socket_path)
            if self.headers is None:
                result['response'] = connection.send_request(content, path=path, method=method, content_type=self.content_type)
            else:
                result['response'] = connection.send_request_with_header(content, path=path, headers=content, method=method, content_type=self.content_type)
            result['changed'] = False if 'ietf-restconf:errors' in result['response'] else True
        except ConnectionError as exc:
            self.module.fail_json(msg=str(exc), exception=traceback.format_exc(), details=dict(path=path, method=method, payload=content, **result))

    def get_module_config(self, data=None):
        '''
        GET the resource with it is present
        '''
        result = dict(changed=False)
        running = self.get_config()
        if not running:
            return result
        result['response'] = running
        return result

    def execute_module(self):
        ''' Execute the module as per the module args '''
        state = self.module.params['state']
        if self.redfish_support is False:
            self.base_path = SFS_BASE_RESTCONF_PATH

        if self.is_method_get_only is True:
            result = self.get_module_config()
        elif state == 'absent':
            result = self.delete_config()
        else:
            result = self.update_config(self.module.params)
        self.module.exit_json(**result)


def get_odata_id(data):
    ''' Return the @odata.id parameter of the SFS resource in data '''
    return data.get('@odata.id')


def extract_id_value(data):
    ''' Extract the resource id value of the SFS resource in data '''
    odata_id = get_odata_id(data)
    pattern = "\('(.+?)'\)"  # nopep8
    all_ids = re.findall(pattern, odata_id)
    if not all_ids:
        return None
    return all_ids[-1]
