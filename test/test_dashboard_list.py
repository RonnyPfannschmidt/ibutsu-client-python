"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ibutsu_client
from ibutsu_client.model.dashboard import Dashboard
from ibutsu_client.model.pagination import Pagination
globals()['Dashboard'] = Dashboard
globals()['Pagination'] = Pagination
from ibutsu_client.model.dashboard_list import DashboardList


class TestDashboardList(unittest.TestCase):
    """DashboardList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDashboardList(self):
        """Test DashboardList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DashboardList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
