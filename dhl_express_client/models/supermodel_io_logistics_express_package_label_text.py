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

class SupermodelIoLogisticsExpressPackageLabelText(object):
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
        'position': 'str',
        'caption': 'str',
        'value': 'str'
    }

    attribute_map = {
        'position': 'position',
        'caption': 'caption',
        'value': 'value'
    }

    def __init__(self, position=None, caption=None, value=None):  # noqa: E501
        """SupermodelIoLogisticsExpressPackageLabelText - a model defined in Swagger"""  # noqa: E501
        self._position = None
        self._caption = None
        self._value = None
        self.discriminator = None
        self.position = position
        self.caption = caption
        self.value = value

    @property
    def position(self):
        """Gets the position of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501

        Position of the bespoke text  # noqa: E501

        :return: The position of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SupermodelIoLogisticsExpressPackageLabelText.

        Position of the bespoke text  # noqa: E501

        :param position: The position of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
        :type: str
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501
        allowed_values = ["left1", "left2", "left3", "right1", "right2", "right3"]  # noqa: E501
        if position not in allowed_values:
            raise ValueError(
                "Invalid value for `position` ({0}), must be one of {1}"  # noqa: E501
                .format(position, allowed_values)
            )

        self._position = position

    @property
    def caption(self):
        """Gets the caption of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501

        Please enter caption to be printed in the tag value  # noqa: E501

        :return: The caption of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this SupermodelIoLogisticsExpressPackageLabelText.

        Please enter caption to be printed in the tag value  # noqa: E501

        :param caption: The caption of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
        :type: str
        """
        if caption is None:
            raise ValueError("Invalid value for `caption`, must not be `None`")  # noqa: E501

        self._caption = caption

    @property
    def value(self):
        """Gets the value of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501

        Please enter value to be printed for the respective tag in caption  # noqa: E501

        :return: The value of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SupermodelIoLogisticsExpressPackageLabelText.

        Please enter value to be printed for the respective tag in caption  # noqa: E501

        :param value: The value of this SupermodelIoLogisticsExpressPackageLabelText.  # noqa: E501
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
        if issubclass(SupermodelIoLogisticsExpressPackageLabelText, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressPackageLabelText):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
