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

class SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification(object):
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
        'receiver_id': 'str',
        'language_code': 'str',
        'language_country_code': 'str',
        'bespoke_message': 'str'
    }

    attribute_map = {
        'type_code': 'typeCode',
        'receiver_id': 'receiverId',
        'language_code': 'languageCode',
        'language_country_code': 'languageCountryCode',
        'bespoke_message': 'bespokeMessage'
    }

    def __init__(self, type_code=None, receiver_id=None, language_code='eng', language_country_code='UK', bespoke_message=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification - a model defined in Swagger"""  # noqa: E501
        self._type_code = None
        self._receiver_id = None
        self._language_code = None
        self._language_country_code = None
        self._bespoke_message = None
        self.discriminator = None
        self.type_code = type_code
        self.receiver_id = receiver_id
        if language_code is not None:
            self.language_code = language_code
        if language_country_code is not None:
            self.language_country_code = language_country_code
        if bespoke_message is not None:
            self.bespoke_message = bespoke_message

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501

        Please enter channel type to send the notification by. At this moment only email is supported  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.

        Please enter channel type to send the notification by. At this moment only email is supported  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501
        allowed_values = ["email"]  # noqa: E501
        if type_code not in allowed_values:
            raise ValueError(
                "Invalid value for `type_code` ({0}), must be one of {1}"  # noqa: E501
                .format(type_code, allowed_values)
            )

        self._type_code = type_code

    @property
    def receiver_id(self):
        """Gets the receiver_id of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501

        Please enter notification receiver email address  # noqa: E501

        :return: The receiver_id of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :rtype: str
        """
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id):
        """Sets the receiver_id of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.

        Please enter notification receiver email address  # noqa: E501

        :param receiver_id: The receiver_id of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :type: str
        """
        if receiver_id is None:
            raise ValueError("Invalid value for `receiver_id`, must not be `None`")  # noqa: E501

        self._receiver_id = receiver_id

    @property
    def language_code(self):
        """Gets the language_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501

        Please enter three letter lanuage code in which you wish to receive the notification in  # noqa: E501

        :return: The language_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.

        Please enter three letter lanuage code in which you wish to receive the notification in  # noqa: E501

        :param language_code: The language_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def language_country_code(self):
        """Gets the language_country_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501

        Please enter two letter language country code  # noqa: E501

        :return: The language_country_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :rtype: str
        """
        return self._language_country_code

    @language_country_code.setter
    def language_country_code(self, language_country_code):
        """Sets the language_country_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.

        Please enter two letter language country code  # noqa: E501

        :param language_country_code: The language_country_code of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :type: str
        """

        self._language_country_code = language_country_code

    @property
    def bespoke_message(self):
        """Gets the bespoke_message of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501

        Please enter your message which will be added to the DHL Express notification email  # noqa: E501

        :return: The bespoke_message of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :rtype: str
        """
        return self._bespoke_message

    @bespoke_message.setter
    def bespoke_message(self, bespoke_message):
        """Sets the bespoke_message of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.

        Please enter your message which will be added to the DHL Express notification email  # noqa: E501

        :param bespoke_message: The bespoke_message of this SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.  # noqa: E501
        :type: str
        """

        self._bespoke_message = bespoke_message

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
