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

class SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery(object):
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
        'delivery_option': 'str',
        'location': 'str',
        'special_instructions': 'str',
        'gate_code': 'str',
        'where_to_leave': 'str',
        'neighbour_name': 'str',
        'neighbour_house_number': 'str',
        'authorizer_name': 'str',
        'service_point_id': 'str',
        'requested_delivery_date': 'str'
    }

    attribute_map = {
        'delivery_option': 'deliveryOption',
        'location': 'location',
        'special_instructions': 'specialInstructions',
        'gate_code': 'gateCode',
        'where_to_leave': 'whereToLeave',
        'neighbour_name': 'neighbourName',
        'neighbour_house_number': 'neighbourHouseNumber',
        'authorizer_name': 'authorizerName',
        'service_point_id': 'servicePointId',
        'requested_delivery_date': 'requestedDeliveryDate'
    }

    def __init__(self, delivery_option=None, location=None, special_instructions=None, gate_code=None, where_to_leave=None, neighbour_name=None, neighbour_house_number=None, authorizer_name=None, service_point_id=None, requested_delivery_date=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery - a model defined in Swagger"""  # noqa: E501
        self._delivery_option = None
        self._location = None
        self._special_instructions = None
        self._gate_code = None
        self._where_to_leave = None
        self._neighbour_name = None
        self._neighbour_house_number = None
        self._authorizer_name = None
        self._service_point_id = None
        self._requested_delivery_date = None
        self.discriminator = None
        self.delivery_option = delivery_option
        if location is not None:
            self.location = location
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if gate_code is not None:
            self.gate_code = gate_code
        if where_to_leave is not None:
            self.where_to_leave = where_to_leave
        if neighbour_name is not None:
            self.neighbour_name = neighbour_name
        if neighbour_house_number is not None:
            self.neighbour_house_number = neighbour_house_number
        if authorizer_name is not None:
            self.authorizer_name = authorizer_name
        if service_point_id is not None:
            self.service_point_id = service_point_id
        if requested_delivery_date is not None:
            self.requested_delivery_date = requested_delivery_date

    @property
    def delivery_option(self):
        """Gets the delivery_option of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        Please choose from one of the delivery options  # noqa: E501

        :return: The delivery_option of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._delivery_option

    @delivery_option.setter
    def delivery_option(self, delivery_option):
        """Sets the delivery_option of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        Please choose from one of the delivery options  # noqa: E501

        :param delivery_option: The delivery_option of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """
        if delivery_option is None:
            raise ValueError("Invalid value for `delivery_option`, must not be `None`")  # noqa: E501
        allowed_values = ["servicepoint", "neighbour", "signatureRelease"]  # noqa: E501
        if delivery_option not in allowed_values:
            raise ValueError(
                "Invalid value for `delivery_option` ({0}), must be one of {1}"  # noqa: E501
                .format(delivery_option, allowed_values)
            )

        self._delivery_option = delivery_option

    @property
    def location(self):
        """Gets the location of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        If delivery option is signatureDelivery please specify location where to leave the shipment  # noqa: E501

        :return: The location of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        If delivery option is signatureDelivery please specify location where to leave the shipment  # noqa: E501

        :param location: The location of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def special_instructions(self):
        """Gets the special_instructions of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        Please enter additional information that might be useful for the DHL Express courier. This field is conditionally mandatory if selected location is 'Other'.  # noqa: E501

        :return: The special_instructions of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        Please enter additional information that might be useful for the DHL Express courier. This field is conditionally mandatory if selected location is 'Other'.  # noqa: E501

        :param special_instructions: The special_instructions of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def gate_code(self):
        """Gets the gate_code of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        Please provide entry code to gain access to an apartment complex or gate  # noqa: E501

        :return: The gate_code of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._gate_code

    @gate_code.setter
    def gate_code(self, gate_code):
        """Sets the gate_code of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        Please provide entry code to gain access to an apartment complex or gate  # noqa: E501

        :param gate_code: The gate_code of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._gate_code = gate_code

    @property
    def where_to_leave(self):
        """Gets the where_to_leave of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        In ase your deliveryOption is 'neighbour' please specify where to leave the package   # noqa: E501

        :return: The where_to_leave of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._where_to_leave

    @where_to_leave.setter
    def where_to_leave(self, where_to_leave):
        """Sets the where_to_leave of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        In ase your deliveryOption is 'neighbour' please specify where to leave the package   # noqa: E501

        :param where_to_leave: The where_to_leave of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """
        allowed_values = ["concierge", "neighbour"]  # noqa: E501
        if where_to_leave not in allowed_values:
            raise ValueError(
                "Invalid value for `where_to_leave` ({0}), must be one of {1}"  # noqa: E501
                .format(where_to_leave, allowed_values)
            )

        self._where_to_leave = where_to_leave

    @property
    def neighbour_name(self):
        """Gets the neighbour_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        In case you wish to leave the package with neighbour please provide the neighbour's name  # noqa: E501

        :return: The neighbour_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._neighbour_name

    @neighbour_name.setter
    def neighbour_name(self, neighbour_name):
        """Sets the neighbour_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        In case you wish to leave the package with neighbour please provide the neighbour's name  # noqa: E501

        :param neighbour_name: The neighbour_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._neighbour_name = neighbour_name

    @property
    def neighbour_house_number(self):
        """Gets the neighbour_house_number of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        In case you wish to leave the package with neighbour please provide the neighbour's house number  # noqa: E501

        :return: The neighbour_house_number of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._neighbour_house_number

    @neighbour_house_number.setter
    def neighbour_house_number(self, neighbour_house_number):
        """Sets the neighbour_house_number of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        In case you wish to leave the package with neighbour please provide the neighbour's house number  # noqa: E501

        :param neighbour_house_number: The neighbour_house_number of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._neighbour_house_number = neighbour_house_number

    @property
    def authorizer_name(self):
        """Gets the authorizer_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        In case your delivery option is 'signatureRelease' please provide name of the person who is authorized to sign and receive the package  # noqa: E501

        :return: The authorizer_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._authorizer_name

    @authorizer_name.setter
    def authorizer_name(self, authorizer_name):
        """Sets the authorizer_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        In case your delivery option is 'signatureRelease' please provide name of the person who is authorized to sign and receive the package  # noqa: E501

        :param authorizer_name: The authorizer_name of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._authorizer_name = authorizer_name

    @property
    def service_point_id(self):
        """Gets the service_point_id of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        In case your delivery option is 'servicepoint' please provide unique DHL Express Service point location ID of where the parcel should be delieverd (please contact your local DHL Express Account Manager to obtain the list of the servicepoint IDs)  # noqa: E501

        :return: The service_point_id of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._service_point_id

    @service_point_id.setter
    def service_point_id(self, service_point_id):
        """Sets the service_point_id of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        In case your delivery option is 'servicepoint' please provide unique DHL Express Service point location ID of where the parcel should be delieverd (please contact your local DHL Express Account Manager to obtain the list of the servicepoint IDs)  # noqa: E501

        :param service_point_id: The service_point_id of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._service_point_id = service_point_id

    @property
    def requested_delivery_date(self):
        """Gets the requested_delivery_date of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501

        for future use  # noqa: E501

        :return: The requested_delivery_date of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :rtype: str
        """
        return self._requested_delivery_date

    @requested_delivery_date.setter
    def requested_delivery_date(self, requested_delivery_date):
        """Sets the requested_delivery_date of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.

        for future use  # noqa: E501

        :param requested_delivery_date: The requested_delivery_date of this SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.  # noqa: E501
        :type: str
        """

        self._requested_delivery_date = requested_delivery_date

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
