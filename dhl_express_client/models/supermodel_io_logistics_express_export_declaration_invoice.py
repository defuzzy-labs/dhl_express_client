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

class SupermodelIoLogisticsExpressExportDeclarationInvoice(object):
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
        'number': 'str',
        '_date': 'str',
        'function': 'str',
        'customer_references': 'list[SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferences]',
        'indicative_customs_values': 'SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues'
    }

    attribute_map = {
        'number': 'number',
        '_date': 'date',
        'function': 'function',
        'customer_references': 'customerReferences',
        'indicative_customs_values': 'indicativeCustomsValues'
    }

    def __init__(self, number=None, _date=None, function=None, customer_references=None, indicative_customs_values=None):  # noqa: E501
        """SupermodelIoLogisticsExpressExportDeclarationInvoice - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self.__date = None
        self._function = None
        self._customer_references = None
        self._indicative_customs_values = None
        self.discriminator = None
        self.number = number
        self._date = _date
        self.function = function
        if customer_references is not None:
            self.customer_references = customer_references
        if indicative_customs_values is not None:
            self.indicative_customs_values = indicative_customs_values

    @property
    def number(self):
        """Gets the number of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501

        Please enter commercial invoice number  # noqa: E501

        :return: The number of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SupermodelIoLogisticsExpressExportDeclarationInvoice.

        Please enter commercial invoice number  # noqa: E501

        :param number: The number of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def _date(self):
        """Gets the _date of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501

        Please enter commercial invoice date  # noqa: E501

        :return: The _date of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this SupermodelIoLogisticsExpressExportDeclarationInvoice.

        Please enter commercial invoice date  # noqa: E501

        :param _date: The _date of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def function(self):
        """Gets the function of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501

        Please provide the purpose was the document details captured and are planned to be used. Note: export and import is only applicable for approve Sale In Transit customers  # noqa: E501

        :return: The function of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this SupermodelIoLogisticsExpressExportDeclarationInvoice.

        Please provide the purpose was the document details captured and are planned to be used. Note: export and import is only applicable for approve Sale In Transit customers  # noqa: E501

        :param function: The function of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :type: str
        """
        if function is None:
            raise ValueError("Invalid value for `function`, must not be `None`")  # noqa: E501
        allowed_values = ["import", "export", "both"]  # noqa: E501
        if function not in allowed_values:
            raise ValueError(
                "Invalid value for `function` ({0}), must be one of {1}"  # noqa: E501
                .format(function, allowed_values)
            )

        self._function = function

    @property
    def customer_references(self):
        """Gets the customer_references of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501

        Please provide the customer references at invoice level.   Note: customerReference/0/value with typeCode 'CU' is mandatory if using POST method and no shipmentTrackingNumber is provided in request. It is recommended to provide less than 20 customer references of 'MRN' type code  # noqa: E501

        :return: The customer_references of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferences]
        """
        return self._customer_references

    @customer_references.setter
    def customer_references(self, customer_references):
        """Sets the customer_references of this SupermodelIoLogisticsExpressExportDeclarationInvoice.

        Please provide the customer references at invoice level.   Note: customerReference/0/value with typeCode 'CU' is mandatory if using POST method and no shipmentTrackingNumber is provided in request. It is recommended to provide less than 20 customer references of 'MRN' type code  # noqa: E501

        :param customer_references: The customer_references of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferences]
        """

        self._customer_references = customer_references

    @property
    def indicative_customs_values(self):
        """Gets the indicative_customs_values of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501


        :return: The indicative_customs_values of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues
        """
        return self._indicative_customs_values

    @indicative_customs_values.setter
    def indicative_customs_values(self, indicative_customs_values):
        """Sets the indicative_customs_values of this SupermodelIoLogisticsExpressExportDeclarationInvoice.


        :param indicative_customs_values: The indicative_customs_values of this SupermodelIoLogisticsExpressExportDeclarationInvoice.  # noqa: E501
        :type: SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues
        """

        self._indicative_customs_values = indicative_customs_values

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
        if issubclass(SupermodelIoLogisticsExpressExportDeclarationInvoice, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressExportDeclarationInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
