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

class SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails(object):
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
        'service_handling_feature_codes': 'list[str]',
        'volumetric_weight': 'float',
        'billing_code': 'str',
        'service_content_code': 'str',
        'customer_details': 'SupermodelIoLogisticsExpressCreateShipmentResponseCustomerDetails',
        'origin_service_area': 'SupermodelIoLogisticsExpressCreateShipmentResponseOriginServiceArea',
        'destination_service_area': 'SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea',
        'dhl_routing_code': 'str',
        'dhl_routing_data_id': 'str',
        'delivery_date_code': 'str',
        'delivery_time_code': 'str',
        'product_short_name': 'str',
        'value_added_services': 'list[SupermodelIoLogisticsExpressCreateShipmentResponseValueAddedServices]',
        'pickup_details': 'SupermodelIoLogisticsExpressCreateShipmentResponsePickupDetails'
    }

    attribute_map = {
        'service_handling_feature_codes': 'serviceHandlingFeatureCodes',
        'volumetric_weight': 'volumetricWeight',
        'billing_code': 'billingCode',
        'service_content_code': 'serviceContentCode',
        'customer_details': 'customerDetails',
        'origin_service_area': 'originServiceArea',
        'destination_service_area': 'destinationServiceArea',
        'dhl_routing_code': 'dhlRoutingCode',
        'dhl_routing_data_id': 'dhlRoutingDataId',
        'delivery_date_code': 'deliveryDateCode',
        'delivery_time_code': 'deliveryTimeCode',
        'product_short_name': 'productShortName',
        'value_added_services': 'valueAddedServices',
        'pickup_details': 'pickupDetails'
    }

    def __init__(self, service_handling_feature_codes=None, volumetric_weight=None, billing_code=None, service_content_code=None, customer_details=None, origin_service_area=None, destination_service_area=None, dhl_routing_code=None, dhl_routing_data_id=None, delivery_date_code=None, delivery_time_code=None, product_short_name=None, value_added_services=None, pickup_details=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails - a model defined in Swagger"""  # noqa: E501
        self._service_handling_feature_codes = None
        self._volumetric_weight = None
        self._billing_code = None
        self._service_content_code = None
        self._customer_details = None
        self._origin_service_area = None
        self._destination_service_area = None
        self._dhl_routing_code = None
        self._dhl_routing_data_id = None
        self._delivery_date_code = None
        self._delivery_time_code = None
        self._product_short_name = None
        self._value_added_services = None
        self._pickup_details = None
        self.discriminator = None
        if service_handling_feature_codes is not None:
            self.service_handling_feature_codes = service_handling_feature_codes
        if volumetric_weight is not None:
            self.volumetric_weight = volumetric_weight
        if billing_code is not None:
            self.billing_code = billing_code
        if service_content_code is not None:
            self.service_content_code = service_content_code
        if customer_details is not None:
            self.customer_details = customer_details
        if origin_service_area is not None:
            self.origin_service_area = origin_service_area
        if destination_service_area is not None:
            self.destination_service_area = destination_service_area
        if dhl_routing_code is not None:
            self.dhl_routing_code = dhl_routing_code
        if dhl_routing_data_id is not None:
            self.dhl_routing_data_id = dhl_routing_data_id
        if delivery_date_code is not None:
            self.delivery_date_code = delivery_date_code
        if delivery_time_code is not None:
            self.delivery_time_code = delivery_time_code
        if product_short_name is not None:
            self.product_short_name = product_short_name
        if value_added_services is not None:
            self.value_added_services = value_added_services
        if pickup_details is not None:
            self.pickup_details = pickup_details

    @property
    def service_handling_feature_codes(self):
        """Gets the service_handling_feature_codes of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        This array contains all the DHL Express special handling feature codes  # noqa: E501

        :return: The service_handling_feature_codes of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_handling_feature_codes

    @service_handling_feature_codes.setter
    def service_handling_feature_codes(self, service_handling_feature_codes):
        """Sets the service_handling_feature_codes of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        This array contains all the DHL Express special handling feature codes  # noqa: E501

        :param service_handling_feature_codes: The service_handling_feature_codes of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: list[str]
        """

        self._service_handling_feature_codes = service_handling_feature_codes

    @property
    def volumetric_weight(self):
        """Gets the volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find calculated volumetric weight based on dimensions provided in the request  # noqa: E501

        :return: The volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: float
        """
        return self._volumetric_weight

    @volumetric_weight.setter
    def volumetric_weight(self, volumetric_weight):
        """Sets the volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find calculated volumetric weight based on dimensions provided in the request  # noqa: E501

        :param volumetric_weight: The volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: float
        """

        self._volumetric_weight = volumetric_weight

    @property
    def billing_code(self):
        """Gets the billing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find billing code which was applied on your shipment  # noqa: E501

        :return: The billing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._billing_code

    @billing_code.setter
    def billing_code(self, billing_code):
        """Sets the billing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find billing code which was applied on your shipment  # noqa: E501

        :param billing_code: The billing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._billing_code = billing_code

    @property
    def service_content_code(self):
        """Gets the service_content_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find the DHL Express shipment content code of your shipment  # noqa: E501

        :return: The service_content_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._service_content_code

    @service_content_code.setter
    def service_content_code(self, service_content_code):
        """Sets the service_content_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find the DHL Express shipment content code of your shipment  # noqa: E501

        :param service_content_code: The service_content_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._service_content_code = service_content_code

    @property
    def customer_details(self):
        """Gets the customer_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501


        :return: The customer_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentResponseCustomerDetails
        """
        return self._customer_details

    @customer_details.setter
    def customer_details(self, customer_details):
        """Sets the customer_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.


        :param customer_details: The customer_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentResponseCustomerDetails
        """

        self._customer_details = customer_details

    @property
    def origin_service_area(self):
        """Gets the origin_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501


        :return: The origin_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentResponseOriginServiceArea
        """
        return self._origin_service_area

    @origin_service_area.setter
    def origin_service_area(self, origin_service_area):
        """Sets the origin_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.


        :param origin_service_area: The origin_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentResponseOriginServiceArea
        """

        self._origin_service_area = origin_service_area

    @property
    def destination_service_area(self):
        """Gets the destination_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501


        :return: The destination_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea
        """
        return self._destination_service_area

    @destination_service_area.setter
    def destination_service_area(self, destination_service_area):
        """Sets the destination_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.


        :param destination_service_area: The destination_service_area of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentResponseDestinationServiceArea
        """

        self._destination_service_area = destination_service_area

    @property
    def dhl_routing_code(self):
        """Gets the dhl_routing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find DHL Routing Code which was applied on your shipment  # noqa: E501

        :return: The dhl_routing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._dhl_routing_code

    @dhl_routing_code.setter
    def dhl_routing_code(self, dhl_routing_code):
        """Sets the dhl_routing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find DHL Routing Code which was applied on your shipment  # noqa: E501

        :param dhl_routing_code: The dhl_routing_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._dhl_routing_code = dhl_routing_code

    @property
    def dhl_routing_data_id(self):
        """Gets the dhl_routing_data_id of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find DHL Routing Data ID which was applied on your shipment  # noqa: E501

        :return: The dhl_routing_data_id of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._dhl_routing_data_id

    @dhl_routing_data_id.setter
    def dhl_routing_data_id(self, dhl_routing_data_id):
        """Sets the dhl_routing_data_id of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find DHL Routing Data ID which was applied on your shipment  # noqa: E501

        :param dhl_routing_data_id: The dhl_routing_data_id of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._dhl_routing_data_id = dhl_routing_data_id

    @property
    def delivery_date_code(self):
        """Gets the delivery_date_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find Delivery Date Code which was applied on your shipment  # noqa: E501

        :return: The delivery_date_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._delivery_date_code

    @delivery_date_code.setter
    def delivery_date_code(self, delivery_date_code):
        """Sets the delivery_date_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find Delivery Date Code which was applied on your shipment  # noqa: E501

        :param delivery_date_code: The delivery_date_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._delivery_date_code = delivery_date_code

    @property
    def delivery_time_code(self):
        """Gets the delivery_time_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find Delivery Time Code which was applied on your shipment  # noqa: E501

        :return: The delivery_time_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._delivery_time_code

    @delivery_time_code.setter
    def delivery_time_code(self, delivery_time_code):
        """Sets the delivery_time_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find Delivery Time Code which was applied on your shipment  # noqa: E501

        :param delivery_time_code: The delivery_time_code of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._delivery_time_code = delivery_time_code

    @property
    def product_short_name(self):
        """Gets the product_short_name of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501

        Here you can find the product short name of your shipment  # noqa: E501

        :return: The product_short_name of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._product_short_name

    @product_short_name.setter
    def product_short_name(self, product_short_name):
        """Sets the product_short_name of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.

        Here you can find the product short name of your shipment  # noqa: E501

        :param product_short_name: The product_short_name of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: str
        """

        self._product_short_name = product_short_name

    @property
    def value_added_services(self):
        """Gets the value_added_services of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501


        :return: The value_added_services of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentResponseValueAddedServices]
        """
        return self._value_added_services

    @value_added_services.setter
    def value_added_services(self, value_added_services):
        """Sets the value_added_services of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.


        :param value_added_services: The value_added_services of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentResponseValueAddedServices]
        """

        self._value_added_services = value_added_services

    @property
    def pickup_details(self):
        """Gets the pickup_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501


        :return: The pickup_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentResponsePickupDetails
        """
        return self._pickup_details

    @pickup_details.setter
    def pickup_details(self, pickup_details):
        """Sets the pickup_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.


        :param pickup_details: The pickup_details of this SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentResponsePickupDetails
        """

        self._pickup_details = pickup_details

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other