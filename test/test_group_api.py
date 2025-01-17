"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.group_api import GroupApi  # noqa: E501


class TestGroupApi(unittest.TestCase):
    """GroupApi unit test stubs"""

    def setUp(self):
        self.api = GroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_group(self):
        """Test case for add_group

        Create a new group  # noqa: E501
        """
        pass

    def test_get_group(self):
        """Test case for get_group

        Get a group  # noqa: E501
        """
        pass

    def test_get_group_list(self):
        """Test case for get_group_list

        Get a list of groups  # noqa: E501
        """
        pass

    def test_update_group(self):
        """Test case for update_group

        Update a group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
