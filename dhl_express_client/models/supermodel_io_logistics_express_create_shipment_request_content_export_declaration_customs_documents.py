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

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments(object):
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
        'value': 'str'
    }

    attribute_map = {
        'type_code': 'typeCode',
        'value': 'value'
    }

    def __init__(self, type_code=None, value=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments - a model defined in Swagger"""  # noqa: E501
        self._type_code = None
        self._value = None
        self.discriminator = None
        self.type_code = type_code
        self.value = value

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501

        Please provide the line item customs document type code  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.

        Please provide the line item customs document type code  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501
        allowed_values = ["972", "AHC", "ALC", "ATA", "ATR", "BEX", "CHA", "CHD", "CHP", "CIT", "CIV", "CI2", "COO", "CPA", "CRL", "CSD", "DEX", "DGD", "DLI", "DOV", "ELP", "EU1", "EU2", "EUS", "EXL", "FMA", "HLC", "HWB", "INV", "IPA", "JLC", "LIC", "LNP", "NID", "PAS", "PFI", "PHY", "PLI", "POA", "PPY", "ROD", "T2M", "TAD", "TCS", "VET", "VEX"]  # noqa: E501
        if type_code not in allowed_values:
            raise ValueError(
                "Invalid value for `type_code` ({0}), must be one of {1}"  # noqa: E501
                .format(type_code, allowed_values)
            )

        self._type_code = type_code

    @property
    def value(self):
        """Gets the value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501

        Please provide the line item customs document ID  # noqa: E501

        :return: The value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.

        Please provide the line item customs document ID  # noqa: E501

        :param value: The value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
