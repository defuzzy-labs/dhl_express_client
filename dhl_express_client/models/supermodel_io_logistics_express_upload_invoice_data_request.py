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

class SupermodelIoLogisticsExpressUploadInvoiceDataRequest(object):
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
        'planned_ship_date': 'str',
        'accounts': 'list[SupermodelIoLogisticsExpressAccount]',
        'content': 'SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent',
        'output_image_properties': 'SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties',
        'customer_details': 'SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails'
    }

    attribute_map = {
        'planned_ship_date': 'plannedShipDate',
        'accounts': 'accounts',
        'content': 'content',
        'output_image_properties': 'outputImageProperties',
        'customer_details': 'customerDetails'
    }

    def __init__(self, planned_ship_date=None, accounts=None, content=None, output_image_properties=None, customer_details=None):  # noqa: E501
        """SupermodelIoLogisticsExpressUploadInvoiceDataRequest - a model defined in Swagger"""  # noqa: E501
        self._planned_ship_date = None
        self._accounts = None
        self._content = None
        self._output_image_properties = None
        self._customer_details = None
        self.discriminator = None
        if planned_ship_date is not None:
            self.planned_ship_date = planned_ship_date
        if accounts is not None:
            self.accounts = accounts
        self.content = content
        if output_image_properties is not None:
            self.output_image_properties = output_image_properties
        if customer_details is not None:
            self.customer_details = customer_details

    @property
    def planned_ship_date(self):
        """Gets the planned_ship_date of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501

        The planned shipment date for the provided shipmentTrackingNumber.  The date must be in the format: YYYY-MM-DD  # noqa: E501

        :return: The planned_ship_date of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._planned_ship_date

    @planned_ship_date.setter
    def planned_ship_date(self, planned_ship_date):
        """Sets the planned_ship_date of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.

        The planned shipment date for the provided shipmentTrackingNumber.  The date must be in the format: YYYY-MM-DD  # noqa: E501

        :param planned_ship_date: The planned_ship_date of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :type: str
        """

        self._planned_ship_date = planned_ship_date

    @property
    def accounts(self):
        """Gets the accounts of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501

        Please enter all the DHL Express accounts and types to be used for this shipment.   Note: accounts/0/number with typeCode 'shipper' is mandatory if using POST method and no shipmentTrackingNumber is provided in request.  # noqa: E501

        :return: The accounts of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.

        Please enter all the DHL Express accounts and types to be used for this shipment.   Note: accounts/0/number with typeCode 'shipper' is mandatory if using POST method and no shipmentTrackingNumber is provided in request.  # noqa: E501

        :param accounts: The accounts of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressAccount]
        """

        self._accounts = accounts

    @property
    def content(self):
        """Gets the content of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501


        :return: The content of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.


        :param content: The content of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :type: SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def output_image_properties(self):
        """Gets the output_image_properties of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501


        :return: The output_image_properties of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties
        """
        return self._output_image_properties

    @output_image_properties.setter
    def output_image_properties(self, output_image_properties):
        """Sets the output_image_properties of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.


        :param output_image_properties: The output_image_properties of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :type: SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties
        """

        self._output_image_properties = output_image_properties

    @property
    def customer_details(self):
        """Gets the customer_details of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501


        :return: The customer_details of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails
        """
        return self._customer_details

    @customer_details.setter
    def customer_details(self, customer_details):
        """Sets the customer_details of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.


        :param customer_details: The customer_details of this SupermodelIoLogisticsExpressUploadInvoiceDataRequest.  # noqa: E501
        :type: SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails
        """

        self._customer_details = customer_details

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
        if issubclass(SupermodelIoLogisticsExpressUploadInvoiceDataRequest, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressUploadInvoiceDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
