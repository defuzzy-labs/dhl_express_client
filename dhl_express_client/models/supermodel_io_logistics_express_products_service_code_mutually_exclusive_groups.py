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

class SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups(object):
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
        'service_code_rule_name': 'str',
        'description': 'str',
        'service_codes': 'list[SupermodelIoLogisticsExpressProductsServiceCodes]'
    }

    attribute_map = {
        'service_code_rule_name': 'serviceCodeRuleName',
        'description': 'description',
        'service_codes': 'serviceCodes'
    }

    def __init__(self, service_code_rule_name=None, description=None, service_codes=None):  # noqa: E501
        """SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups - a model defined in Swagger"""  # noqa: E501
        self._service_code_rule_name = None
        self._description = None
        self._service_codes = None
        self.discriminator = None
        if service_code_rule_name is not None:
            self.service_code_rule_name = service_code_rule_name
        if description is not None:
            self.description = description
        if service_codes is not None:
            self.service_codes = service_codes

    @property
    def service_code_rule_name(self):
        """Gets the service_code_rule_name of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501

        Mutually exclusive serviceCode group name  # noqa: E501

        :return: The service_code_rule_name of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :rtype: str
        """
        return self._service_code_rule_name

    @service_code_rule_name.setter
    def service_code_rule_name(self, service_code_rule_name):
        """Sets the service_code_rule_name of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.

        Mutually exclusive serviceCode group name  # noqa: E501

        :param service_code_rule_name: The service_code_rule_name of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :type: str
        """

        self._service_code_rule_name = service_code_rule_name

    @property
    def description(self):
        """Gets the description of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501

        Mutually exclusive serviceCode group description  # noqa: E501

        :return: The description of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.

        Mutually exclusive serviceCode group description  # noqa: E501

        :param description: The description of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_codes(self):
        """Gets the service_codes of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501


        :return: The service_codes of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsServiceCodes]
        """
        return self._service_codes

    @service_codes.setter
    def service_codes(self, service_codes):
        """Sets the service_codes of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.


        :param service_codes: The service_codes of this SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsServiceCodes]
        """

        self._service_codes = service_codes

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
        if issubclass(SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other