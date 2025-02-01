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

class SupermodelIoLogisticsExpressProductsPickupCapabilities(object):
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
        'next_business_day': 'bool',
        'local_cutoff_date_and_time': 'str',
        'gmt_cutoff_time': 'str',
        'pickup_earliest': 'str',
        'pickup_latest': 'str',
        'origin_service_area_code': 'str',
        'origin_facility_area_code': 'str',
        'pickup_additional_days': 'float',
        'pickup_day_of_week': 'float'
    }

    attribute_map = {
        'next_business_day': 'nextBusinessDay',
        'local_cutoff_date_and_time': 'localCutoffDateAndTime',
        'gmt_cutoff_time': 'GMTCutoffTime',
        'pickup_earliest': 'pickupEarliest',
        'pickup_latest': 'pickupLatest',
        'origin_service_area_code': 'originServiceAreaCode',
        'origin_facility_area_code': 'originFacilityAreaCode',
        'pickup_additional_days': 'pickupAdditionalDays',
        'pickup_day_of_week': 'pickupDayOfWeek'
    }

    def __init__(self, next_business_day=None, local_cutoff_date_and_time=None, gmt_cutoff_time=None, pickup_earliest=None, pickup_latest=None, origin_service_area_code=None, origin_facility_area_code=None, pickup_additional_days=None, pickup_day_of_week=None):  # noqa: E501
        """SupermodelIoLogisticsExpressProductsPickupCapabilities - a model defined in Swagger"""  # noqa: E501
        self._next_business_day = None
        self._local_cutoff_date_and_time = None
        self._gmt_cutoff_time = None
        self._pickup_earliest = None
        self._pickup_latest = None
        self._origin_service_area_code = None
        self._origin_facility_area_code = None
        self._pickup_additional_days = None
        self._pickup_day_of_week = None
        self.discriminator = None
        if next_business_day is not None:
            self.next_business_day = next_business_day
        if local_cutoff_date_and_time is not None:
            self.local_cutoff_date_and_time = local_cutoff_date_and_time
        if gmt_cutoff_time is not None:
            self.gmt_cutoff_time = gmt_cutoff_time
        if pickup_earliest is not None:
            self.pickup_earliest = pickup_earliest
        if pickup_latest is not None:
            self.pickup_latest = pickup_latest
        if origin_service_area_code is not None:
            self.origin_service_area_code = origin_service_area_code
        if origin_facility_area_code is not None:
            self.origin_facility_area_code = origin_facility_area_code
        if pickup_additional_days is not None:
            self.pickup_additional_days = pickup_additional_days
        if pickup_day_of_week is not None:
            self.pickup_day_of_week = pickup_day_of_week

    @property
    def next_business_day(self):
        """Gets the next_business_day of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        This indicator has values of Y or N, and tells the consumer if the service in the response has a pickup date on the same day as the requested shipment date (per the request).  # noqa: E501

        :return: The next_business_day of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: bool
        """
        return self._next_business_day

    @next_business_day.setter
    def next_business_day(self, next_business_day):
        """Sets the next_business_day of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        This indicator has values of Y or N, and tells the consumer if the service in the response has a pickup date on the same day as the requested shipment date (per the request).  # noqa: E501

        :param next_business_day: The next_business_day of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: bool
        """

        self._next_business_day = next_business_day

    @property
    def local_cutoff_date_and_time(self):
        """Gets the local_cutoff_date_and_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        This is the cutoff time for the service<BR>                offered in the response. This represents the latest time (local to origin) which the shipment can be tendered to the courier for that service on that day.  # noqa: E501

        :return: The local_cutoff_date_and_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._local_cutoff_date_and_time

    @local_cutoff_date_and_time.setter
    def local_cutoff_date_and_time(self, local_cutoff_date_and_time):
        """Sets the local_cutoff_date_and_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        This is the cutoff time for the service<BR>                offered in the response. This represents the latest time (local to origin) which the shipment can be tendered to the courier for that service on that day.  # noqa: E501

        :param local_cutoff_date_and_time: The local_cutoff_date_and_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._local_cutoff_date_and_time = local_cutoff_date_and_time

    @property
    def gmt_cutoff_time(self):
        """Gets the gmt_cutoff_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        Pickup cut off time in GMT  # noqa: E501

        :return: The gmt_cutoff_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._gmt_cutoff_time

    @gmt_cutoff_time.setter
    def gmt_cutoff_time(self, gmt_cutoff_time):
        """Sets the gmt_cutoff_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        Pickup cut off time in GMT  # noqa: E501

        :param gmt_cutoff_time: The gmt_cutoff_time of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._gmt_cutoff_time = gmt_cutoff_time

    @property
    def pickup_earliest(self):
        """Gets the pickup_earliest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        The DHL earliest time possible for pickup  # noqa: E501

        :return: The pickup_earliest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._pickup_earliest

    @pickup_earliest.setter
    def pickup_earliest(self, pickup_earliest):
        """Sets the pickup_earliest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        The DHL earliest time possible for pickup  # noqa: E501

        :param pickup_earliest: The pickup_earliest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._pickup_earliest = pickup_earliest

    @property
    def pickup_latest(self):
        """Gets the pickup_latest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        The DHL latest time possible for pickup  # noqa: E501

        :return: The pickup_latest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._pickup_latest

    @pickup_latest.setter
    def pickup_latest(self, pickup_latest):
        """Sets the pickup_latest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        The DHL latest time possible for pickup  # noqa: E501

        :param pickup_latest: The pickup_latest of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._pickup_latest = pickup_latest

    @property
    def origin_service_area_code(self):
        """Gets the origin_service_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        The DHL Service Area Code for the origin of the Shipment  # noqa: E501

        :return: The origin_service_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._origin_service_area_code

    @origin_service_area_code.setter
    def origin_service_area_code(self, origin_service_area_code):
        """Sets the origin_service_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        The DHL Service Area Code for the origin of the Shipment  # noqa: E501

        :param origin_service_area_code: The origin_service_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._origin_service_area_code = origin_service_area_code

    @property
    def origin_facility_area_code(self):
        """Gets the origin_facility_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        The DHL Facility Code for the Origin  # noqa: E501

        :return: The origin_facility_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: str
        """
        return self._origin_facility_area_code

    @origin_facility_area_code.setter
    def origin_facility_area_code(self, origin_facility_area_code):
        """Sets the origin_facility_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        The DHL Facility Code for the Origin  # noqa: E501

        :param origin_facility_area_code: The origin_facility_area_code of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: str
        """

        self._origin_facility_area_code = origin_facility_area_code

    @property
    def pickup_additional_days(self):
        """Gets the pickup_additional_days of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        This is additional transit delays (in days) for shipment picked up from the mentioned city or postal area to arrival at the service area.  # noqa: E501

        :return: The pickup_additional_days of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._pickup_additional_days

    @pickup_additional_days.setter
    def pickup_additional_days(self, pickup_additional_days):
        """Sets the pickup_additional_days of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        This is additional transit delays (in days) for shipment picked up from the mentioned city or postal area to arrival at the service area.  # noqa: E501

        :param pickup_additional_days: The pickup_additional_days of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: float
        """

        self._pickup_additional_days = pickup_additional_days

    @property
    def pickup_day_of_week(self):
        """Gets the pickup_day_of_week of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501

        Pickup day of the week number  # noqa: E501

        :return: The pickup_day_of_week of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :rtype: float
        """
        return self._pickup_day_of_week

    @pickup_day_of_week.setter
    def pickup_day_of_week(self, pickup_day_of_week):
        """Sets the pickup_day_of_week of this SupermodelIoLogisticsExpressProductsPickupCapabilities.

        Pickup day of the week number  # noqa: E501

        :param pickup_day_of_week: The pickup_day_of_week of this SupermodelIoLogisticsExpressProductsPickupCapabilities.  # noqa: E501
        :type: float
        """

        self._pickup_day_of_week = pickup_day_of_week

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
        if issubclass(SupermodelIoLogisticsExpressProductsPickupCapabilities, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressProductsPickupCapabilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
