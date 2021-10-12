"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.run_api import RunApi  # noqa: E501


class TestRunApi(unittest.TestCase):
    """RunApi unit test stubs"""

    def setUp(self):
        self.api = RunApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_run(self):
        """Test case for add_run

        Create a run  # noqa: E501
        """
        pass

    def test_bulk_update(self):
        """Test case for bulk_update

        Update multiple runs with common metadata  # noqa: E501
        """
        pass

    def test_get_run(self):
        """Test case for get_run

        Get a single run by ID (uuid required)  # noqa: E501
        """
        pass

    def test_get_run_list(self):
        """Test case for get_run_list

        Get a list of the test runs  # noqa: E501
        """
        pass

    def test_update_run(self):
        """Test case for update_run

        Update a single run  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
