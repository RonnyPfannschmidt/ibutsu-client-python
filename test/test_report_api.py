"""
    Ibutsu API

    A system to store and query test results  # noqa: E501

    The version of the OpenAPI document: 1.13.4
    Generated by: https://openapi-generator.tech
"""


import unittest

import ibutsu_client
from ibutsu_client.api.report_api import ReportApi  # noqa: E501


class TestReportApi(unittest.TestCase):
    """ReportApi unit test stubs"""

    def setUp(self):
        self.api = ReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_report(self):
        """Test case for add_report

        Create a new report  # noqa: E501
        """
        pass

    def test_delete_report(self):
        """Test case for delete_report

        Delete a report  # noqa: E501
        """
        pass

    def test_download_report(self):
        """Test case for download_report

        Download a report  # noqa: E501
        """
        pass

    def test_get_report(self):
        """Test case for get_report

        Get a report  # noqa: E501
        """
        pass

    def test_get_report_list(self):
        """Test case for get_report_list

        Get a list of reports  # noqa: E501
        """
        pass

    def test_get_report_types(self):
        """Test case for get_report_types

        Get a list of report types  # noqa: E501
        """
        pass

    def test_view_report(self):
        """Test case for view_report

        View a report  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
