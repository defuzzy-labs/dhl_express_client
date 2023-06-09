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

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity(object):
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
        'value': 'int',
        'unit_of_measurement': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit_of_measurement': 'unitOfMeasurement'
    }

    def __init__(self, value=None, unit_of_measurement=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._unit_of_measurement = None
        self.discriminator = None
        self.value = value
        self.unit_of_measurement = unit_of_measurement

    @property
    def value(self):
        """Gets the value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501

        Please enter number of pieces in the line item  # noqa: E501

        :return: The value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.

        Please enter number of pieces in the line item  # noqa: E501

        :param value: The value of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501

        Please provide correct unit of measurement<BR>                        <BR>                        Possible values;<BR>                        BOX Boxes<BR>                        2GM                               Centimeters<BR>                        2M3 Cubic Centimeters<BR>                        3M3 Cubic Feet<BR>                        M3 Cubic Meters<BR>                        DPR Dozen Pairs<BR>                        DOZ Dozen<BR>                        2NO Each<BR>                        PCS Pieces<BR>                        GM Grams<BR>                        GRS Gross<BR>                        KG Kilograms<BR>                        L Liters<BR>                        M Meters<BR>                        3GM Milligrams<BR>                        3L Milliliters<BR>                        X No Unit Required<BR>                        NO Number<BR>                        2KG Ounces<BR>                        PRS Pairs<BR>                        2L Gallons<BR>                        3KG Pounds<BR>                        CM2 Square Centimeters<BR>                        2M2 Square Feet<BR>                        3M2 Square Inches<BR>                        M2 Square Meters<BR>                        4M2 Square Yards<BR>                        3M Yards<BR>                        CM Centimeters<BR>                        CONE Cone<BR>                        CT Carat<BR>                        EA Each<BR>                        LBS Pounds<BR>                        RILL Rill<BR>                        ROLL Roll<BR>                        SET Set<BR>                        TU Time Unit<BR>                        YDS Yard  # noqa: E501

        :return: The unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.

        Please provide correct unit of measurement<BR>                        <BR>                        Possible values;<BR>                        BOX Boxes<BR>                        2GM                               Centimeters<BR>                        2M3 Cubic Centimeters<BR>                        3M3 Cubic Feet<BR>                        M3 Cubic Meters<BR>                        DPR Dozen Pairs<BR>                        DOZ Dozen<BR>                        2NO Each<BR>                        PCS Pieces<BR>                        GM Grams<BR>                        GRS Gross<BR>                        KG Kilograms<BR>                        L Liters<BR>                        M Meters<BR>                        3GM Milligrams<BR>                        3L Milliliters<BR>                        X No Unit Required<BR>                        NO Number<BR>                        2KG Ounces<BR>                        PRS Pairs<BR>                        2L Gallons<BR>                        3KG Pounds<BR>                        CM2 Square Centimeters<BR>                        2M2 Square Feet<BR>                        3M2 Square Inches<BR>                        M2 Square Meters<BR>                        4M2 Square Yards<BR>                        3M Yards<BR>                        CM Centimeters<BR>                        CONE Cone<BR>                        CT Carat<BR>                        EA Each<BR>                        LBS Pounds<BR>                        RILL Rill<BR>                        ROLL Roll<BR>                        SET Set<BR>                        TU Time Unit<BR>                        YDS Yard  # noqa: E501

        :param unit_of_measurement: The unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.  # noqa: E501
        :type: str
        """
        if unit_of_measurement is None:
            raise ValueError("Invalid value for `unit_of_measurement`, must not be `None`")  # noqa: E501
        allowed_values = ["BOX", "2GM", "2M3", "3M3", "M3", "DPR", "DOZ", "2NO", "PCS", "GM", "GRS", "KG", "L", "M", "3GM", "3L", "X", "NO", "2KG", "PRS", "2L", "3KG", "CM2", "2M2", "3M2", "M2", "4M2", "3M", "CM", "CONE", "CT", "EA", "LBS", "RILL", "ROLL", "SET", "TU", "YDS"]  # noqa: E501
        if unit_of_measurement not in allowed_values:
            raise ValueError(
                "Invalid value for `unit_of_measurement` ({0}), must be one of {1}"  # noqa: E501
                .format(unit_of_measurement, allowed_values)
            )

        self._unit_of_measurement = unit_of_measurement

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
