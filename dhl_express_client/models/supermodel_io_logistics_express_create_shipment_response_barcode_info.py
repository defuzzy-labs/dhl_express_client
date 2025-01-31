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

class SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo(object):
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
        'shipment_identification_number_barcode_content': 'str',
        'origin_destination_service_type_barcode_content': 'str',
        'routing_barcode_content': 'str',
        'tracking_number_barcodes': 'list[SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes]'
    }

    attribute_map = {
        'shipment_identification_number_barcode_content': 'shipmentIdentificationNumberBarcodeContent',
        'origin_destination_service_type_barcode_content': 'originDestinationServiceTypeBarcodeContent',
        'routing_barcode_content': 'routingBarcodeContent',
        'tracking_number_barcodes': 'trackingNumberBarcodes'
    }

    def __init__(self, shipment_identification_number_barcode_content=None, origin_destination_service_type_barcode_content=None, routing_barcode_content=None, tracking_number_barcodes=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo - a model defined in Swagger"""  # noqa: E501
        self._shipment_identification_number_barcode_content = None
        self._origin_destination_service_type_barcode_content = None
        self._routing_barcode_content = None
        self._tracking_number_barcodes = None
        self.discriminator = None
        if shipment_identification_number_barcode_content is not None:
            self.shipment_identification_number_barcode_content = shipment_identification_number_barcode_content
        if origin_destination_service_type_barcode_content is not None:
            self.origin_destination_service_type_barcode_content = origin_destination_service_type_barcode_content
        if routing_barcode_content is not None:
            self.routing_barcode_content = routing_barcode_content
        if tracking_number_barcodes is not None:
            self.tracking_number_barcodes = tracking_number_barcodes

    @property
    def shipment_identification_number_barcode_content(self):
        """Gets the shipment_identification_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501

        Barcode base64 encoded airwaybill number  # noqa: E501

        :return: The shipment_identification_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._shipment_identification_number_barcode_content

    @shipment_identification_number_barcode_content.setter
    def shipment_identification_number_barcode_content(self, shipment_identification_number_barcode_content):
        """Sets the shipment_identification_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.

        Barcode base64 encoded airwaybill number  # noqa: E501

        :param shipment_identification_number_barcode_content: The shipment_identification_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :type: str
        """

        self._shipment_identification_number_barcode_content = shipment_identification_number_barcode_content

    @property
    def origin_destination_service_type_barcode_content(self):
        """Gets the origin_destination_service_type_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501

        Barcode base64 image of origin service area code, destination service area code and global product code  # noqa: E501

        :return: The origin_destination_service_type_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._origin_destination_service_type_barcode_content

    @origin_destination_service_type_barcode_content.setter
    def origin_destination_service_type_barcode_content(self, origin_destination_service_type_barcode_content):
        """Sets the origin_destination_service_type_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.

        Barcode base64 image of origin service area code, destination service area code and global product code  # noqa: E501

        :param origin_destination_service_type_barcode_content: The origin_destination_service_type_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :type: str
        """

        self._origin_destination_service_type_barcode_content = origin_destination_service_type_barcode_content

    @property
    def routing_barcode_content(self):
        """Gets the routing_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501

        Barcode base64 image of DHL routing code  # noqa: E501

        :return: The routing_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._routing_barcode_content

    @routing_barcode_content.setter
    def routing_barcode_content(self, routing_barcode_content):
        """Sets the routing_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.

        Barcode base64 image of DHL routing code  # noqa: E501

        :param routing_barcode_content: The routing_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :type: str
        """

        self._routing_barcode_content = routing_barcode_content

    @property
    def tracking_number_barcodes(self):
        """Gets the tracking_number_barcodes of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501

        Here you can find barcode details for each piece  # noqa: E501

        :return: The tracking_number_barcodes of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes]
        """
        return self._tracking_number_barcodes

    @tracking_number_barcodes.setter
    def tracking_number_barcodes(self, tracking_number_barcodes):
        """Sets the tracking_number_barcodes of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.

        Here you can find barcode details for each piece  # noqa: E501

        :param tracking_number_barcodes: The tracking_number_barcodes of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes]
        """

        self._tracking_number_barcodes = tracking_number_barcodes

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
