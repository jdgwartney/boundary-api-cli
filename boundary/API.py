#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from boundary import AlarmCreate


class API:

    def __init__(self, api_host="premimum-api.boundary.com", email=None, api_token=None):
        self._api_host = api_host
        self._email = email
        self._api_token = api_token

    def alarm_create(self, **kwargs):
        api = AlarmCreate()
        api._kwargs = kwargs
        return api.api_call()

    def alarm_delete(self, **kwargs):
        pass

    def alarm_list(self, **kwargs):
        pass

    def alarm_update(self, **kwargs):
        pass
