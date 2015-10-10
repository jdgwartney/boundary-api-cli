#!/usr/bin/env python
#
# Copyright 2014-2015 Boundary, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import os.path


class CLITestParameters:

    def __init__(self, filename='cli_test_parameters.json'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.parameters = None
        pass

    def load(self):
        with open(self.filename, "r") as f:
            self.parameters = json.load(f)

    def get(self, name):
        if self.parameters is None:
            self.load()
        return self.parameters[name]

    def get_description(self, name):
        return self.get(name)['description']
