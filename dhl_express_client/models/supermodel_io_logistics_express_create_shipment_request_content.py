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

class SupermodelIoLogisticsExpressCreateShipmentRequestContent(object):
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
        'packages': 'list[SupermodelIoLogisticsExpressPackage]',
        'is_customs_declarable': 'bool',
        'declared_value': 'float',
        'declared_value_currency': 'str',
        'export_declaration': 'SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration',
        'description': 'str',
        'us_filing_type_value': 'str',
        'incoterm': 'str',
        'unit_of_measurement': 'str'
    }

    attribute_map = {
        'packages': 'packages',
        'is_customs_declarable': 'isCustomsDeclarable',
        'declared_value': 'declaredValue',
        'declared_value_currency': 'declaredValueCurrency',
        'export_declaration': 'exportDeclaration',
        'description': 'description',
        'us_filing_type_value': 'USFilingTypeValue',
        'incoterm': 'incoterm',
        'unit_of_measurement': 'unitOfMeasurement'
    }

    def __init__(self, packages=None, is_customs_declarable=None, declared_value=None, declared_value_currency=None, export_declaration=None, description=None, us_filing_type_value=None, incoterm=None, unit_of_measurement=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestContent - a model defined in Swagger"""  # noqa: E501
        self._packages = None
        self._is_customs_declarable = None
        self._declared_value = None
        self._declared_value_currency = None
        self._export_declaration = None
        self._description = None
        self._us_filing_type_value = None
        self._incoterm = None
        self._unit_of_measurement = None
        self.discriminator = None
        self.packages = packages
        self.is_customs_declarable = is_customs_declarable
        if declared_value is not None:
            self.declared_value = declared_value
        if declared_value_currency is not None:
            self.declared_value_currency = declared_value_currency
        if export_declaration is not None:
            self.export_declaration = export_declaration
        self.description = description
        if us_filing_type_value is not None:
            self.us_filing_type_value = us_filing_type_value
        self.incoterm = incoterm
        self.unit_of_measurement = unit_of_measurement

    @property
    def packages(self):
        """Gets the packages of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        Here you can define properties per package  # noqa: E501

        :return: The packages of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressPackage]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        Here you can define properties per package  # noqa: E501

        :param packages: The packages of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressPackage]
        """
        if packages is None:
            raise ValueError("Invalid value for `packages`, must not be `None`")  # noqa: E501

        self._packages = packages

    @property
    def is_customs_declarable(self):
        """Gets the is_customs_declarable of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false).Note:If the shipment is dutiable, exportDeclaration element must be provided.  # noqa: E501

        :return: The is_customs_declarable of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: bool
        """
        return self._is_customs_declarable

    @is_customs_declarable.setter
    def is_customs_declarable(self, is_customs_declarable):
        """Sets the is_customs_declarable of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false).Note:If the shipment is dutiable, exportDeclaration element must be provided.  # noqa: E501

        :param is_customs_declarable: The is_customs_declarable of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: bool
        """
        if is_customs_declarable is None:
            raise ValueError("Invalid value for `is_customs_declarable`, must not be `None`")  # noqa: E501

        self._is_customs_declarable = is_customs_declarable

    @property
    def declared_value(self):
        """Gets the declared_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        For customs purposes please advise on declared value of the shipment  # noqa: E501

        :return: The declared_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: float
        """
        return self._declared_value

    @declared_value.setter
    def declared_value(self, declared_value):
        """Sets the declared_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        For customs purposes please advise on declared value of the shipment  # noqa: E501

        :param declared_value: The declared_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: float
        """

        self._declared_value = declared_value

    @property
    def declared_value_currency(self):
        """Gets the declared_value_currency of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        For customs purposes please advise on declared value currency code of the shipment  # noqa: E501

        :return: The declared_value_currency of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: str
        """
        return self._declared_value_currency

    @declared_value_currency.setter
    def declared_value_currency(self, declared_value_currency):
        """Sets the declared_value_currency of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        For customs purposes please advise on declared value currency code of the shipment  # noqa: E501

        :param declared_value_currency: The declared_value_currency of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: str
        """

        self._declared_value_currency = declared_value_currency

    @property
    def export_declaration(self):
        """Gets the export_declaration of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501


        :return: The export_declaration of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration
        """
        return self._export_declaration

    @export_declaration.setter
    def export_declaration(self, export_declaration):
        """Sets the export_declaration of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.


        :param export_declaration: The export_declaration of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration
        """

        self._export_declaration = export_declaration

    @property
    def description(self):
        """Gets the description of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        Please enter description of your shipment  # noqa: E501

        :return: The description of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        Please enter description of your shipment  # noqa: E501

        :param description: The description of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def us_filing_type_value(self):
        """Gets the us_filing_type_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        This is used for the US AES4, FTR and ITN numbers to be printed on the Transport Label  # noqa: E501

        :return: The us_filing_type_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: str
        """
        return self._us_filing_type_value

    @us_filing_type_value.setter
    def us_filing_type_value(self, us_filing_type_value):
        """Sets the us_filing_type_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        This is used for the US AES4, FTR and ITN numbers to be printed on the Transport Label  # noqa: E501

        :param us_filing_type_value: The us_filing_type_value of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: str
        """

        self._us_filing_type_value = us_filing_type_value

    @property
    def incoterm(self):
        """Gets the incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.<BR>          EXW ExWorks<BR>          FCA Free Carrier<BR>          CPT Carriage Paid To<BR>          CIP Carriage and Insurance Paid To<BR>          DPU Delivered at Place Unloaded<BR>          DAP Delivered at Place<BR>          DDP Delivered Duty Paid<BR>          FAS Free Alongside Ship<BR>          FOB Free on Board<BR>          CFR Cost and Freight<BR>          CIF Cost, Insurance and Freight<BR>          DAF Delivered at Frontier<BR>          DAT Delivered at Terminal<BR>          DDU Delivered Duty Unpaid<BR>          DEQ Delivery ex Quay<BR>          DES Delivered ex Ship  # noqa: E501

        :return: The incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: str
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.<BR>          EXW ExWorks<BR>          FCA Free Carrier<BR>          CPT Carriage Paid To<BR>          CIP Carriage and Insurance Paid To<BR>          DPU Delivered at Place Unloaded<BR>          DAP Delivered at Place<BR>          DDP Delivered Duty Paid<BR>          FAS Free Alongside Ship<BR>          FOB Free on Board<BR>          CFR Cost and Freight<BR>          CIF Cost, Insurance and Freight<BR>          DAF Delivered at Frontier<BR>          DAT Delivered at Terminal<BR>          DDU Delivered Duty Unpaid<BR>          DEQ Delivery ex Quay<BR>          DES Delivered ex Ship  # noqa: E501

        :param incoterm: The incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :type: str
        """
        if incoterm is None:
            raise ValueError("Invalid value for `incoterm`, must not be `None`")  # noqa: E501
        allowed_values = ["EXW", "FCA", "CPT", "CIP", "DPU", "DAP", "DDP", "FAS", "FOB", "CFR", "CIF", "DAF", "DAT", "DDU", "DEQ", "DES"]  # noqa: E501
        if incoterm not in allowed_values:
            raise ValueError(
                "Invalid value for `incoterm` ({0}), must be one of {1}"  # noqa: E501
                .format(incoterm, allowed_values)
            )

        self._incoterm = incoterm

    @property
    def unit_of_measurement(self):
        """Gets the unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501

        Please enter Unit of measurement - metric,imperial  # noqa: E501

        :return: The unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measurement

    @unit_of_measurement.setter
    def unit_of_measurement(self, unit_of_measurement):
        """Sets the unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.

        Please enter Unit of measurement - metric,imperial  # noqa: E501

        :param unit_of_measurement: The unit_of_measurement of this SupermodelIoLogisticsExpressCreateShipmentRequestContent.  # noqa: E501
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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestContent, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
