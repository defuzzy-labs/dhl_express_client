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

class SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea(object):
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
        'facility_code': 'str',
        'service_area_code': 'str',
        'inbound_sort_code': 'str'
    }

    attribute_map = {
        'facility_code': 'facilityCode',
        'service_area_code': 'serviceAreaCode',
        'inbound_sort_code': 'inboundSortCode'
    }

    def __init__(self, facility_code=None, service_area_code=None, inbound_sort_code=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea - a model defined in Swagger"""  # noqa: E501
        self._facility_code = None
        self._service_area_code = None
        self._inbound_sort_code = None
        self.discriminator = None
        if facility_code is not None:
            self.facility_code = facility_code
        if service_area_code is not None:
            self.service_area_code = service_area_code
        if inbound_sort_code is not None:
            self.inbound_sort_code = inbound_sort_code

    @property
    def facility_code(self):
        """Gets the facility_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501


        :return: The facility_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._facility_code

    @facility_code.setter
    def facility_code(self, facility_code):
        """Sets the facility_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.


        :param facility_code: The facility_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
        :type: str
        """

        self._facility_code = facility_code

    @property
    def service_area_code(self):
        """Gets the service_area_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501


        :return: The service_area_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._service_area_code

    @service_area_code.setter
    def service_area_code(self, service_area_code):
        """Sets the service_area_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.


        :param service_area_code: The service_area_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
        :type: str
        """

        self._service_area_code = service_area_code

    @property
    def inbound_sort_code(self):
        """Gets the inbound_sort_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501


        :return: The inbound_sort_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
        :rtype: str
        """
        return self._inbound_sort_code

    @inbound_sort_code.setter
    def inbound_sort_code(self, inbound_sort_code):
        """Sets the inbound_sort_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.


        :param inbound_sort_code: The inbound_sort_code of this SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea.  # noqa: E501
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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
