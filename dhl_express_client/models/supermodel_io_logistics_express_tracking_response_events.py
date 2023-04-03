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

class SupermodelIoLogisticsExpressTrackingResponseEvents(object):
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
        '_date': 'str',
        'time': 'str',
        'type_code': 'str',
        'description': 'str',
        'service_area': 'list[SupermodelIoLogisticsExpressTrackingResponseServiceArea]',
        'signed_by': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'time': 'time',
        'type_code': 'typeCode',
        'description': 'description',
        'service_area': 'serviceArea',
        'signed_by': 'signedBy'
    }

    def __init__(self, _date=None, time=None, type_code=None, description=None, service_area=None, signed_by=None):  # noqa: E501
        """SupermodelIoLogisticsExpressTrackingResponseEvents - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._time = None
        self._type_code = None
        self._description = None
        self._service_area = None
        self._signed_by = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if time is not None:
            self.time = time
        if type_code is not None:
            self.type_code = type_code
        if description is not None:
            self.description = description
        if service_area is not None:
            self.service_area = service_area
        if signed_by is not None:
            self.signed_by = signed_by

    @property
    def _date(self):
        """Gets the _date of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The _date of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param _date: The _date of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def time(self):
        """Gets the time of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The time of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param time: The time of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The type_code of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param type_code: The type_code of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: str
        """

        self._type_code = type_code

    @property
    def description(self):
        """Gets the description of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The description of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param description: The description of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_area(self):
        """Gets the service_area of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The service_area of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressTrackingResponseServiceArea]
        """
        return self._service_area

    @service_area.setter
    def service_area(self, service_area):
        """Sets the service_area of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param service_area: The service_area of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressTrackingResponseServiceArea]
        """

        self._service_area = service_area

    @property
    def signed_by(self):
        """Gets the signed_by of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501


        :return: The signed_by of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :rtype: str
        """
        return self._signed_by

    @signed_by.setter
    def signed_by(self, signed_by):
        """Sets the signed_by of this SupermodelIoLogisticsExpressTrackingResponseEvents.


        :param signed_by: The signed_by of this SupermodelIoLogisticsExpressTrackingResponseEvents.  # noqa: E501
        :type: str
        """

        self._signed_by = signed_by

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
        if issubclass(SupermodelIoLogisticsExpressTrackingResponseEvents, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressTrackingResponseEvents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
