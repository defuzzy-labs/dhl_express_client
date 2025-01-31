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

class SupermodelIoLogisticsExpressRatesExchangeRates(object):
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
        'current_exchange_rate': 'float',
        'currency': 'str',
        'base_currency': 'str'
    }

    attribute_map = {
        'current_exchange_rate': 'currentExchangeRate',
        'currency': 'currency',
        'base_currency': 'baseCurrency'
    }

    def __init__(self, current_exchange_rate=None, currency=None, base_currency=None):  # noqa: E501
        """SupermodelIoLogisticsExpressRatesExchangeRates - a model defined in Swagger"""  # noqa: E501
        self._current_exchange_rate = None
        self._currency = None
        self._base_currency = None
        self.discriminator = None
        self.current_exchange_rate = current_exchange_rate
        self.currency = currency
        self.base_currency = base_currency

    @property
    def current_exchange_rate(self):
        """Gets the current_exchange_rate of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501

        Rate of the currency exchange  # noqa: E501

        :return: The current_exchange_rate of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :rtype: float
        """
        return self._current_exchange_rate

    @current_exchange_rate.setter
    def current_exchange_rate(self, current_exchange_rate):
        """Sets the current_exchange_rate of this SupermodelIoLogisticsExpressRatesExchangeRates.

        Rate of the currency exchange  # noqa: E501

        :param current_exchange_rate: The current_exchange_rate of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :type: float
        """
        if current_exchange_rate is None:
            raise ValueError("Invalid value for `current_exchange_rate`, must not be `None`")  # noqa: E501

        self._current_exchange_rate = current_exchange_rate

    @property
    def currency(self):
        """Gets the currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501

        The currency code  # noqa: E501

        :return: The currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SupermodelIoLogisticsExpressRatesExchangeRates.

        The currency code  # noqa: E501

        :param currency: The currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def base_currency(self):
        """Gets the base_currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501

        The currency code of the base currency is either USD or EUR  # noqa: E501

        :return: The base_currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this SupermodelIoLogisticsExpressRatesExchangeRates.

        The currency code of the base currency is either USD or EUR  # noqa: E501

        :param base_currency: The base_currency of this SupermodelIoLogisticsExpressRatesExchangeRates.  # noqa: E501
        :type: str
        """
        if base_currency is None:
            raise ValueError("Invalid value for `base_currency`, must not be `None`")  # noqa: E501

        self._base_currency = base_currency

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
        if issubclass(SupermodelIoLogisticsExpressRatesExchangeRates, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressRatesExchangeRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
