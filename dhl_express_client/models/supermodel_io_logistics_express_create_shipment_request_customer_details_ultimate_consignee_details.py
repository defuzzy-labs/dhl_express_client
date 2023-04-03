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

class SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails(object):
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
        'postal_address': 'SupermodelIoLogisticsExpressAddressCreateShipmentRequest',
        'contact_information': 'SupermodelIoLogisticsExpressContact',
        'registration_numbers': 'list[SupermodelIoLogisticsExpressRegistrationNumbers]',
        'bank_details': 'SupermodelIoLogisticsExpressRegistrationNumbers',
        'type_code': 'str'
    }

    attribute_map = {
        'postal_address': 'postalAddress',
        'contact_information': 'contactInformation',
        'registration_numbers': 'registrationNumbers',
        'bank_details': 'bankDetails',
        'type_code': 'typeCode'
    }

    def __init__(self, postal_address=None, contact_information=None, registration_numbers=None, bank_details=None, type_code=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails - a model defined in Swagger"""  # noqa: E501
        self._postal_address = None
        self._contact_information = None
        self._registration_numbers = None
        self._bank_details = None
        self._type_code = None
        self.discriminator = None
        self.postal_address = postal_address
        self.contact_information = contact_information
        if registration_numbers is not None:
            self.registration_numbers = registration_numbers
        if bank_details is not None:
            self.bank_details = bank_details
        if type_code is not None:
            self.type_code = type_code

    @property
    def postal_address(self):
        """Gets the postal_address of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501


        :return: The postal_address of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressAddressCreateShipmentRequest
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.


        :param postal_address: The postal_address of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressAddressCreateShipmentRequest
        """
        if postal_address is None:
            raise ValueError("Invalid value for `postal_address`, must not be `None`")  # noqa: E501

        self._postal_address = postal_address

    @property
    def contact_information(self):
        """Gets the contact_information of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501


        :return: The contact_information of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressContact
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information):
        """Sets the contact_information of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.


        :param contact_information: The contact_information of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressContact
        """
        if contact_information is None:
            raise ValueError("Invalid value for `contact_information`, must not be `None`")  # noqa: E501

        self._contact_information = contact_information

    @property
    def registration_numbers(self):
        """Gets the registration_numbers of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501


        :return: The registration_numbers of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressRegistrationNumbers]
        """
        return self._registration_numbers

    @registration_numbers.setter
    def registration_numbers(self, registration_numbers):
        """Sets the registration_numbers of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.


        :param registration_numbers: The registration_numbers of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressRegistrationNumbers]
        """

        self._registration_numbers = registration_numbers

    @property
    def bank_details(self):
        """Gets the bank_details of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501


        :return: The bank_details of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressRegistrationNumbers
        """
        return self._bank_details

    @bank_details.setter
    def bank_details(self, bank_details):
        """Sets the bank_details of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.


        :param bank_details: The bank_details of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressRegistrationNumbers
        """

        self._bank_details = bank_details

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501

        Please enter the business party role type of the ultimate consignee  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.

        Please enter the business party role type of the ultimate consignee  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails.  # noqa: E501
        :type: str
        """

        self._type_code = type_code

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetailsUltimateConsigneeDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other