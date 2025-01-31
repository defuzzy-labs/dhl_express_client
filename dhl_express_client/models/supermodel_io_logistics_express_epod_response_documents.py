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

class SupermodelIoLogisticsExpressEPODResponseDocuments(object):
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
        'encoding_format': 'str',
        'content': 'str',
        'type_code': 'str'
    }

    attribute_map = {
        'encoding_format': 'encodingFormat',
        'content': 'content',
        'type_code': 'typeCode'
    }

    def __init__(self, encoding_format=None, content=None, type_code=None):  # noqa: E501
        """SupermodelIoLogisticsExpressEPODResponseDocuments - a model defined in Swagger"""  # noqa: E501
        self._encoding_format = None
        self._content = None
        self._type_code = None
        self.discriminator = None
        if encoding_format is not None:
            self.encoding_format = encoding_format
        if content is not None:
            self.content = content
        if type_code is not None:
            self.type_code = type_code

    @property
    def encoding_format(self):
        """Gets the encoding_format of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501


        :return: The encoding_format of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._encoding_format

    @encoding_format.setter
    def encoding_format(self, encoding_format):
        """Sets the encoding_format of this SupermodelIoLogisticsExpressEPODResponseDocuments.


        :param encoding_format: The encoding_format of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
        :type: str
        """

        self._encoding_format = encoding_format

    @property
    def content(self):
        """Gets the content of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501


        :return: The content of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SupermodelIoLogisticsExpressEPODResponseDocuments.


        :param content: The content of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501


        :return: The type_code of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressEPODResponseDocuments.


        :param type_code: The type_code of this SupermodelIoLogisticsExpressEPODResponseDocuments.  # noqa: E501
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
        if issubclass(SupermodelIoLogisticsExpressEPODResponseDocuments, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressEPODResponseDocuments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
