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


class AirflowMonitoringTest(base.BaseShipyardTest):
    def _get_workflows_id(self):
        resp = self.shipyard_airflow_monitoring_client.list_workflows()
        self.assertTrue(len(resp[0]) > 0,
                        'No configdocs available, nothing to test')
        return resp[0]['workflow_id']

    @decorators.idempotent_id('5a41bb54-c010-4d09-9d68-eece565e66f3')
    def test_get_workflows_list(self):
        """List of workflows, Successful with response status 200"""
        response = self.shipyard_airflow_monitoring_client.list_workflows()
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('7e4fb56b-6637-48bf-808d-c166ee5f804f')
    def test_get_workflow(self):
        """A particular workflow detail, Successful with response status 200"""
        workflow_id = self._get_workflows_id()
        response = self.shipyard_airflow_monitoring_client. \
            get_workflow(workflow_id)
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['workflow_id'], workflow_id)
