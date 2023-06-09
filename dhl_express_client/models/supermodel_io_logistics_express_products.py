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

class SupermodelIoLogisticsExpressProducts(object):
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
        'products': 'list[SupermodelIoLogisticsExpressProductsProducts]',
        'warnings': 'list[str]'
    }

    attribute_map = {
        'products': 'products',
        'warnings': 'warnings'
    }

    def __init__(self, products=None, warnings=None):  # noqa: E501
        """SupermodelIoLogisticsExpressProducts - a model defined in Swagger"""  # noqa: E501
        self._products = None
        self._warnings = None
        self.discriminator = None
        self.products = products
        if warnings is not None:
            self.warnings = warnings

    @property
    def products(self):
        """Gets the products of this SupermodelIoLogisticsExpressProducts.  # noqa: E501


        :return: The products of this SupermodelIoLogisticsExpressProducts.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsProducts]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this SupermodelIoLogisticsExpressProducts.


        :param products: The products of this SupermodelIoLogisticsExpressProducts.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsProducts]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def warnings(self):
        """Gets the warnings of this SupermodelIoLogisticsExpressProducts.  # noqa: E501


        :return: The warnings of this SupermodelIoLogisticsExpressProducts.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this SupermodelIoLogisticsExpressProducts.


        :param warnings: The warnings of this SupermodelIoLogisticsExpressProducts.  # noqa: E501
        :type: list[str]
        """

        self._warnings = warnings

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
        if issubclass(SupermodelIoLogisticsExpressProducts, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
