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

class SupermodelIoLogisticsExpressPickupRequest(object):
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
        'planned_pickup_date_and_time': 'str',
        'close_time': 'str',
        'location': 'str',
        'location_type': 'str',
        'accounts': 'list[SupermodelIoLogisticsExpressAccount]',
        'special_instructions': 'list[SupermodelIoLogisticsExpressPickupRequestSpecialInstructions]',
        'remark': 'str',
        'customer_details': 'SupermodelIoLogisticsExpressPickupRequestCustomerDetails',
        'shipment_details': 'list[SupermodelIoLogisticsExpressPickupRequestShipmentDetails]'
    }

    attribute_map = {
        'planned_pickup_date_and_time': 'plannedPickupDateAndTime',
        'close_time': 'closeTime',
        'location': 'location',
        'location_type': 'locationType',
        'accounts': 'accounts',
        'special_instructions': 'specialInstructions',
        'remark': 'remark',
        'customer_details': 'customerDetails',
        'shipment_details': 'shipmentDetails'
    }

    def __init__(self, planned_pickup_date_and_time=None, close_time=None, location=None, location_type=None, accounts=None, special_instructions=None, remark=None, customer_details=None, shipment_details=None):  # noqa: E501
        """SupermodelIoLogisticsExpressPickupRequest - a model defined in Swagger"""  # noqa: E501
        self._planned_pickup_date_and_time = None
        self._close_time = None
        self._location = None
        self._location_type = None
        self._accounts = None
        self._special_instructions = None
        self._remark = None
        self._customer_details = None
        self._shipment_details = None
        self.discriminator = None
        self.planned_pickup_date_and_time = planned_pickup_date_and_time
        if close_time is not None:
            self.close_time = close_time
        if location is not None:
            self.location = location
        if location_type is not None:
            self.location_type = location_type
        self.accounts = accounts
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if remark is not None:
            self.remark = remark
        self.customer_details = customer_details
        self.shipment_details = shipment_details

    @property
    def planned_pickup_date_and_time(self):
        """Gets the planned_pickup_date_and_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Identifies the date and time the package is ready for pickup Both the date and time portions of the string are expected to be used. The date should not be a past date or a date more than 10 days in the future. The time is the local time of the shipment based on the shipper's time zone. The date component must be in the format: YYYY-MM-DD; the time component must be in the format: HH:MM:SS using a 24 hour clock. The date and time parts are separated by the letter T (e.g. 2006-06-26T17:00:00 GMT+01:00).<BR>                             # noqa: E501

        :return: The planned_pickup_date_and_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._planned_pickup_date_and_time

    @planned_pickup_date_and_time.setter
    def planned_pickup_date_and_time(self, planned_pickup_date_and_time):
        """Sets the planned_pickup_date_and_time of this SupermodelIoLogisticsExpressPickupRequest.

        Identifies the date and time the package is ready for pickup Both the date and time portions of the string are expected to be used. The date should not be a past date or a date more than 10 days in the future. The time is the local time of the shipment based on the shipper's time zone. The date component must be in the format: YYYY-MM-DD; the time component must be in the format: HH:MM:SS using a 24 hour clock. The date and time parts are separated by the letter T (e.g. 2006-06-26T17:00:00 GMT+01:00).<BR>                             # noqa: E501

        :param planned_pickup_date_and_time: The planned_pickup_date_and_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: str
        """
        if planned_pickup_date_and_time is None:
            raise ValueError("Invalid value for `planned_pickup_date_and_time`, must not be `None`")  # noqa: E501

        self._planned_pickup_date_and_time = planned_pickup_date_and_time

    @property
    def close_time(self):
        """Gets the close_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)   # noqa: E501

        :return: The close_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._close_time

    @close_time.setter
    def close_time(self, close_time):
        """Sets the close_time of this SupermodelIoLogisticsExpressPickupRequest.

        The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)   # noqa: E501

        :param close_time: The close_time of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: str
        """

        self._close_time = close_time

    @property
    def location(self):
        """Gets the location of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Provides information on where the package should be picked up by DHL courier. <BR>                             # noqa: E501

        :return: The location of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SupermodelIoLogisticsExpressPickupRequest.

        Provides information on where the package should be picked up by DHL courier. <BR>                             # noqa: E501

        :param location: The location of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def location_type(self):
        """Gets the location_type of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Provides information on where the package should be picked up by DHL courier. <BR>                             # noqa: E501

        :return: The location_type of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this SupermodelIoLogisticsExpressPickupRequest.

        Provides information on where the package should be picked up by DHL courier. <BR>                             # noqa: E501

        :param location_type: The location_type of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["business", "residence"]  # noqa: E501
        if location_type not in allowed_values:
            raise ValueError(
                "Invalid value for `location_type` ({0}), must be one of {1}"  # noqa: E501
                .format(location_type, allowed_values)
            )

        self._location_type = location_type

    @property
    def accounts(self):
        """Gets the accounts of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501


        :return: The accounts of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SupermodelIoLogisticsExpressPickupRequest.


        :param accounts: The accounts of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressAccount]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def special_instructions(self):
        """Gets the special_instructions of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Details special pickup instructions you may wish to send to the DHL Courier.  # noqa: E501

        :return: The special_instructions of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressPickupRequestSpecialInstructions]
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this SupermodelIoLogisticsExpressPickupRequest.

        Details special pickup instructions you may wish to send to the DHL Courier.  # noqa: E501

        :param special_instructions: The special_instructions of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressPickupRequestSpecialInstructions]
        """

        self._special_instructions = special_instructions

    @property
    def remark(self):
        """Gets the remark of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Please provide additional pickup remark  # noqa: E501

        :return: The remark of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this SupermodelIoLogisticsExpressPickupRequest.

        Please provide additional pickup remark  # noqa: E501

        :param remark: The remark of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def customer_details(self):
        """Gets the customer_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501


        :return: The customer_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressPickupRequestCustomerDetails
        """
        return self._customer_details

    @customer_details.setter
    def customer_details(self, customer_details):
        """Sets the customer_details of this SupermodelIoLogisticsExpressPickupRequest.


        :param customer_details: The customer_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: SupermodelIoLogisticsExpressPickupRequestCustomerDetails
        """
        if customer_details is None:
            raise ValueError("Invalid value for `customer_details`, must not be `None`")  # noqa: E501

        self._customer_details = customer_details

    @property
    def shipment_details(self):
        """Gets the shipment_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501

        Please provide details related to shipment you want to do the pickup for  # noqa: E501

        :return: The shipment_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressPickupRequestShipmentDetails]
        """
        return self._shipment_details

    @shipment_details.setter
    def shipment_details(self, shipment_details):
        """Sets the shipment_details of this SupermodelIoLogisticsExpressPickupRequest.

        Please provide details related to shipment you want to do the pickup for  # noqa: E501

        :param shipment_details: The shipment_details of this SupermodelIoLogisticsExpressPickupRequest.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressPickupRequestShipmentDetails]
        """
        if shipment_details is None:
            raise ValueError("Invalid value for `shipment_details`, must not be `None`")  # noqa: E501

        self._shipment_details = shipment_details

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
        if issubclass(SupermodelIoLogisticsExpressPickupRequest, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressPickupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
