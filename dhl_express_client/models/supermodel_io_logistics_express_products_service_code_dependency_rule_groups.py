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

class SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups(object):
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
        'dependent_service_code': 'str',
        'dependency_rule_group': 'list[SupermodelIoLogisticsExpressProductsDependencyRuleGroup]'
    }

    attribute_map = {
        'dependent_service_code': 'dependentServiceCode',
        'dependency_rule_group': 'dependencyRuleGroup'
    }

    def __init__(self, dependent_service_code=None, dependency_rule_group=None):  # noqa: E501
        """SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups - a model defined in Swagger"""  # noqa: E501
        self._dependent_service_code = None
        self._dependency_rule_group = None
        self.discriminator = None
        if dependent_service_code is not None:
            self.dependent_service_code = dependent_service_code
        if dependency_rule_group is not None:
            self.dependency_rule_group = dependency_rule_group

    @property
    def dependent_service_code(self):
        """Gets the dependent_service_code of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501

        Dependent special service charge code where the rule groups are applied  # noqa: E501

        :return: The dependent_service_code of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501
        :rtype: str
        """
        return self._dependent_service_code

    @dependent_service_code.setter
    def dependent_service_code(self, dependent_service_code):
        """Sets the dependent_service_code of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.

        Dependent special service charge code where the rule groups are applied  # noqa: E501

        :param dependent_service_code: The dependent_service_code of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501
        :type: str
        """

        self._dependent_service_code = dependent_service_code

    @property
    def dependency_rule_group(self):
        """Gets the dependency_rule_group of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501


        :return: The dependency_rule_group of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsDependencyRuleGroup]
        """
        return self._dependency_rule_group

    @dependency_rule_group.setter
    def dependency_rule_group(self, dependency_rule_group):
        """Sets the dependency_rule_group of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.


        :param dependency_rule_group: The dependency_rule_group of this SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsDependencyRuleGroup]
        """

        self._dependency_rule_group = dependency_rule_group

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
        if issubclass(SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
