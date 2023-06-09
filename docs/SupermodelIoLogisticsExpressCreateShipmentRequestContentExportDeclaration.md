# SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclaration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_items** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems.md) | Please enter details for each export line item | 
**invoice** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationInvoice.md) |  | [optional] 
**remarks** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationRemarks]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationRemarks.md) | Please enter up to three remarks. &lt;BR&gt;              If using Customs Invoice template COMMERCIAL_INVOICE_04, the invoice can only print the first remarks field. The recommended max length is 20 characters. &lt;BR&gt;              If using Customs Invoice template COMMERCIAL_INVOICE_L_10 or COMMERCIAL_INVOICE_P_10, the invoice can print all three remraks fields.  The recommended max length is 45 characters. | [optional] 
**additional_charges** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalCharges]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationAdditionalCharges.md) | Please enter additional charge to appear on the invoice&lt;BR&gt;              admin, Administration Charge&lt;BR&gt;              delivery, Delivery Charge&lt;BR&gt;              documentation, Documentation Charge&lt;BR&gt;              expedite, Expedite Charge&lt;BR&gt;              export, Export Charge&lt;BR&gt;              freight, Freight Charge&lt;BR&gt;              fuel_surcharge, Fuel Surcharge&lt;BR&gt;              logistic, Logistic Charge&lt;BR&gt;              other, Other Charge&lt;BR&gt;              packaging, Packaging Charge&lt;BR&gt;              pickup, Pickup Charge&lt;BR&gt;              handling, Handling Charge&lt;BR&gt;              vat, VAT Charge&lt;BR&gt;              insurance, Insurance Cost&lt;BR&gt;              reverse_charge, Reverse Charge | [optional] 
**destination_port_name** | **str** | Please provide destination port details | [optional] 
**place_of_incoterm** | **str** | Name of port of departure, shipment or destination as required under the applicable delivery term. | [optional] 
**payer_vat_number** | **str** | Please provide Payer VAT number | [optional] 
**recipient_reference** | **str** | Please enter recipient reference | [optional] 
**exporter** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationExporter.md) |  | [optional] 
**package_marks** | **str** | Please enter package marks | [optional] 
**declaration_notes** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationDeclarationNotes]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationDeclarationNotes.md) | Please provide up to three dcelaration notes | [optional] 
**export_reference** | **str** | Please enter export reference | [optional] 
**export_reason** | **str** | Please enter export reason | [optional] 
**export_reason_type** | **str** | Please provide the reason for export | [optional] 
**licenses** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLicenses]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLicenses.md) | Please provide details about export and import licenses | [optional] 
**shipment_type** | **str** | Please provide the shipment was sent for Personal (Gift) or Commercial (Sale) reasons | [optional] 
**customs_documents** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments1]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments1.md) | Please provide the Customs Documents at invoice level | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

