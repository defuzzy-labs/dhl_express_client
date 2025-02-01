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

class Pickup(object):
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
        'is_requested': 'bool',
        'close_time': 'str',
        'location': 'str',
        'special_instructions': 'list[PickupSpecialInstructions]',
        'pickup_details': 'PickupPickupDetails',
        'pickup_requestor_details': 'PickupPickupRequestorDetails'
    }

    attribute_map = {
        'is_requested': 'isRequested',
        'close_time': 'closeTime',
        'location': 'location',
        'special_instructions': 'specialInstructions',
        'pickup_details': 'pickupDetails',
        'pickup_requestor_details': 'pickupRequestorDetails'
    }

    def __init__(self, is_requested=False, close_time=None, location=None, special_instructions=None, pickup_details=None, pickup_requestor_details=None):  # noqa: E501
        """Pickup - a model defined in Swagger"""  # noqa: E501
        self._is_requested = None
        self._close_time = None
        self._location = None
        self._special_instructions = None
        self._pickup_details = None
        self._pickup_requestor_details = None
        self.discriminator = None
        self.is_requested = is_requested
        if close_time is not None:
            self.close_time = close_time
        if location is not None:
            self.location = location
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if pickup_details is not None:
            self.pickup_details = pickup_details
        if pickup_requestor_details is not None:
            self.pickup_requestor_details = pickup_requestor_details

    @property
    def is_requested(self):
        """Gets the is_requested of this Pickup.  # noqa: E501

        Please advise if a pickup is needed for this shipment  # noqa: E501

        :return: The is_requested of this Pickup.  # noqa: E501
        :rtype: bool
        """
        return self._is_requested

    @is_requested.setter
    def is_requested(self, is_requested):
        """Sets the is_requested of this Pickup.

        Please advise if a pickup is needed for this shipment  # noqa: E501

        :param is_requested: The is_requested of this Pickup.  # noqa: E501
        :type: bool
        """
        if is_requested is None:
            raise ValueError("Invalid value for `is_requested`, must not be `None`")  # noqa: E501

        self._is_requested = is_requested

    @property
    def close_time(self):
        """Gets the close_time of this Pickup.  # noqa: E501

        The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)   # noqa: E501

        :return: The close_time of this Pickup.  # noqa: E501
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this Pickup.

        The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)   # noqa: E501

        :param close_time: The close_time of this Pickup.  # noqa: E501
        :type: str
        """

        self._close_time = close_time

    @property
    def location(self):
        """Gets the location of this Pickup.  # noqa: E501

        Provides information on where the package should be picked up by DHL courier.  # noqa: E501

        :return: The location of this Pickup.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Pickup.

        Provides information on where the package should be picked up by DHL courier.  # noqa: E501

        :param location: The location of this Pickup.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def special_instructions(self):
        """Gets the special_instructions of this Pickup.  # noqa: E501

        Details special pickup instructions you may wish to send to the DHL Courier.  # noqa: E501

        :return: The special_instructions of this Pickup.  # noqa: E501
        :rtype: list[PickupSpecialInstructions]
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this Pickup.

        Details special pickup instructions you may wish to send to the DHL Courier.  # noqa: E501

        :param special_instructions: The special_instructions of this Pickup.  # noqa: E501
        :type: list[PickupSpecialInstructions]
        """

        self._special_instructions = special_instructions

    @property
    def pickup_details(self):
        """Gets the pickup_details of this Pickup.  # noqa: E501


        :return: The pickup_details of this Pickup.  # noqa: E501
        :rtype: PickupPickupDetails
        """
        return self._pickup_details

    @pickup_details.setter
    def pickup_details(self, pickup_details):
        """Sets the pickup_details of this Pickup.


        :param pickup_details: The pickup_details of this Pickup.  # noqa: E501
        :type: PickupPickupDetails
        """

        self._pickup_details = pickup_details

    @property
    def pickup_requestor_details(self):
        """Gets the pickup_requestor_details of this Pickup.  # noqa: E501


        :return: The pickup_requestor_details of this Pickup.  # noqa: E501
        :rtype: PickupPickupRequestorDetails
        """
        return self._pickup_requestor_details

    @pickup_requestor_details.setter
    def pickup_requestor_details(self, pickup_requestor_details):
        """Sets the pickup_requestor_details of this Pickup.


        :param pickup_requestor_details: The pickup_requestor_details of this Pickup.  # noqa: E501
        :type: PickupPickupRequestorDetails
        """

        self._pickup_requestor_details = pickup_requestor_details

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
        if issubclass(Pickup, dict):
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
        if not isinstance(other, Pickup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
