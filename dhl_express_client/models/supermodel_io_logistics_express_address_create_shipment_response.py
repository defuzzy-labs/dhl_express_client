# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services    In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments)   # noqa: E501

    OpenAPI spec version: 2.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SupermodelIoLogisticsExpressAddressCreateShipmentResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'postal_code': 'str',
        'city_name': 'str',
        'country_code': 'str',
        'province_code': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'city_district_name': 'str',
        'province_name': 'str',
        'country_name': 'str'
    }

    attribute_map = {
        'postal_code': 'postalCode',
        'city_name': 'cityName',
        'country_code': 'countryCode',
        'province_code': 'provinceCode',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_line3': 'addressLine3',
        'city_district_name': 'cityDistrictName',
        'province_name': 'provinceName',
        'country_name': 'countryName'
    }

    def __init__(self, postal_code=None, city_name=None, country_code=None, province_code=None, address_line1=None, address_line2=None, address_line3=None, city_district_name=None, province_name=None, country_name=None):  # noqa: E501
        """SupermodelIoLogisticsExpressAddressCreateShipmentResponse - a model defined in Swagger"""  # noqa: E501
        self._postal_code = None
        self._city_name = None
        self._country_code = None
        self._province_code = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._city_district_name = None
        self._province_name = None
        self._country_name = None
        self.discriminator = None
        self.postal_code = postal_code
        self.city_name = city_name
        self.country_code = country_code
        if province_code is not None:
            self.province_code = province_code
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if city_district_name is not None:
            self.city_district_name = city_district_name
        if province_name is not None:
            self.province_name = province_name
        if country_name is not None:
            self.country_name = country_name

    @property
    def postal_code(self):
        """Gets the postal_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Postal code  # noqa: E501

        :return: The postal_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Postal code  # noqa: E501

        :param postal_code: The postal_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def city_name(self):
        """Gets the city_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        City name  # noqa: E501

        :return: The city_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """Sets the city_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        City name  # noqa: E501

        :param city_name: The city_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if city_name is None:
            raise ValueError("Invalid value for `city_name`, must not be `None`")  # noqa: E501

        self._city_name = city_name

    @property
    def country_code(self):
        """Gets the country_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Country code  # noqa: E501

        :return: The country_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Country code  # noqa: E501

        :param country_code: The country_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501

        self._country_code = country_code

    @property
    def province_code(self):
        """Gets the province_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Province or state code  # noqa: E501

        :return: The province_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._province_code

    @province_code.setter
    def province_code(self, province_code):
        """Sets the province_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Province or state code  # noqa: E501

        :param province_code: The province_code of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._province_code = province_code

    @property
    def address_line1(self):
        """Gets the address_line1 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Address line 1  # noqa: E501

        :return: The address_line1 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Address line 1  # noqa: E501

        :param address_line1: The address_line1 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Address line 2  # noqa: E501

        :return: The address_line2 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Address line 2  # noqa: E501

        :param address_line2: The address_line2 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Address line 3  # noqa: E501

        :return: The address_line3 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Address line 3  # noqa: E501

        :param address_line3: The address_line3 of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._address_line3 = address_line3

    @property
    def city_district_name(self):
        """Gets the city_district_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Suburb or county name  # noqa: E501

        :return: The city_district_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._city_district_name

    @city_district_name.setter
    def city_district_name(self, city_district_name):
        """Sets the city_district_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Suburb or county name  # noqa: E501

        :param city_district_name: The city_district_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._city_district_name = city_district_name

    @property
    def province_name(self):
        """Gets the province_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Please enter your state or province name  # noqa: E501

        :return: The province_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._province_name

    @province_name.setter
    def province_name(self, province_name):
        """Sets the province_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Please enter your state or province name  # noqa: E501

        :param province_name: The province_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._province_name = province_name

    @property
    def country_name(self):
        """Gets the country_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501

        Please enter your country name  # noqa: E501

        :return: The country_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_name

    @country_name.setter
    def country_name(self, country_name):
        """Sets the country_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.

        Please enter your country name  # noqa: E501

        :param country_name: The country_name of this SupermodelIoLogisticsExpressAddressCreateShipmentResponse.  # noqa: E501
        :type: str
        """

        self._country_name = country_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SupermodelIoLogisticsExpressAddressCreateShipmentResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupermodelIoLogisticsExpressAddressCreateShipmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
