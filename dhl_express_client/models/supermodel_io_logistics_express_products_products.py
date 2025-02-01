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

class SupermodelIoLogisticsExpressProductsProducts(object):
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
        'product_name': 'str',
        'product_code': 'str',
        'local_product_code': 'str',
        'local_product_country_code': 'str',
        'network_type_code': 'str',
        'is_customer_agreement': 'bool',
        'weight': 'Weight',
        'breakdown': 'list[SupermodelIoLogisticsExpressProductsBreakdown]',
        'service_code_mutually_exclusive_groups': 'list[SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups]',
        'service_code_dependency_rule_groups': 'list[SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups]',
        'pickup_capabilities': 'SupermodelIoLogisticsExpressProductsPickupCapabilities',
        'delivery_capabilities': 'SupermodelIoLogisticsExpressProductsDeliveryCapabilities'
    }

    attribute_map = {
        'product_name': 'productName',
        'product_code': 'productCode',
        'local_product_code': 'localProductCode',
        'local_product_country_code': 'localProductCountryCode',
        'network_type_code': 'networkTypeCode',
        'is_customer_agreement': 'isCustomerAgreement',
        'weight': 'weight',
        'breakdown': 'breakdown',
        'service_code_mutually_exclusive_groups': 'serviceCodeMutuallyExclusiveGroups',
        'service_code_dependency_rule_groups': 'serviceCodeDependencyRuleGroups',
        'pickup_capabilities': 'pickupCapabilities',
        'delivery_capabilities': 'deliveryCapabilities'
    }

    def __init__(self, product_name=None, product_code=None, local_product_code=None, local_product_country_code=None, network_type_code=None, is_customer_agreement=None, weight=None, breakdown=None, service_code_mutually_exclusive_groups=None, service_code_dependency_rule_groups=None, pickup_capabilities=None, delivery_capabilities=None):  # noqa: E501
        """SupermodelIoLogisticsExpressProductsProducts - a model defined in Swagger"""  # noqa: E501
        self._product_name = None
        self._product_code = None
        self._local_product_code = None
        self._local_product_country_code = None
        self._network_type_code = None
        self._is_customer_agreement = None
        self._weight = None
        self._breakdown = None
        self._service_code_mutually_exclusive_groups = None
        self._service_code_dependency_rule_groups = None
        self._pickup_capabilities = None
        self._delivery_capabilities = None
        self.discriminator = None
        if product_name is not None:
            self.product_name = product_name
        if product_code is not None:
            self.product_code = product_code
        if local_product_code is not None:
            self.local_product_code = local_product_code
        if local_product_country_code is not None:
            self.local_product_country_code = local_product_country_code
        if network_type_code is not None:
            self.network_type_code = network_type_code
        if is_customer_agreement is not None:
            self.is_customer_agreement = is_customer_agreement
        if weight is not None:
            self.weight = weight
        if breakdown is not None:
            self.breakdown = breakdown
        if service_code_mutually_exclusive_groups is not None:
            self.service_code_mutually_exclusive_groups = service_code_mutually_exclusive_groups
        if service_code_dependency_rule_groups is not None:
            self.service_code_dependency_rule_groups = service_code_dependency_rule_groups
        if pickup_capabilities is not None:
            self.pickup_capabilities = pickup_capabilities
        if delivery_capabilities is not None:
            self.delivery_capabilities = delivery_capabilities

    @property
    def product_name(self):
        """Gets the product_name of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        Name of the DHL Express product  # noqa: E501

        :return: The product_name of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this SupermodelIoLogisticsExpressProductsProducts.

        Name of the DHL Express product  # noqa: E501

        :param product_name: The product_name of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def product_code(self):
        """Gets the product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        This is the global DHL Express product code for which the delivery is feasible respecting the input data from the request.  # noqa: E501

        :return: The product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this SupermodelIoLogisticsExpressProductsProducts.

        This is the global DHL Express product code for which the delivery is feasible respecting the input data from the request.  # noqa: E501

        :param product_code: The product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: str
        """

        self._product_code = product_code

    @property
    def local_product_code(self):
        """Gets the local_product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        This is the local DHL Express product code for which the delivery is feasible respecting the input data from the request.  # noqa: E501

        :return: The local_product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: str
        """
        return self._local_product_code

    @local_product_code.setter
    def local_product_code(self, local_product_code):
        """Sets the local_product_code of this SupermodelIoLogisticsExpressProductsProducts.

        This is the local DHL Express product code for which the delivery is feasible respecting the input data from the request.  # noqa: E501

        :param local_product_code: The local_product_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: str
        """

        self._local_product_code = local_product_code

    @property
    def local_product_country_code(self):
        """Gets the local_product_country_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        The country code for the local service used  # noqa: E501

        :return: The local_product_country_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: str
        """
        return self._local_product_country_code

    @local_product_country_code.setter
    def local_product_country_code(self, local_product_country_code):
        """Sets the local_product_country_code of this SupermodelIoLogisticsExpressProductsProducts.

        The country code for the local service used  # noqa: E501

        :param local_product_country_code: The local_product_country_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: str
        """

        self._local_product_country_code = local_product_country_code

    @property
    def network_type_code(self):
        """Gets the network_type_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        The NetworkTypeCode element indicates the product belongs to the Day Definite (DD) or Time Definite (TD) network.<BR>            Possible Values;<BR>            DD: Day Definite product<BR>            TD: Time Definite product  # noqa: E501

        :return: The network_type_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: str
        """
        return self._network_type_code

    @network_type_code.setter
    def network_type_code(self, network_type_code):
        """Sets the network_type_code of this SupermodelIoLogisticsExpressProductsProducts.

        The NetworkTypeCode element indicates the product belongs to the Day Definite (DD) or Time Definite (TD) network.<BR>            Possible Values;<BR>            DD: Day Definite product<BR>            TD: Time Definite product  # noqa: E501

        :param network_type_code: The network_type_code of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: str
        """

        self._network_type_code = network_type_code

    @property
    def is_customer_agreement(self):
        """Gets the is_customer_agreement of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        Indicator that the product only can be offered to customers with prior agreement.  # noqa: E501

        :return: The is_customer_agreement of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: bool
        """
        return self._is_customer_agreement

    @is_customer_agreement.setter
    def is_customer_agreement(self, is_customer_agreement):
        """Sets the is_customer_agreement of this SupermodelIoLogisticsExpressProductsProducts.

        Indicator that the product only can be offered to customers with prior agreement.  # noqa: E501

        :param is_customer_agreement: The is_customer_agreement of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: bool
        """

        self._is_customer_agreement = is_customer_agreement

    @property
    def weight(self):
        """Gets the weight of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501


        :return: The weight of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: Weight
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SupermodelIoLogisticsExpressProductsProducts.


        :param weight: The weight of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: Weight
        """

        self._weight = weight

    @property
    def breakdown(self):
        """Gets the breakdown of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501


        :return: The breakdown of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsBreakdown]
        """
        return self._breakdown

    @breakdown.setter
    def breakdown(self, breakdown):
        """Sets the breakdown of this SupermodelIoLogisticsExpressProductsProducts.


        :param breakdown: The breakdown of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsBreakdown]
        """

        self._breakdown = breakdown

    @property
    def service_code_mutually_exclusive_groups(self):
        """Gets the service_code_mutually_exclusive_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        Group of serviceCodes that are mutually exclusive.  Only one serviceCode among the list must be applied for a shipment  # noqa: E501

        :return: The service_code_mutually_exclusive_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups]
        """
        return self._service_code_mutually_exclusive_groups

    @service_code_mutually_exclusive_groups.setter
    def service_code_mutually_exclusive_groups(self, service_code_mutually_exclusive_groups):
        """Sets the service_code_mutually_exclusive_groups of this SupermodelIoLogisticsExpressProductsProducts.

        Group of serviceCodes that are mutually exclusive.  Only one serviceCode among the list must be applied for a shipment  # noqa: E501

        :param service_code_mutually_exclusive_groups: The service_code_mutually_exclusive_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups]
        """

        self._service_code_mutually_exclusive_groups = service_code_mutually_exclusive_groups

    @property
    def service_code_dependency_rule_groups(self):
        """Gets the service_code_dependency_rule_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501

        Dependency rule groups for a particular serviceCode.  # noqa: E501

        :return: The service_code_dependency_rule_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups]
        """
        return self._service_code_dependency_rule_groups

    @service_code_dependency_rule_groups.setter
    def service_code_dependency_rule_groups(self, service_code_dependency_rule_groups):
        """Sets the service_code_dependency_rule_groups of this SupermodelIoLogisticsExpressProductsProducts.

        Dependency rule groups for a particular serviceCode.  # noqa: E501

        :param service_code_dependency_rule_groups: The service_code_dependency_rule_groups of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups]
        """

        self._service_code_dependency_rule_groups = service_code_dependency_rule_groups

    @property
    def pickup_capabilities(self):
        """Gets the pickup_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501


        :return: The pickup_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressProductsPickupCapabilities
        """
        return self._pickup_capabilities

    @pickup_capabilities.setter
    def pickup_capabilities(self, pickup_capabilities):
        """Sets the pickup_capabilities of this SupermodelIoLogisticsExpressProductsProducts.


        :param pickup_capabilities: The pickup_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: SupermodelIoLogisticsExpressProductsPickupCapabilities
        """

        self._pickup_capabilities = pickup_capabilities

    @property
    def delivery_capabilities(self):
        """Gets the delivery_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501


        :return: The delivery_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressProductsDeliveryCapabilities
        """
        return self._delivery_capabilities

    @delivery_capabilities.setter
    def delivery_capabilities(self, delivery_capabilities):
        """Sets the delivery_capabilities of this SupermodelIoLogisticsExpressProductsProducts.


        :param delivery_capabilities: The delivery_capabilities of this SupermodelIoLogisticsExpressProductsProducts.  # noqa: E501
        :type: SupermodelIoLogisticsExpressProductsDeliveryCapabilities
        """

        self._delivery_capabilities = delivery_capabilities

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
        if issubclass(SupermodelIoLogisticsExpressProductsProducts, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressProductsProducts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
