"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ibutsu_client
from ibutsu_client.model.group import Group
from ibutsu_client.model.pagination import Pagination
globals()['Group'] = Group
globals()['Pagination'] = Pagination
from ibutsu_client.model.group_list import GroupList


class TestGroupList(unittest.TestCase):
    """GroupList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupList(self):
        """Test GroupList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GroupList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
