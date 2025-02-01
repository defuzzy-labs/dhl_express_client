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

class SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes(object):
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
        'reference_number': 'float',
        'tracking_number_barcode_content': 'str'
    }

    attribute_map = {
        'reference_number': 'referenceNumber',
        'tracking_number_barcode_content': 'trackingNumberBarcodeContent'
    }

    def __init__(self, reference_number=None, tracking_number_barcode_content=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes - a model defined in Swagger"""  # noqa: E501
        self._reference_number = None
        self._tracking_number_barcode_content = None
        self.discriminator = None
        if reference_number is not None:
            self.reference_number = reference_number
        if tracking_number_barcode_content is not None:
            self.tracking_number_barcode_content = tracking_number_barcode_content

    @property
    def reference_number(self):
        """Gets the reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501

        Piece serial number  # noqa: E501

        :return: The reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501
        :rtype: float
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.

        Piece serial number  # noqa: E501

        :param reference_number: The reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501
        :type: float
        """

        self._reference_number = reference_number

    @property
    def tracking_number_barcode_content(self):
        """Gets the tracking_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501

        Barcode base4 image of each piece of the shipment  # noqa: E501

        :return: The tracking_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number_barcode_content

    @tracking_number_barcode_content.setter
    def tracking_number_barcode_content(self, tracking_number_barcode_content):
        """Sets the tracking_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.

        Barcode base4 image of each piece of the shipment  # noqa: E501

        :param tracking_number_barcode_content: The tracking_number_barcode_content of this SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes.  # noqa: E501
        :type: str
        """

        self._tracking_number_barcode_content = tracking_number_barcode_content

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfoTrackingNumberBarcodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
