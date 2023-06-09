# SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationLineItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Please provide line item number | 
**description** | **str** | Please provide description of the line item | 
**price** | **float** | Please provide unit or article price line item value | 
**quantity** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationQuantity.md) |  | 
**commodity_codes** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCommodityCodes]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCommodityCodes.md) | Please provide Commodity codes for the shipment at item line level | [optional] 
**export_reason_type** | **str** | Please provide the reason for export | [optional] 
**manufacturer_country** | **str** | Please enter two letter ISO manufacturer country code | 
**export_control_classification_number** | **str** | Please enter Export Control Classification Number info&lt;BR&gt;                    This is required for EEI filing US country usage | [optional] 
**weight** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationWeight**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationWeight.md) |  | 
**is_taxes_paid** | **bool** | Please provide if the Taxes is paid for the line item | [optional] 
**additional_information** | **list[str]** | Please provide the additional information | [optional] 
**customer_references** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomerReferences]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomerReferences.md) | Please provide the Customer References for the line item | [optional] 
**customs_documents** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCustomsDocuments.md) | Please provide the customs documents details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

