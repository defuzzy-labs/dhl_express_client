# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services   In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments)   # noqa: E501

    OpenAPI spec version: 2.12.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SupermodelIoLogisticsExpressContactCreateShipmentResponse(object):
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
        'company_name': 'str',
        'full_name': 'str'
    }

    attribute_map = {
        'company_name': 'companyName',
        'full_name': 'fullName'
    }

    def __init__(self, company_name=None, full_name=None):  # noqa: E501
        """SupermodelIoLogisticsExpressContactCreateShipmentResponse - a model defined in Swagger"""  # noqa: E501
        self._company_name = None
        self._full_name = None
        self.discriminator = None
        self.company_name = company_name
        self.full_name = full_name

    @property
    def company_name(self):
        """Gets the company_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501

        Company name  # noqa: E501

        :return: The company_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.

        Company name  # noqa: E501

        :param company_name: The company_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def full_name(self):
        """Gets the full_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501

        Full name  # noqa: E501

        :return: The full_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.

        Full name  # noqa: E501

        :param full_name: The full_name of this SupermodelIoLogisticsExpressContactCreateShipmentResponse.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

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
        if issubclass(SupermodelIoLogisticsExpressContactCreateShipmentResponse, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressContactCreateShipmentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
