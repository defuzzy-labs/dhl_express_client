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

class SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails(object):
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
        'product_code': 'str',
        'local_product_code': 'str',
        'accounts': 'list[SupermodelIoLogisticsExpressAccount]',
        'value_added_services': 'list[SupermodelIoLogisticsExpressValueAddedServicesRates]',
        'is_customs_declarable': 'bool',
        'declared_value': 'float',
        'declared_value_currency': 'str',
        'unit_of_measurement': 'str',
        'shipment_tracking_number': 'str',
        'packages': 'list[SupermodelIoLogisticsExpressPackageRR]'
    }

    attribute_map = {
        'product_code': 'productCode',
        'local_product_code': 'localProductCode',
        'accounts': 'accounts',
        'value_added_services': 'valueAddedServices',
        'is_customs_declarable': 'isCustomsDeclarable',
        'declared_value': 'declaredValue',
        'declared_value_currency': 'declaredValueCurrency',
        'unit_of_measurement': 'unitOfMeasurement',
        'shipment_tracking_number': 'shipmentTrackingNumber',
        'packages': 'packages'
    }

    def __init__(self, product_code=None, local_product_code=None, accounts=None, value_added_services=None, is_customs_declarable=None, declared_value=None, declared_value_currency=None, unit_of_measurement=None, shipment_tracking_number=None, packages=None):  # noqa: E501
        """SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails - a model defined in Swagger"""  # noqa: E501
        self._product_code = None
        self._local_product_code = None
        self._accounts = None
        self._value_added_services = None
        self._is_customs_declarable = None
        self._declared_value = None
        self._declared_value_currency = None
        self._unit_of_measurement = None
        self._shipment_tracking_number = None
        self._packages = None
        self.discriminator = None
        self.product_code = product_code
        if local_product_code is not None:
            self.local_product_code = local_product_code
        if accounts is not None:
            self.accounts = accounts
        if value_added_services is not None:
            self.value_added_services = value_added_services
        self.is_customs_declarable = is_customs_declarable
        if declared_value is not None:
            self.declared_value = declared_value
        if declared_value_currency is not None:
            self.declared_value_currency = declared_value_currency
        self.unit_of_measurement = unit_of_measurement
        if shipment_tracking_number is not None:
            self.shipment_tracking_number = shipment_tracking_number
        self.packages = packages

    @property
    def product_code(self):
        """Gets the product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        Please provide DHL Express Global product code of the shipment  # noqa: E501

        :return: The product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        Please provide DHL Express Global product code of the shipment  # noqa: E501

        :param product_code: The product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: str
        """
        if product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def local_product_code(self):
        """Gets the local_product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        Please provide DHL Express Local product code of the shipment  # noqa: E501

        :return: The local_product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._local_product_code

    @local_product_code.setter
    def local_product_code(self, local_product_code):
        """Sets the local_product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        Please provide DHL Express Local product code of the shipment  # noqa: E501

        :param local_product_code: The local_product_code of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: str
        """

        self._local_product_code = local_product_code

    @property
    def accounts(self):
        """Gets the accounts of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501


        :return: The accounts of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.


        :param accounts: The accounts of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressAccount]
        """

        self._accounts = accounts

    @property
    def value_added_services(self):
        """Gets the value_added_services of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501


        :return: The value_added_services of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressValueAddedServicesRates]
        """
        return self._value_added_services

    @value_added_services.setter
    def value_added_services(self, value_added_services):
        """Sets the value_added_services of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.


        :param value_added_services: The value_added_services of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressValueAddedServicesRates]
        """

        self._value_added_services = value_added_services

    @property
    def is_customs_declarable(self):
        """Gets the is_customs_declarable of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false)  # noqa: E501

        :return: The is_customs_declarable of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_customs_declarable

    @is_customs_declarable.setter
    def is_customs_declarable(self, is_customs_declarable):
        """Sets the is_customs_declarable of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false)  # noqa: E501

        :param is_customs_declarable: The is_customs_declarable of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: bool
        """
        if is_customs_declarable is None:
            raise ValueError("Invalid value for `is_customs_declarable`, must not be `None`")  # noqa: E501

        self._is_customs_declarable = is_customs_declarable

    @property
    def declared_value(self):
        """Gets the declared_value of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        For customs purposes please advise on declared value of the shipment  # noqa: E501

        :return: The declared_value of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: float
        """
        return self._declared_value

    @declared_value.setter
    def declared_value(self, declared_value):
        """Sets the declared_value of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        For customs purposes please advise on declared value of the shipment  # noqa: E501

        :param declared_value: The declared_value of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: float
        """

        self._declared_value = declared_value

    @property
    def declared_value_currency(self):
        """Gets the declared_value_currency of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        For customs purposes please advise on declared value currency code of the shipment  # noqa: E501

        :return: The declared_value_currency of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._declared_value_currency

    @declared_value_currency.setter
    def declared_value_currency(self, declared_value_currency):
        """Sets the declared_value_currency of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        For customs purposes please advise on declared value currency code of the shipment  # noqa: E501

        :param declared_value_currency: The declared_value_currency of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: str
        """

        self._declared_value_currency = declared_value_currency

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        Please enter Unit of measurement - metric,imperial  # noqa: E501

        :return: The unit_of_measurement of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        Please enter Unit of measurement - metric,imperial  # noqa: E501

        :param unit_of_measurement: The unit_of_measurement of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: str
        """
        if unit_of_measurement is None:
            raise ValueError("Invalid value for `unit_of_measurement`, must not be `None`")  # noqa: E501
        allowed_values = ["metric", "imperial"]  # noqa: E501
        if unit_of_measurement not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_of_measurement` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_of_measurement, allowed_values)
            )

        self._unit_of_measurement = unit_of_measurement

    @property
    def shipment_tracking_number(self):
        """Gets the shipment_tracking_number of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501

        Please provide Shipment Identification number (AWB number)  # noqa: E501

        :return: The shipment_tracking_number of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._shipment_tracking_number

    @shipment_tracking_number.setter
    def shipment_tracking_number(self, shipment_tracking_number):
        """Sets the shipment_tracking_number of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.

        Please provide Shipment Identification number (AWB number)  # noqa: E501

        :param shipment_tracking_number: The shipment_tracking_number of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: str
        """

        self._shipment_tracking_number = shipment_tracking_number

    @property
    def packages(self):
        """Gets the packages of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501


        :return: The packages of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressPackageRR]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.


        :param packages: The packages of this SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressPackageRR]
        """
        if packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

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
        if issubclass(SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
