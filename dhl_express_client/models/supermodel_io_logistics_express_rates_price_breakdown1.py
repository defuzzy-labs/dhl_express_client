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

class SupermodelIoLogisticsExpressRatesPriceBreakdown1(object):
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
        'price_type': 'str',
        'type_code': 'str',
        'price': 'float',
        'rate': 'float',
        'base_price': 'float'
    }

    attribute_map = {
        'price_type': 'priceType',
        'type_code': 'typeCode',
        'price': 'price',
        'rate': 'rate',
        'base_price': 'basePrice'
    }

    def __init__(self, price_type=None, type_code=None, price=None, rate=None, base_price=None):  # noqa: E501
        """SupermodelIoLogisticsExpressRatesPriceBreakdown1 - a model defined in Swagger"""  # noqa: E501
        self._price_type = None
        self._type_code = None
        self._price = None
        self._rate = None
        self._base_price = None
        self.discriminator = None
        if price_type is not None:
            self.price_type = price_type
        if type_code is not None:
            self.type_code = type_code
        if price is not None:
            self.price = price
        if rate is not None:
            self.rate = rate
        if base_price is not None:
            self.base_price = base_price

    @property
    def price_type(self):
        """Gets the price_type of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501

        If a breakdown is provided, details can either be; 'TAX',<BR>                              'DISCOUNT'  # noqa: E501

        :return: The price_type of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.

        If a breakdown is provided, details can either be; 'TAX',<BR>                              'DISCOUNT'  # noqa: E501

        :param price_type: The price_type of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :type: str
        """

        self._price_type = price_type

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501

        Discount or tax type codes as provided by DHL Express. Example values:<BR>                              For discount;<BR>                              P: promotional<BR>                              S: special  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.

        Discount or tax type codes as provided by DHL Express. Example values:<BR>                              For discount;<BR>                              P: promotional<BR>                              S: special  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :type: str
        """

        self._type_code = type_code

    @property
    def price(self):
        """Gets the price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501

        The actual amount of the discount/tax  # noqa: E501

        :return: The price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.

        The actual amount of the discount/tax  # noqa: E501

        :param price: The price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def rate(self):
        """Gets the rate of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501

        Percentage of the discount/tax  # noqa: E501

        :return: The rate of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.

        Percentage of the discount/tax  # noqa: E501

        :param rate: The rate of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def base_price(self):
        """Gets the base_price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501

        The base amount of the service charge  # noqa: E501

        :return: The base_price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """Sets the base_price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.

        The base amount of the service charge  # noqa: E501

        :param base_price: The base_price of this SupermodelIoLogisticsExpressRatesPriceBreakdown1.  # noqa: E501
        :type: float
        """

        self._base_price = base_price

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
        if issubclass(SupermodelIoLogisticsExpressRatesPriceBreakdown1, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressRatesPriceBreakdown1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
