# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments)   # noqa: E501

    OpenAPI spec version: 2.12.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.address_api import AddressApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAddressApi(unittest.TestCase):
    """AddressApi unit test stubs"""

    def setUp(self):
        self.api = AddressApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_exp_api_address_validate(self):
        """Test case for exp_api_address_validate

        Validate DHL Express pickup/delivery capabilities at origin/destination  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
