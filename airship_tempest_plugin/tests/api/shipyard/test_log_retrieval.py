# Copyright 2018 AT&T Corp
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from airship_tempest_plugin.tests.api.shipyard import base
from tempest.lib import decorators


class LogRetrievalTest(base.BaseShipyardTest):

    def _get_action_step_id(self):
        resp = self.shipyard_actions_client.list_actions()
        self.assertTrue(len(resp[1]) > 0,
                        'No actions available, nothing to test')
        return resp[1]['id'], resp[1]['steps'][0]['id']

    @decorators.idempotent_id('1a8e95fd-77cc-4576-99e1-4ebbb4d8469a')
    def test_get_action_step_logs(self):
        """Get actions step log, Successful with response status 200"""
        action_id, step_id = self._get_action_step_id()
        response = self.shipyard_log_retrieval_client.\
            get_action_step_logs(action_id, step_id)
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response[1]['task_id'], step_id)
