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

class Weight1(object):
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
        'volumetric': 'float',
        'provided': 'float',
        'unit_of_measurement': 'str'
    }

    attribute_map = {
        'volumetric': 'volumetric',
        'provided': 'provided',
        'unit_of_measurement': 'unitOfMeasurement'
    }

    def __init__(self, volumetric=None, provided=None, unit_of_measurement=None):  # noqa: E501
        """Weight1 - a model defined in Swagger"""  # noqa: E501
        self._volumetric = None
        self._provided = None
        self._unit_of_measurement = None
        self.discriminator = None
        if volumetric is not None:
            self.volumetric = volumetric
        if provided is not None:
            self.provided = provided
        if unit_of_measurement is not None:
            self.unit_of_measurement = unit_of_measurement

    @property
    def volumetric(self):
        """Gets the volumetric of this Weight1.  # noqa: E501

        The dimensional weight of the shipment  # noqa: E501

        :return: The volumetric of this Weight1.  # noqa: E501
        :rtype: float
        """
        return self._volumetric

    @volumetric.setter
    def volumetric(self, volumetric):
        """Sets the volumetric of this Weight1.

        The dimensional weight of the shipment  # noqa: E501

        :param volumetric: The volumetric of this Weight1.  # noqa: E501
        :type: float
        """

        self._volumetric = volumetric

    @property
    def provided(self):
        """Gets the provided of this Weight1.  # noqa: E501

        The quoted weight of the shipment  # noqa: E501

        :return: The provided of this Weight1.  # noqa: E501
        :rtype: float
        """
        return self._provided

    @provided.setter
    def provided(self, provided):
        """Sets the provided of this Weight1.

        The quoted weight of the shipment  # noqa: E501

        :param provided: The provided of this Weight1.  # noqa: E501
        :type: float
        """

        self._provided = provided

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this Weight1.  # noqa: E501

        The unit of measurement for the dimensions of the package.  # noqa: E501

        :return: The unit_of_measurement of this Weight1.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this Weight1.

        The unit of measurement for the dimensions of the package.  # noqa: E501

        :param unit_of_measurement: The unit_of_measurement of this Weight1.  # noqa: E501
        :type: str
        """

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
        if issubclass(Weight1, dict):
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
        if not isinstance(other, Weight1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
