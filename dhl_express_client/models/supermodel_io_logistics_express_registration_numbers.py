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

class SupermodelIoLogisticsExpressRegistrationNumbers(object):
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
        'type_code': 'str',
        'number': 'str',
        'issuer_country_code': 'str'
    }

    attribute_map = {
        'type_code': 'typeCode',
        'number': 'number',
        'issuer_country_code': 'issuerCountryCode'
    }

    def __init__(self, type_code='VAT', number=None, issuer_country_code=None):  # noqa: E501
        """SupermodelIoLogisticsExpressRegistrationNumbers - a model defined in Swagger"""  # noqa: E501
        self._type_code = None
        self._number = None
        self._issuer_country_code = None
        self.discriminator = None
        self.type_code = type_code
        self.number = number
        self.issuer_country_code = issuer_country_code

    @property
    def type_code(self):
        """Gets the type_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501

        VAT, Value-Added tax<BR>      EIN, Employer Identification Number<BR>      GST, Goods and Service Tax<BR>      SSN, Social Security Number<BR>      EOR, European Union Registration and Identification<BR>      DUN, Data Universal Numberin System<BR>      FED, Federal Tax ID<BR>      STA, State Tax ID<BR>      CNP, Brazil CNPJ/CPF Federal Tax<BR>      IE, Brazil type IE/RG Federal Tax<BR>      INN, Russia bank details section INN<BR>      KPP, Russia bank details section KPP<BR>      OGR, Russia bank details section OGRN<BR>      OKP, Russia bank details sectionOKPO<BR>      SDT, Overseas Registered Supplier or Import One-Stop-Shop or GB VAT (foreign) registration or AUSid GST Registration or VAT on E-Commerce<BR>      FTZ, Free Trade Zone ID<BR>      DAN, Deferment Account Duties Only<BR>      TAN, Deferment Account Tax Only<BR>      DTF, Deferment Account Duties, Taxes and Fees Only<BR>      RGP, EU Registered Exporters registration ID<BR>       DLI,Driver's License <BR>      NID,National Identity Card<BR>      ,PAS:Passport<BR>      ,MID:Manufacturer ID  # noqa: E501

        :return: The type_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this SupermodelIoLogisticsExpressRegistrationNumbers.

        VAT, Value-Added tax<BR>      EIN, Employer Identification Number<BR>      GST, Goods and Service Tax<BR>      SSN, Social Security Number<BR>      EOR, European Union Registration and Identification<BR>      DUN, Data Universal Numberin System<BR>      FED, Federal Tax ID<BR>      STA, State Tax ID<BR>      CNP, Brazil CNPJ/CPF Federal Tax<BR>      IE, Brazil type IE/RG Federal Tax<BR>      INN, Russia bank details section INN<BR>      KPP, Russia bank details section KPP<BR>      OGR, Russia bank details section OGRN<BR>      OKP, Russia bank details sectionOKPO<BR>      SDT, Overseas Registered Supplier or Import One-Stop-Shop or GB VAT (foreign) registration or AUSid GST Registration or VAT on E-Commerce<BR>      FTZ, Free Trade Zone ID<BR>      DAN, Deferment Account Duties Only<BR>      TAN, Deferment Account Tax Only<BR>      DTF, Deferment Account Duties, Taxes and Fees Only<BR>      RGP, EU Registered Exporters registration ID<BR>       DLI,Driver's License <BR>      NID,National Identity Card<BR>      ,PAS:Passport<BR>      ,MID:Manufacturer ID  # noqa: E501

        :param type_code: The type_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :type: str
        """
        if type_code is None:
            raise ValueError("Invalid value for `type_code`, must not be `None`")  # noqa: E501
        allowed_values = ["VAT", "EIN", "GST", "SSN", "EOR", "DUN", "FED", "STA", "CNP", "IE", "INN", "KPP", "OGR", "OKP", "MRN", "SDT", "FTZ", "DAN", "TAN", "DTF", "RGP", "DLI", "NID", "PAS", "MID"]  # noqa: E501
        if type_code not in allowed_values:
            raise ValueError(
                "Invalid value for `type_code` ({0}), must be one of {1}"  # noqa: E501
                .format(type_code, allowed_values)
            )

        self._type_code = type_code

    @property
    def number(self):
        """Gets the number of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501

        Please enter registration number  # noqa: E501

        :return: The number of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SupermodelIoLogisticsExpressRegistrationNumbers.

        Please enter registration number  # noqa: E501

        :param number: The number of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def issuer_country_code(self):
        """Gets the issuer_country_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501

        Please enter 2 character code of the country where the Registration Number has been issued by  # noqa: E501

        :return: The issuer_country_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :rtype: str
        """
        return self._issuer_country_code

    @issuer_country_code.setter
    def issuer_country_code(self, issuer_country_code):
        """Sets the issuer_country_code of this SupermodelIoLogisticsExpressRegistrationNumbers.

        Please enter 2 character code of the country where the Registration Number has been issued by  # noqa: E501

        :param issuer_country_code: The issuer_country_code of this SupermodelIoLogisticsExpressRegistrationNumbers.  # noqa: E501
        :type: str
        """
        if issuer_country_code is None:
            raise ValueError("Invalid value for `issuer_country_code`, must not be `None`")  # noqa: E501

        self._issuer_country_code = issuer_country_code

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
        if issubclass(SupermodelIoLogisticsExpressRegistrationNumbers, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressRegistrationNumbers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
