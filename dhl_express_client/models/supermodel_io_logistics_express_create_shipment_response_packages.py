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

class SupermodelIoLogisticsExpressCreateShipmentResponsePackages(object):
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
        'tracking_number': 'str',
        'tracking_url': 'str',
        'volumetric_weight': 'float',
        'documents': 'list[SupermodelIoLogisticsExpressCreateShipmentResponseDocuments]'
    }

    attribute_map = {
        'reference_number': 'referenceNumber',
        'tracking_number': 'trackingNumber',
        'tracking_url': 'trackingUrl',
        'volumetric_weight': 'volumetricWeight',
        'documents': 'documents'
    }

    def __init__(self, reference_number=None, tracking_number=None, tracking_url=None, volumetric_weight=None, documents=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentResponsePackages - a model defined in Swagger"""  # noqa: E501
        self._reference_number = None
        self._tracking_number = None
        self._tracking_url = None
        self._volumetric_weight = None
        self._documents = None
        self.discriminator = None
        if reference_number is not None:
            self.reference_number = reference_number
        self.tracking_number = tracking_number
        if tracking_url is not None:
            self.tracking_url = tracking_url
        if volumetric_weight is not None:
            self.volumetric_weight = volumetric_weight
        if documents is not None:
            self.documents = documents

    @property
    def reference_number(self):
        """Gets the reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501

        Piece serial number  # noqa: E501

        :return: The reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :rtype: float
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.

        Piece serial number  # noqa: E501

        :param reference_number: The reference_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :type: float
        """

        self._reference_number = reference_number

    @property
    def tracking_number(self):
        """Gets the tracking_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501

        Here is provided each piece its Identification number  # noqa: E501

        :return: The tracking_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.

        Here is provided each piece its Identification number  # noqa: E501

        :param tracking_number: The tracking_number of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :type: str
        """
        if tracking_number is None:
            raise ValueError("Invalid value for `tracking_number`, must not be `None`")  # noqa: E501

        self._tracking_number = tracking_number

    @property
    def tracking_url(self):
        """Gets the tracking_url of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501

        You can use ths URL to track your shipment by Piece Identification Number  # noqa: E501

        :return: The tracking_url of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :rtype: str
        """
        return self._tracking_url

    @tracking_url.setter
    def tracking_url(self, tracking_url):
        """Sets the tracking_url of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.

        You can use ths URL to track your shipment by Piece Identification Number  # noqa: E501

        :param tracking_url: The tracking_url of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :type: str
        """

        self._tracking_url = tracking_url

    @property
    def volumetric_weight(self):
        """Gets the volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501

        Here is provided each piece volumetric/ dimensional weight  # noqa: E501

        :return: The volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :rtype: float
        """
        return self._volumetric_weight

    @volumetric_weight.setter
    def volumetric_weight(self, volumetric_weight):
        """Sets the volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.

        Here is provided each piece volumetric/ dimensional weight  # noqa: E501

        :param volumetric_weight: The volumetric_weight of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :type: float
        """

        self._volumetric_weight = volumetric_weight

    @property
    def documents(self):
        """Gets the documents of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501

        Here you can find all documents created for the piece's QRcode  # noqa: E501

        :return: The documents of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentResponseDocuments]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.

        Here you can find all documents created for the piece's QRcode  # noqa: E501

        :param documents: The documents of this SupermodelIoLogisticsExpressCreateShipmentResponsePackages.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentResponseDocuments]
        """

        self._documents = documents

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentResponsePackages, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentResponsePackages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
