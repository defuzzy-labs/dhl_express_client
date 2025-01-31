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

class SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges(object):
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
        'currency_type': 'str',
        'price_currency': 'str',
        'price': 'float',
        'service_breakdown': 'list[SupermodelIoLogisticsExpressCreateShipmentResponseServiceBreakdown]'
    }

    attribute_map = {
        'currency_type': 'currencyType',
        'price_currency': 'priceCurrency',
        'price': 'price',
        'service_breakdown': 'serviceBreakdown'
    }

    def __init__(self, currency_type=None, price_currency=None, price=None, service_breakdown=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges - a model defined in Swagger"""  # noqa: E501
        self._currency_type = None
        self._price_currency = None
        self._price = None
        self._service_breakdown = None
        self.discriminator = None
        self.currency_type = currency_type
        self.price_currency = price_currency
        self.price = price
        if service_breakdown is not None:
            self.service_breakdown = service_breakdown

    @property
    def currency_type(self):
        """Gets the currency_type of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501

        Possible Values :<BR>            - 'BILLC', billing currency<BR>            - 'PULCL', country public rates currency<BR>            - 'BASEC', base currency  # noqa: E501

        :return: The currency_type of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :rtype: str
        """
        return self._currency_type

    @currency_type.setter
    def currency_type(self, currency_type):
        """Sets the currency_type of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.

        Possible Values :<BR>            - 'BILLC', billing currency<BR>            - 'PULCL', country public rates currency<BR>            - 'BASEC', base currency  # noqa: E501

        :param currency_type: The currency_type of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :type: str
        """
        if currency_type is None:
            raise ValueError("Invalid value for `currency_type`, must not be `None`")  # noqa: E501

        self._currency_type = currency_type

    @property
    def price_currency(self):
        """Gets the price_currency of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501

        This the currency of the rated shipment for the prices listed.  # noqa: E501

        :return: The price_currency of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :rtype: str
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, price_currency):
        """Sets the price_currency of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.

        This the currency of the rated shipment for the prices listed.  # noqa: E501

        :param price_currency: The price_currency of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :type: str
        """
        if price_currency is None:
            raise ValueError("Invalid value for `price_currency`, must not be `None`")  # noqa: E501

        self._price_currency = price_currency

    @property
    def price(self):
        """Gets the price of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501

        The amount price of DHL product and services  # noqa: E501

        :return: The price of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.

        The amount price of DHL product and services  # noqa: E501

        :param price: The price of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def service_breakdown(self):
        """Gets the service_breakdown of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501


        :return: The service_breakdown of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentResponseServiceBreakdown]
        """
        return self._service_breakdown

    @service_breakdown.setter
    def service_breakdown(self, service_breakdown):
        """Sets the service_breakdown of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.


        :param service_breakdown: The service_breakdown of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentResponseServiceBreakdown]
        """

        self._service_breakdown = service_breakdown

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
