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

class SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration(object):
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
        'line_items': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems]',
        'invoice': 'SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice',
        'remarks': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationRemarks]',
        'additional_charges': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalCharges]',
        'destination_port_name': 'str',
        'place_of_incoterm': 'str',
        'payer_vat_number': 'str',
        'recipient_reference': 'str',
        'exporter': 'SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter',
        'package_marks': 'str',
        'declaration_notes': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationDeclarationNotes]',
        'export_reference': 'str',
        'export_reason': 'str',
        'export_reason_type': 'str',
        'licenses': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLicenses]',
        'shipment_type': 'str',
        'customs_documents': 'list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments1]'
    }

    attribute_map = {
        'line_items': 'lineItems',
        'invoice': 'invoice',
        'remarks': 'remarks',
        'additional_charges': 'additionalCharges',
        'destination_port_name': 'destinationPortName',
        'place_of_incoterm': 'placeOfIncoterm',
        'payer_vat_number': 'payerVATNumber',
        'recipient_reference': 'recipientReference',
        'exporter': 'exporter',
        'package_marks': 'packageMarks',
        'declaration_notes': 'declarationNotes',
        'export_reference': 'exportReference',
        'export_reason': 'exportReason',
        'export_reason_type': 'exportReasonType',
        'licenses': 'licenses',
        'shipment_type': 'shipmentType',
        'customs_documents': 'customsDocuments'
    }

    def __init__(self, line_items=None, invoice=None, remarks=None, additional_charges=None, destination_port_name=None, place_of_incoterm=None, payer_vat_number=None, recipient_reference=None, exporter=None, package_marks=None, declaration_notes=None, export_reference=None, export_reason=None, export_reason_type=None, licenses=None, shipment_type=None, customs_documents=None):  # noqa: E501
        """SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration - a model defined in Swagger"""  # noqa: E501
        self._line_items = None
        self._invoice = None
        self._remarks = None
        self._additional_charges = None
        self._destination_port_name = None
        self._place_of_incoterm = None
        self._payer_vat_number = None
        self._recipient_reference = None
        self._exporter = None
        self._package_marks = None
        self._declaration_notes = None
        self._export_reference = None
        self._export_reason = None
        self._export_reason_type = None
        self._licenses = None
        self._shipment_type = None
        self._customs_documents = None
        self.discriminator = None
        self.line_items = line_items
        if invoice is not None:
            self.invoice = invoice
        if remarks is not None:
            self.remarks = remarks
        if additional_charges is not None:
            self.additional_charges = additional_charges
        if destination_port_name is not None:
            self.destination_port_name = destination_port_name
        if place_of_incoterm is not None:
            self.place_of_incoterm = place_of_incoterm
        if payer_vat_number is not None:
            self.payer_vat_number = payer_vat_number
        if recipient_reference is not None:
            self.recipient_reference = recipient_reference
        if exporter is not None:
            self.exporter = exporter
        if package_marks is not None:
            self.package_marks = package_marks
        if declaration_notes is not None:
            self.declaration_notes = declaration_notes
        if export_reference is not None:
            self.export_reference = export_reference
        if export_reason is not None:
            self.export_reason = export_reason
        if export_reason_type is not None:
            self.export_reason_type = export_reason_type
        if licenses is not None:
            self.licenses = licenses
        if shipment_type is not None:
            self.shipment_type = shipment_type
        if customs_documents is not None:
            self.customs_documents = customs_documents

    @property
    def line_items(self):
        """Gets the line_items of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter details for each export line item  # noqa: E501

        :return: The line_items of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter details for each export line item  # noqa: E501

        :param line_items: The line_items of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")  # noqa: E501

        self._line_items = line_items

    @property
    def invoice(self):
        """Gets the invoice of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501


        :return: The invoice of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.


        :param invoice: The invoice of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice
        """

        self._invoice = invoice

    @property
    def remarks(self):
        """Gets the remarks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter up to three remarks. <BR>              If using Customs Invoice template COMMERCIAL_INVOICE_04, the invoice can only print the first remarks field. The recommended max length is 20 characters. <BR>              If using Customs Invoice template COMMERCIAL_INVOICE_L_10 or COMMERCIAL_INVOICE_P_10, the invoice can print all three remraks fields.  The recommended max length is 45 characters.  # noqa: E501

        :return: The remarks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationRemarks]
        """
        return self._remarks

    @remarks.setter
    def remarks(self, remarks):
        """Sets the remarks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter up to three remarks. <BR>              If using Customs Invoice template COMMERCIAL_INVOICE_04, the invoice can only print the first remarks field. The recommended max length is 20 characters. <BR>              If using Customs Invoice template COMMERCIAL_INVOICE_L_10 or COMMERCIAL_INVOICE_P_10, the invoice can print all three remraks fields.  The recommended max length is 45 characters.  # noqa: E501

        :param remarks: The remarks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationRemarks]
        """

        self._remarks = remarks

    @property
    def additional_charges(self):
        """Gets the additional_charges of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter additional charge to appear on the invoice<BR>              admin, Administration Charge<BR>              delivery, Delivery Charge<BR>              documentation, Documentation Charge<BR>              expedite, Expedite Charge<BR>              export, Export Charge<BR>              freight, Freight Charge<BR>              fuel_surcharge, Fuel Surcharge<BR>              logistic, Logistic Charge<BR>              other, Other Charge<BR>              packaging, Packaging Charge<BR>              pickup, Pickup Charge<BR>              handling, Handling Charge<BR>              vat, VAT Charge<BR>              insurance, Insurance Cost<BR>              reverse_charge, Reverse Charge  # noqa: E501

        :return: The additional_charges of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalCharges]
        """
        return self._additional_charges

    @additional_charges.setter
    def additional_charges(self, additional_charges):
        """Sets the additional_charges of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter additional charge to appear on the invoice<BR>              admin, Administration Charge<BR>              delivery, Delivery Charge<BR>              documentation, Documentation Charge<BR>              expedite, Expedite Charge<BR>              export, Export Charge<BR>              freight, Freight Charge<BR>              fuel_surcharge, Fuel Surcharge<BR>              logistic, Logistic Charge<BR>              other, Other Charge<BR>              packaging, Packaging Charge<BR>              pickup, Pickup Charge<BR>              handling, Handling Charge<BR>              vat, VAT Charge<BR>              insurance, Insurance Cost<BR>              reverse_charge, Reverse Charge  # noqa: E501

        :param additional_charges: The additional_charges of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalCharges]
        """

        self._additional_charges = additional_charges

    @property
    def destination_port_name(self):
        """Gets the destination_port_name of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide destination port details  # noqa: E501

        :return: The destination_port_name of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._destination_port_name

    @destination_port_name.setter
    def destination_port_name(self, destination_port_name):
        """Sets the destination_port_name of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide destination port details  # noqa: E501

        :param destination_port_name: The destination_port_name of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._destination_port_name = destination_port_name

    @property
    def place_of_incoterm(self):
        """Gets the place_of_incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Name of port of departure, shipment or destination as required under the applicable delivery term.  # noqa: E501

        :return: The place_of_incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._place_of_incoterm

    @place_of_incoterm.setter
    def place_of_incoterm(self, place_of_incoterm):
        """Sets the place_of_incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Name of port of departure, shipment or destination as required under the applicable delivery term.  # noqa: E501

        :param place_of_incoterm: The place_of_incoterm of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._place_of_incoterm = place_of_incoterm

    @property
    def payer_vat_number(self):
        """Gets the payer_vat_number of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide Payer VAT number  # noqa: E501

        :return: The payer_vat_number of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._payer_vat_number

    @payer_vat_number.setter
    def payer_vat_number(self, payer_vat_number):
        """Sets the payer_vat_number of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide Payer VAT number  # noqa: E501

        :param payer_vat_number: The payer_vat_number of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._payer_vat_number = payer_vat_number

    @property
    def recipient_reference(self):
        """Gets the recipient_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter recipient reference  # noqa: E501

        :return: The recipient_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._recipient_reference

    @recipient_reference.setter
    def recipient_reference(self, recipient_reference):
        """Sets the recipient_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter recipient reference  # noqa: E501

        :param recipient_reference: The recipient_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._recipient_reference = recipient_reference

    @property
    def exporter(self):
        """Gets the exporter of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501


        :return: The exporter of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter
        """
        return self._exporter

    @exporter.setter
    def exporter(self, exporter):
        """Sets the exporter of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.


        :param exporter: The exporter of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter
        """

        self._exporter = exporter

    @property
    def package_marks(self):
        """Gets the package_marks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter package marks  # noqa: E501

        :return: The package_marks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._package_marks

    @package_marks.setter
    def package_marks(self, package_marks):
        """Sets the package_marks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter package marks  # noqa: E501

        :param package_marks: The package_marks of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._package_marks = package_marks

    @property
    def declaration_notes(self):
        """Gets the declaration_notes of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide up to three dcelaration notes  # noqa: E501

        :return: The declaration_notes of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationDeclarationNotes]
        """
        return self._declaration_notes

    @declaration_notes.setter
    def declaration_notes(self, declaration_notes):
        """Sets the declaration_notes of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide up to three dcelaration notes  # noqa: E501

        :param declaration_notes: The declaration_notes of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationDeclarationNotes]
        """

        self._declaration_notes = declaration_notes

    @property
    def export_reference(self):
        """Gets the export_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter export reference  # noqa: E501

        :return: The export_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._export_reference

    @export_reference.setter
    def export_reference(self, export_reference):
        """Sets the export_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter export reference  # noqa: E501

        :param export_reference: The export_reference of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._export_reference = export_reference

    @property
    def export_reason(self):
        """Gets the export_reason of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please enter export reason  # noqa: E501

        :return: The export_reason of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._export_reason

    @export_reason.setter
    def export_reason(self, export_reason):
        """Sets the export_reason of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please enter export reason  # noqa: E501

        :param export_reason: The export_reason of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: str
        """

        self._export_reason = export_reason

    @property
    def export_reason_type(self):
        """Gets the export_reason_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide the reason for export  # noqa: E501

        :return: The export_reason_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._export_reason_type

    @export_reason_type.setter
    def export_reason_type(self, export_reason_type):
        """Sets the export_reason_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide the reason for export  # noqa: E501

        :param export_reason_type: The export_reason_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
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
    def licenses(self):
        """Gets the licenses of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide details about export and import licenses  # noqa: E501

        :return: The licenses of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLicenses]
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide details about export and import licenses  # noqa: E501

        :param licenses: The licenses of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLicenses]
        """

        self._licenses = licenses

    @property
    def shipment_type(self):
        """Gets the shipment_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons  # noqa: E501

        :return: The shipment_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: str
        """
        return self._shipment_type

    @shipment_type.setter
    def shipment_type(self, shipment_type):
        """Sets the shipment_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons  # noqa: E501

        :param shipment_type: The shipment_type of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
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
        """Gets the customs_documents of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501

        Please provide the Customs Documents at invoice level  # noqa: E501

        :return: The customs_documents of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments1]
        """
        return self._customs_documents

    @customs_documents.setter
    def customs_documents(self, customs_documents):
        """Sets the customs_documents of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.

        Please provide the Customs Documents at invoice level  # noqa: E501

        :param customs_documents: The customs_documents of this SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments1]
        """

        self._customs_documents = customs_documents

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
        if issubclass(SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration, dict):
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
        if not isinstance(other, SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
