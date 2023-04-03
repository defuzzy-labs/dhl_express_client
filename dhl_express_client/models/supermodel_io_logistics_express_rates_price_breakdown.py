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

class SupermodelIoLogisticsExpressRatesPriceBreakdown(object):
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
        'type_code': 'str',
        'price': 'float'
    }

    attribute_map = {
        'type_code': 'typeCode',
        'price': 'price'
    }

    def __init__(self, type_code=None, price=None):  # noqa: E501
        """SupermodelIoLogisticsExpressRatesPriceBreakdown - a model defined in Swagger"""  # noqa: E501
        self._type_code = None
        self._price = None
        self.discriminator = None
        self.type_code = type_code
        self.price = price

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501

        Expected values in Breakdown/Type are below:<BR>                        STTXA:  Total tax for the shipment<BR>                        STDIS: Total discount for the shipment<BR>                        SPRQT: Net shipment / weight charge  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown.

        Expected values in Breakdown/Type are below:<BR>                        STTXA:  Total tax for the shipment<BR>                        STDIS: Total discount for the shipment<BR>                        SPRQT: Net shipment / weight charge  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501

        self._type_code = type_code

    @property
    def price(self):
        """Gets the price of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501

        The amount price of DHL product and services  # noqa: E501

        :return: The price of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SupermodelIoLogisticsExpressRatesPriceBreakdown.

        The amount price of DHL product and services  # noqa: E501

        :param price: The price of this SupermodelIoLogisticsExpressRatesPriceBreakdown.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

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
        if issubclass(SupermodelIoLogisticsExpressRatesPriceBreakdown, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressRatesPriceBreakdown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other