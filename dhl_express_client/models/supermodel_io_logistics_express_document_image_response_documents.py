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

class SupermodelIoLogisticsExpressDocumentImageResponseDocuments(object):
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
        'shipment_tracking_number': 'str',
        'type_code': 'str',
        'function': 'str',
        'encoding_format': 'str',
        'content': 'str'
    }

    attribute_map = {
        'shipment_tracking_number': 'shipmentTrackingNumber',
        'type_code': 'typeCode',
        'function': 'function',
        'encoding_format': 'encodingFormat',
        'content': 'content'
    }

    def __init__(self, shipment_tracking_number=None, type_code=None, function=None, encoding_format=None, content=None):  # noqa: E501
        """SupermodelIoLogisticsExpressDocumentImageResponseDocuments - a model defined in Swagger"""  # noqa: E501
        self._shipment_tracking_number = None
        self._type_code = None
        self._function = None
        self._encoding_format = None
        self._content = None
        self.discriminator = None
        self.shipment_tracking_number = shipment_tracking_number
        self.type_code = type_code
        if function is not None:
            self.function = function
        self.encoding_format = encoding_format
        self.content = content

    @property
    def shipment_tracking_number(self):
        """Gets the shipment_tracking_number of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501

        Shipment Tracking Number  # noqa: E501

        :return: The shipment_tracking_number of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._shipment_tracking_number

    @shipment_tracking_number.setter
    def shipment_tracking_number(self, shipment_tracking_number):
        """Sets the shipment_tracking_number of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.

        Shipment Tracking Number  # noqa: E501

        :param shipment_tracking_number: The shipment_tracking_number of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :type: str
        """
        if shipment_tracking_number is None:
            raise ValueError("Invalid value for `shipment_tracking_number`, must not be `None`")  # noqa: E501

        self._shipment_tracking_number = shipment_tracking_number

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501

        Identifies type of the document like commercial invoice or waybill, or archived zip documents  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.

        Identifies type of the document like commercial invoice or waybill, or archived zip documents  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501

        self._type_code = type_code

    @property
    def function(self):
        """Gets the function of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501

        Clearance code or document function whether for import, export or both.  Returned only for customs-entry  # noqa: E501

        :return: The function of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.

        Clearance code or document function whether for import, export or both.  Returned only for customs-entry  # noqa: E501

        :param function: The function of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :type: str
        """
        allowed_values = ["import", "export", "both"]  # noqa: E501
        if function not in allowed_values:
            raise ValueError(
                "Invalid value for `function` ({0}), must be one of {1}"  # noqa: E501
                .format(function, allowed_values)
            )

        self._function = function

    @property
    def encoding_format(self):
        """Gets the encoding_format of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501

        Identifies image format the document is created in, like PDF, TIFF, or ZIP  # noqa: E501

        :return: The encoding_format of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._encoding_format

    @encoding_format.setter
    def encoding_format(self, encoding_format):
        """Sets the encoding_format of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.

        Identifies image format the document is created in, like PDF, TIFF, or ZIP  # noqa: E501

        :param encoding_format: The encoding_format of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :type: str
        """
        if encoding_format is None:
            raise ValueError("Invalid value for `encoding_format`, must not be `None`")  # noqa: E501

        self._encoding_format = encoding_format

    @property
    def content(self):
        """Gets the content of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501

        Contains base64 encoded document image or archived zip  # noqa: E501

        :return: The content of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.

        Contains base64 encoded document image or archived zip  # noqa: E501

        :param content: The content of this SupermodelIoLogisticsExpressDocumentImageResponseDocuments.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

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
        if issubclass(SupermodelIoLogisticsExpressDocumentImageResponseDocuments, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressDocumentImageResponseDocuments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other