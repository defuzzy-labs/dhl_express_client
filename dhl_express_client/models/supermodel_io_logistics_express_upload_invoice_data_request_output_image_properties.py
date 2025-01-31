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

class SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties(object):
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
        'image_options': 'list[SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptions]'
    }

    attribute_map = {
        'image_options': 'imageOptions'
    }

    def __init__(self, image_options=None):  # noqa: E501
        """SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties - a model defined in Swagger"""  # noqa: E501
        self._image_options = None
        self.discriminator = None
        if image_options is not None:
            self.image_options = image_options

    @property
    def image_options(self):
        """Gets the image_options of this SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.  # noqa: E501

        Here the image options are defined for label, waybillDoc, invoice, receipt and QRcode  # noqa: E501

        :return: The image_options of this SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptions]
        """
        return self._image_options

    @image_options.setter
    def image_options(self, image_options):
        """Sets the image_options of this SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.

        Here the image options are defined for label, waybillDoc, invoice, receipt and QRcode  # noqa: E501

        :param image_options: The image_options of this SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImagePropertiesImageOptions]
        """

        self._image_options = image_options

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
        if issubclass(SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
