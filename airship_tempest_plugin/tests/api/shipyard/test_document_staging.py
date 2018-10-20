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

import logging
from airship_tempest_plugin.tests.api.shipyard import base
from tempest.lib import decorators
from tempest.lib import exceptions

logger = logging.getLogger()


class DocumentStagingTest(base.BaseShipyardTest):
    def _get_collection_id(self):
        resp = self.shipyard_document_staging_client.get_configdocs_status()
        self.assertTrue(len(resp[0]) > 0,
                        'No configdocs available, nothing to test')
        return resp[0]['collection_name']

    @decorators.idempotent_id('db351ee5-a608-4492-b705-6e6c654a60e7')
    def test_get_collection_list(self):
        """Config docs status, Successful with response status 200"""
        response = self.shipyard_document_staging_client. \
            get_configdocs_status()
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('743ab304-be35-4e45-ad47-e124dce3b9dc')
    def test_get_collection(self):
        """Get Config docs for a particular collection, Successful with
           response status 200.
           In case document does not found, return 404 Not Found
        """
        collection_id = self._get_collection_id()
        try:
            response = self.shipyard_document_staging_client. \
                get_configdocs(collection_id)
            self.assertEqual(response.response['status'], '200')
        except exceptions.NotFound:
            logger.info("The Shipyard buffer does not contain this collection")
            pass

    @decorators.idempotent_id('bd138747-582e-4c2e-9f26-09c3fccad96f')
    def test_get_collection_version_buffer(self):
        """Get Config docs of buffer version,
           Successful with response status 200
           In case document does not found, return 404 Not Found
        """
        collection_id = self._get_collection_id()
        try:
            response = self.shipyard_document_staging_client. \
                get_configdocs_version(collection_id, "buffer")
            self.assertEqual(response.response['status'], '200')
        except exceptions.NotFound:
            logger.info("The Shipyard buffer does not contain this collection")
            pass

    @decorators.idempotent_id('d42c691a-07a2-41cc-91a6-9d02be8f2649')
    def test_get_collection_version_committed(self):
        """Get Config docs of committed version,
           Successful with response status 200
        """
        collection_id = self._get_collection_id()
        response = self.shipyard_document_staging_client. \
            get_configdocs_version(collection_id, "committed")
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('2940492a-47b0-4218-859a-b9cb556f480b')
    def test_get_collection_version_successful_site_action(self):
        """Get Config docs of successful_site_action version,
        Successful with response status 200
        """
        collection_id = self._get_collection_id()
        response = self.shipyard_document_staging_client. \
            get_configdocs_version(collection_id, "successful_site_action")
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('f6b86b85-5797-4664-95a9-0b6d242b50b7')
    def test_get_collection_version_last_site_action(self):
        """Get Config docs of last_site_action,
           Successful with response status 200
        """
        collection_id = self._get_collection_id()
        response = self.shipyard_document_staging_client. \
            get_configdocs_version(collection_id, "last_site_action")
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('2db31479-8d1f-4d95-a3a0-31b1bf726f39')
    def test_get_renderedconfigdocs(self):
        """Get RenderedConfig docs, Successful with response status 200
           In case document does not found, return 404 Not Found
        """
        try:
            response = self.shipyard_document_staging_client. \
                get_renderedconfigdocs()
            self.assertEqual(response.response['status'], '200')
        except exceptions.NotFound:
            logger.info("buffer version does not exist")
            pass

    @decorators.idempotent_id('ffd9d1d9-9846-4493-9f9e-e35f12ce56da')
    def test_get_renderedconfigdocs_version_buffer(self):
        """Get RenderedConfig docs of buffer version,
           Successful with response status 200
           In case document does not found, return 404 Not Found
        """
        try:
            response = self.shipyard_document_staging_client. \
                get_renderedconfigdocs_version("buffer")
            self.assertEqual(response.response['status'], '200')
        except exceptions.NotFound:
            logger.info("buffer version does not exist")
            pass

    @decorators.idempotent_id('353e9955-7f12-4561-a3c2-c9819f259775')
    def test_get_renderedconfigdocs_version_committed(self):
        """Get RenderedConfig docs of committed version,
           Successful with response status 200
        """
        response = self.shipyard_document_staging_client. \
            get_renderedconfigdocs_version("committed")
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('3daac942-baec-4078-a632-71b66dca1e91')
    def test_get_renderedconfigdocs_version_successful_site_action(self):
        """Get RenderedConfig docs of successful_site_action version,
           Successful with response status 200
           In case document does not found, return 404 Not Found
        """
        try:
            response = self.shipyard_document_staging_client. \
                get_renderedconfigdocs_version("successful_site_action")
            self.assertEqual(response.response['status'], '200')
        except exceptions.NotFound:
            logger.info("This revision does not exist")
            pass

    @decorators.idempotent_id('9af56232-eacf-4baa-85e9-cbb93772974d')
    def test_get_renderedconfigdocs_version_last_site_action(self):
        """Get RenderedConfig docs of last_site_action,
           Successful with response status 200
        """
        response = self.shipyard_document_staging_client. \
            get_renderedconfigdocs_version("last_site_action")
        self.assertEqual(response.response['status'], '200')

    @decorators.idempotent_id('1aedf793-dde4-49df-a6d2-109bc11b6db5')
    def test_get_collection_compare_two_revisions_doc(self):
        """Get Config docs of two versions and compare in between,
           Successful with response status 200
        """
        response = self.shipyard_document_staging_client. \
            get_configdocs_compare_two("committed%2Cbuffer")
        self.assertEqual(response.response['status'], '200')
        self.assertEqual(response['new_version'], 'buffer')
        self.assertEqual(response['base_version'], 'committed')
