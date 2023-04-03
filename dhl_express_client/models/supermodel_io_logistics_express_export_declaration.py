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

class SupermodelIoLogisticsExpressExportDeclaration(object):
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
        'line_items': 'list[SupermodelIoLogisticsExpressExportDeclarationLineItems]',
        'invoice': 'SupermodelIoLogisticsExpressExportDeclarationInvoice',
        'remarks': 'list[SupermodelIoLogisticsExpressExportDeclarationRemarks]',
        'additional_charges': 'list[SupermodelIoLogisticsExpressExportDeclarationAdditionalCharges]',
        'place_of_incoterm': 'str',
        'recipient_reference': 'str',
        'exporter': 'SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter',
        'export_reason_type': 'str',
        'shipment_type': 'str',
        'customs_documents': 'list[SupermodelIoLogisticsExpressExportDeclarationCustomsDocuments1]',
        'incoterm': 'str'
    }

    attribute_map = {
        'line_items': 'lineItems',
        'invoice': 'invoice',
        'remarks': 'remarks',
        'additional_charges': 'additionalCharges',
        'place_of_incoterm': 'placeOfIncoterm',
        'recipient_reference': 'recipientReference',
        'exporter': 'exporter',
        'export_reason_type': 'exportReasonType',
        'shipment_type': 'shipmentType',
        'customs_documents': 'customsDocuments',
        'incoterm': 'incoterm'
    }

    def __init__(self, line_items=None, invoice=None, remarks=None, additional_charges=None, place_of_incoterm=None, recipient_reference=None, exporter=None, export_reason_type=None, shipment_type=None, customs_documents=None, incoterm=None):  # noqa: E501
        """SupermodelIoLogisticsExpressExportDeclaration - a model defined in Swagger"""  # noqa: E501
        self._line_items = None
        self._invoice = None
        self._remarks = None
        self._additional_charges = None
        self._place_of_incoterm = None
        self._recipient_reference = None
        self._exporter = None
        self._export_reason_type = None
        self._shipment_type = None
        self._customs_documents = None
        self._incoterm = None
        self.discriminator = None
        self.line_items = line_items
        self.invoice = invoice
        if remarks is not None:
            self.remarks = remarks
        if additional_charges is not None:
            self.additional_charges = additional_charges
        if place_of_incoterm is not None:
            self.place_of_incoterm = place_of_incoterm
        if recipient_reference is not None:
            self.recipient_reference = recipient_reference
        if exporter is not None:
            self.exporter = exporter
        if export_reason_type is not None:
            self.export_reason_type = export_reason_type
        if shipment_type is not None:
            self.shipment_type = shipment_type
        if customs_documents is not None:
            self.customs_documents = customs_documents
        self.incoterm = incoterm

    @property
    def line_items(self):
        """Gets the line_items of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please enter details for each export line item  # noqa: E501

        :return: The line_items of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressExportDeclarationLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this SupermodelIoLogisticsExpressExportDeclaration.

        Please enter details for each export line item  # noqa: E501

        :param line_items: The line_items of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressExportDeclarationLineItems]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")  # noqa: E501

        self._line_items = line_items

    @property
    def invoice(self):
        """Gets the invoice of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501


        :return: The invoice of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressExportDeclarationInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this SupermodelIoLogisticsExpressExportDeclaration.


        :param invoice: The invoice of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: SupermodelIoLogisticsExpressExportDeclarationInvoice
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice

    @property
    def remarks(self):
        """Gets the remarks of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please enter up to three remarks  # noqa: E501

        :return: The remarks of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressExportDeclarationRemarks]
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this SupermodelIoLogisticsExpressExportDeclaration.

        Please enter up to three remarks  # noqa: E501

        :param remarks: The remarks of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressExportDeclarationRemarks]
        """

        self._remarks = remarks

    @property
    def additional_charges(self):
        """Gets the additional_charges of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please enter additional charge to appear on the invoice<BR>      admin, Administration Charge<BR>      delivery, Delivery Charge<BR>      documentation, Documentation Charge<BR>      expedite, Expedite Charge<BR>      freight, Freight Charge<BR>      fuel surcharge, Fuel Surcharge<BR>      logistic, Logistic Charge<BR>      other, Other Charge<BR>      packaging, Packaging Charge<BR>      pickup, Pickup Charge<BR>      handling, Handling Charge<BR>      vat, VAT Charge<BR>      insurance, Insurance Cost  # noqa: E501

        :return: The additional_charges of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressExportDeclarationAdditionalCharges]
        """
        return self._additional_charges

    @additional_charges.setter
    def additional_charges(self, additional_charges):
        """Sets the additional_charges of this SupermodelIoLogisticsExpressExportDeclaration.

        Please enter additional charge to appear on the invoice<BR>      admin, Administration Charge<BR>      delivery, Delivery Charge<BR>      documentation, Documentation Charge<BR>      expedite, Expedite Charge<BR>      freight, Freight Charge<BR>      fuel surcharge, Fuel Surcharge<BR>      logistic, Logistic Charge<BR>      other, Other Charge<BR>      packaging, Packaging Charge<BR>      pickup, Pickup Charge<BR>      handling, Handling Charge<BR>      vat, VAT Charge<BR>      insurance, Insurance Cost  # noqa: E501

        :param additional_charges: The additional_charges of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressExportDeclarationAdditionalCharges]
        """

        self._additional_charges = additional_charges

    @property
    def place_of_incoterm(self):
        """Gets the place_of_incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Name of port of departure, shipment or destination as required under the applicable delivery term.  # noqa: E501

        :return: The place_of_incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._place_of_incoterm

    @place_of_incoterm.setter
    def place_of_incoterm(self, place_of_incoterm):
        """Sets the place_of_incoterm of this SupermodelIoLogisticsExpressExportDeclaration.

        Name of port of departure, shipment or destination as required under the applicable delivery term.  # noqa: E501

        :param place_of_incoterm: The place_of_incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: str
        """

        self._place_of_incoterm = place_of_incoterm

    @property
    def recipient_reference(self):
        """Gets the recipient_reference of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please enter recipient reference  # noqa: E501

        :return: The recipient_reference of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._recipient_reference

    @recipient_reference.setter
    def recipient_reference(self, recipient_reference):
        """Sets the recipient_reference of this SupermodelIoLogisticsExpressExportDeclaration.

        Please enter recipient reference  # noqa: E501

        :param recipient_reference: The recipient_reference of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: str
        """

        self._recipient_reference = recipient_reference

    @property
    def exporter(self):
        """Gets the exporter of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501


        :return: The exporter of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter
        """
        return self._exporter

    @exporter.setter
    def exporter(self, exporter):
        """Sets the exporter of this SupermodelIoLogisticsExpressExportDeclaration.


        :param exporter: The exporter of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter
        """

        self._exporter = exporter

    @property
    def export_reason_type(self):
        """Gets the export_reason_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please provide the reason for export  # noqa: E501

        :return: The export_reason_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._export_reason_type

    @export_reason_type.setter
    def export_reason_type(self, export_reason_type):
        """Sets the export_reason_type of this SupermodelIoLogisticsExpressExportDeclaration.

        Please provide the reason for export  # noqa: E501

        :param export_reason_type: The export_reason_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: str
        """
        allowed_values = ["permanent", "temporary", "return", "used_exhibition_goods_to_origin", "intercompany_use", "commercial_purpose_or_sale", "personal_belongings_or_personal_use", "sample", "gift", "return_to_origin", "warranty_replacement", "diplomatic_goods", "defence_material"]  # noqa: E501
        if export_reason_type not in allowed_values:
            raise ValueError(
                "Invalid value for `export_reason_type` ({0}), must be one of {1}"  # noqa: E501
                .format(export_reason_type, allowed_values)
            )

        self._export_reason_type = export_reason_type

    @property
    def shipment_type(self):
        """Gets the shipment_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons  # noqa: E501

        :return: The shipment_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this SupermodelIoLogisticsExpressExportDeclaration.

        Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons  # noqa: E501

        :param shipment_type: The shipment_type of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: str
        """
        allowed_values = ["personal", "commercial"]  # noqa: E501
        if shipment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `shipment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(shipment_type, allowed_values)
            )

        self._shipment_type = shipment_type

    @property
    def customs_documents(self):
        """Gets the customs_documents of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        Please provide the Customs Documents at invoice level  # noqa: E501

        :return: The customs_documents of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressExportDeclarationCustomsDocuments1]
        """
        return self._customs_documents

    @customs_documents.setter
    def customs_documents(self, customs_documents):
        """Sets the customs_documents of this SupermodelIoLogisticsExpressExportDeclaration.

        Please provide the Customs Documents at invoice level  # noqa: E501

        :param customs_documents: The customs_documents of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressExportDeclarationCustomsDocuments1]
        """

        self._customs_documents = customs_documents

    @property
    def incoterm(self):
        """Gets the incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501

        The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.<BR>      EXW ExWorks<BR>      FCA Free Carrier<BR>      CPT Carriage Paid To<BR>      CIP Carriage and Insurance Paid To<BR>      DPU Delivered at Place Unloaded<BR>      DAP Delivered at Place<BR>      DDP Delivered Duty Paid<BR>      FAS Free Alongside Ship<BR>      FOB Free on Board<BR>      CFR Cost and Freight<BR>      CIF Cost, Insurance and Freight<BR>      DAF Delivered at Frontier<BR>      DAT Delivered at Terminal<BR>      DDU Delivered Duty Unpaid<BR>      DEQ Delivery ex Quay<BR>      DES Delivered ex Ship  # noqa: E501

        :return: The incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._incoterm

    @incoterm.setter
    def incoterm(self, incoterm):
        """Sets the incoterm of this SupermodelIoLogisticsExpressExportDeclaration.

        The Incoterms rules are a globally-recognized set of standards, used worldwide in international and domestic contracts for the delivery of goods, illustrating responsibilities between buyer and seller for costs and risk, as well as cargo insurance.<BR>      EXW ExWorks<BR>      FCA Free Carrier<BR>      CPT Carriage Paid To<BR>      CIP Carriage and Insurance Paid To<BR>      DPU Delivered at Place Unloaded<BR>      DAP Delivered at Place<BR>      DDP Delivered Duty Paid<BR>      FAS Free Alongside Ship<BR>      FOB Free on Board<BR>      CFR Cost and Freight<BR>      CIF Cost, Insurance and Freight<BR>      DAF Delivered at Frontier<BR>      DAT Delivered at Terminal<BR>      DDU Delivered Duty Unpaid<BR>      DEQ Delivery ex Quay<BR>      DES Delivered ex Ship  # noqa: E501

        :param incoterm: The incoterm of this SupermodelIoLogisticsExpressExportDeclaration.  # noqa: E501
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
        if issubclass(SupermodelIoLogisticsExpressExportDeclaration, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressExportDeclaration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other