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

class SupermodelIoLogisticsExpressRatesBreakdown1(object):
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
        'name': 'str',
        'service_code': 'str',
        'local_service_code': 'str',
        'type_code': 'str',
        'service_type_code': 'str',
        'price': 'float',
        'price_currency': 'str',
        'is_customer_agreement': 'bool',
        'is_marketed_service': 'bool',
        'is_billing_service_indicator': 'bool',
        'price_breakdown': 'list[SupermodelIoLogisticsExpressRatesPriceBreakdown2]',
        'tariff_rate_formula': 'str'
    }

    attribute_map = {
        'name': 'name',
        'service_code': 'serviceCode',
        'local_service_code': 'localServiceCode',
        'type_code': 'typeCode',
        'service_type_code': 'serviceTypeCode',
        'price': 'price',
        'price_currency': 'priceCurrency',
        'is_customer_agreement': 'isCustomerAgreement',
        'is_marketed_service': 'isMarketedService',
        'is_billing_service_indicator': 'isBillingServiceIndicator',
        'price_breakdown': 'priceBreakdown',
        'tariff_rate_formula': 'tariffRateFormula'
    }

    def __init__(self, name=None, service_code=None, local_service_code=None, type_code=None, service_type_code=None, price=None, price_currency=None, is_customer_agreement=None, is_marketed_service=None, is_billing_service_indicator=None, price_breakdown=None, tariff_rate_formula=None):  # noqa: E501
        """SupermodelIoLogisticsExpressRatesBreakdown1 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._service_code = None
        self._local_service_code = None
        self._type_code = None
        self._service_type_code = None
        self._price = None
        self._price_currency = None
        self._is_customer_agreement = None
        self._is_marketed_service = None
        self._is_billing_service_indicator = None
        self._price_breakdown = None
        self._tariff_rate_formula = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if service_code is not None:
            self.service_code = service_code
        if local_service_code is not None:
            self.local_service_code = local_service_code
        self.type_code = type_code
        if service_type_code is not None:
            self.service_type_code = service_type_code
        self.price = price
        if price_currency is not None:
            self.price_currency = price_currency
        if is_customer_agreement is not None:
            self.is_customer_agreement = is_customer_agreement
        if is_marketed_service is not None:
            self.is_marketed_service = is_marketed_service
        if is_billing_service_indicator is not None:
            self.is_billing_service_indicator = is_billing_service_indicator
        if price_breakdown is not None:
            self.price_breakdown = price_breakdown
        if tariff_rate_formula is not None:
            self.tariff_rate_formula = tariff_rate_formula

    @property
    def name(self):
        """Gets the name of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Name of the charge  # noqa: E501

        :return: The name of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Name of the charge  # noqa: E501

        :param name: The name of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def service_code(self):
        """Gets the service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Special service or extra charge code. This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery  # noqa: E501

        :return: The service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._service_code

    @service_code.setter
    def service_code(self, service_code):
        """Sets the service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Special service or extra charge code. This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery  # noqa: E501

        :param service_code: The service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._service_code = service_code

    @property
    def local_service_code(self):
        """Gets the local_service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Local service code  # noqa: E501

        :return: The local_service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._local_service_code

    @local_service_code.setter
    def local_service_code(self, local_service_code):
        """Sets the local_service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Local service code  # noqa: E501

        :param local_service_code: The local_service_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._local_service_code = local_service_code

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Charge type or category.<BR>                        Possible values;<BR>                        - DUTY<BR>                        - TAX<BR>                        - FEE  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Charge type or category.<BR>                        Possible values;<BR>                        - DUTY<BR>                        - TAX<BR>                        - FEE  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501

        self._type_code = type_code

    @property
    def service_type_code(self):
        """Gets the service_type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Special service charge code type for service. XCH type charge codes are Optional Services and should be displayed to users for selection.<BR>                        The possible values are;<BR>                        - XCH = Extra charge<BR>                        - FEE = Fee<BR>                        - SCH = Surcharge<BR>                        - NRI = Non Revenue Item<BR>                        Other charges may be automatically returned when applicable.  # noqa: E501

        :return: The service_type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Special service charge code type for service. XCH type charge codes are Optional Services and should be displayed to users for selection.<BR>                        The possible values are;<BR>                        - XCH = Extra charge<BR>                        - FEE = Fee<BR>                        - SCH = Surcharge<BR>                        - NRI = Non Revenue Item<BR>                        Other charges may be automatically returned when applicable.  # noqa: E501

        :param service_type_code: The service_type_code of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._service_type_code = service_type_code

    @property
    def price(self):
        """Gets the price of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        The charge amount of the line item charge.  # noqa: E501

        :return: The price of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SupermodelIoLogisticsExpressRatesBreakdown1.

        The charge amount of the line item charge.  # noqa: E501

        :param price: The price of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def price_currency(self):
        """Gets the price_currency of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        This the currency of the rated shipment for the prices listed.  # noqa: E501

        :return: The price_currency of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._price_currency

    @price_currency.setter
    def price_currency(self, price_currency):
        """Sets the price_currency of this SupermodelIoLogisticsExpressRatesBreakdown1.

        This the currency of the rated shipment for the prices listed.  # noqa: E501

        :param price_currency: The price_currency of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._price_currency = price_currency

    @property
    def is_customer_agreement(self):
        """Gets the is_customer_agreement of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Customer agreement indicator for product and services, if service is offered with prior customer agreement  # noqa: E501

        :return: The is_customer_agreement of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: bool
        """
        return self._is_customer_agreement

    @is_customer_agreement.setter
    def is_customer_agreement(self, is_customer_agreement):
        """Sets the is_customer_agreement of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Customer agreement indicator for product and services, if service is offered with prior customer agreement  # noqa: E501

        :param is_customer_agreement: The is_customer_agreement of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: bool
        """

        self._is_customer_agreement = is_customer_agreement

    @property
    def is_marketed_service(self):
        """Gets the is_marketed_service of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Indicator if the special service is marketed service  # noqa: E501

        :return: The is_marketed_service of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: bool
        """
        return self._is_marketed_service

    @is_marketed_service.setter
    def is_marketed_service(self, is_marketed_service):
        """Sets the is_marketed_service of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Indicator if the special service is marketed service  # noqa: E501

        :param is_marketed_service: The is_marketed_service of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: bool
        """

        self._is_marketed_service = is_marketed_service

    @property
    def is_billing_service_indicator(self):
        """Gets the is_billing_service_indicator of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Indicator if there is any discount allowed  # noqa: E501

        :return: The is_billing_service_indicator of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: bool
        """
        return self._is_billing_service_indicator

    @is_billing_service_indicator.setter
    def is_billing_service_indicator(self, is_billing_service_indicator):
        """Sets the is_billing_service_indicator of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Indicator if there is any discount allowed  # noqa: E501

        :param is_billing_service_indicator: The is_billing_service_indicator of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: bool
        """

        self._is_billing_service_indicator = is_billing_service_indicator

    @property
    def price_breakdown(self):
        """Gets the price_breakdown of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501


        :return: The price_breakdown of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressRatesPriceBreakdown2]
        """
        return self._price_breakdown

    @price_breakdown.setter
    def price_breakdown(self, price_breakdown):
        """Sets the price_breakdown of this SupermodelIoLogisticsExpressRatesBreakdown1.


        :param price_breakdown: The price_breakdown of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressRatesPriceBreakdown2]
        """

        self._price_breakdown = price_breakdown

    @property
    def tariff_rate_formula(self):
        """Gets the tariff_rate_formula of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501

        Tariff Rate Formula on Line Item Level  # noqa: E501

        :return: The tariff_rate_formula of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :rtype: str
        """
        return self._tariff_rate_formula

    @tariff_rate_formula.setter
    def tariff_rate_formula(self, tariff_rate_formula):
        """Sets the tariff_rate_formula of this SupermodelIoLogisticsExpressRatesBreakdown1.

        Tariff Rate Formula on Line Item Level  # noqa: E501

        :param tariff_rate_formula: The tariff_rate_formula of this SupermodelIoLogisticsExpressRatesBreakdown1.  # noqa: E501
        :type: str
        """

        self._tariff_rate_formula = tariff_rate_formula

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
        if issubclass(SupermodelIoLogisticsExpressRatesBreakdown1, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressRatesBreakdown1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
