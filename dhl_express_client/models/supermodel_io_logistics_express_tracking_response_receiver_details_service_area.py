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

class SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea(object):
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
        'code': 'str',
        'description': 'str',
        'facility_code': 'str',
        'inbound_sort_code': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'facility_code': 'facilityCode',
        'inbound_sort_code': 'inboundSortCode'
    }

    def __init__(self, code=None, description=None, facility_code=None, inbound_sort_code=None):  # noqa: E501
        """SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._description = None
        self._facility_code = None
        self._inbound_sort_code = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if facility_code is not None:
            self.facility_code = facility_code
        if inbound_sort_code is not None:
            self.inbound_sort_code = inbound_sort_code

    @property
    def code(self):
        """Gets the code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501


        :return: The code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.


        :param code: The code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501


        :return: The description of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.


        :param description: The description of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def facility_code(self):
        """Gets the facility_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501


        :return: The facility_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._facility_code

    @facility_code.setter
    def facility_code(self, facility_code):
        """Sets the facility_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.


        :param facility_code: The facility_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :type: str
        """

        self._facility_code = facility_code

    @property
    def inbound_sort_code(self):
        """Gets the inbound_sort_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501


        :return: The inbound_sort_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._inbound_sort_code

    @inbound_sort_code.setter
    def inbound_sort_code(self, inbound_sort_code):
        """Sets the inbound_sort_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.


        :param inbound_sort_code: The inbound_sort_code of this SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea.  # noqa: E501
        :type: str
        """

        self._inbound_sort_code = inbound_sort_code

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
        if issubclass(SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressTrackingResponseReceiverDetailsServiceArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
