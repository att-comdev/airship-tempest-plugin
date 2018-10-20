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


class SiteStatusesTest(base.BaseShipyardTest):
    @decorators.idempotent_id('c4c6fd0f-83dd-42ae-a4eb-430708490b71')
    def test_get_site_statuses(self):
        """Get Site status, Successful with response status 200"""
        response = self.shipyard_site_statuses_client.get_site_statuses()
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['nodes_provision_status'][0]['status'], 'Deployed')
        self.assertEqual(response['machines_powerstate'][0]['power_state'], 'on')

    @decorators.idempotent_id('9cfbf0b9-e826-4a9d-b1d2-055adaa8ecc2')
    def test_get_site_statuses_node_provision_status(self):
        """Get Site status of Node Provision and
           Successful with response status 200
        """
        response = self.shipyard_site_statuses_client. \
            get_site_statuses_arg('nodes-provision-status')
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['nodes_provision_status'][0]['status'], 'Deployed')

    @decorators.idempotent_id('c329dbe8-4cb2-4a8b-9aa8-3a032c73102b')
    def test_get_site_statuses_node_power_status(self):
        """Get Site status of Node Power and
           Successful with response status 200
        """
        response = self.shipyard_site_statuses_client. \
            get_site_statuses_arg('machines-power-state')
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['machines_powerstate'][0]['power_state'], 'on')

    @decorators.idempotent_id('52a87dde-1458-45fd-92c6-edcd93eb0c14')
    def test_get_site_statuses_both_filters_together(self):
        """Get Site status of both filters together and
           Successful with response status 200
        """
        response = self.shipyard_site_statuses_client. \
            get_site_statuses_arg('nodes-provision-status%2Cmachines-power-state')
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['nodes_provision_status'][0]['status'], 'Deployed')
        self.assertEqual(response['machines_powerstate'][0]['power_state'], 'on')
