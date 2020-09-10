# coding: utf-8

"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.10.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ibutsu_client
from ibutsu_client.models.model_import import ModelImport  # noqa: E501
from ibutsu_client.rest import ApiException

class TestModelImport(unittest.TestCase):
    """ModelImport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelImport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ibutsu_client.models.model_import.ModelImport()  # noqa: E501
        if include_optional :
            return ModelImport(
                id = '8ebba624448f749dfc5f', 
                status = 'done', 
                filename = 'test-run.xml', 
                format = 'JUnit', 
                run_id = '97dd93951b96f9bada68'
            )
        else :
            return ModelImport(
        )

    def testModelImport(self):
        """Test ModelImport"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
