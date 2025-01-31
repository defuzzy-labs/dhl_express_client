# SupermodelIoLogisticsExpressExportDeclarationLineItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Please provide line item number | 
**description** | **str** | Please provide description of the line item | 
**price** | **float** | Please provide unit or article price line item value | 
**quantity** | [**SupermodelIoLogisticsExpressExportDeclarationQuantity**](SupermodelIoLogisticsExpressExportDeclarationQuantity.md) |  | 
**commodity_codes** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCommodityCodes]**](SupermodelIoLogisticsExpressCreateShipmentRequestContentExportDeclarationCommodityCodes.md) | Please provide Commodity codes for the shipment at item line level | [optional] 
**export_reason_type** | **str** | Please provide the reason for export | [optional] 
**manufacturer_country** | **str** | Please enter two letter ISO manufacturer country code | 
**weight** | [**SupermodelIoLogisticsExpressExportDeclarationWeight**](SupermodelIoLogisticsExpressExportDeclarationWeight.md) |  | 
**is_taxes_paid** | **bool** | Please provide if the Taxes is paid for the line item | [optional] 
**customer_references** | [**list[SupermodelIoLogisticsExpressExportDeclarationCustomerReferences]**](SupermodelIoLogisticsExpressExportDeclarationCustomerReferences.md) | Please provide the Customer References for the line item | [optional] 
**customs_documents** | [**list[SupermodelIoLogisticsExpressExportDeclarationCustomsDocuments]**](SupermodelIoLogisticsExpressExportDeclarationCustomsDocuments.md) | Please provide the customs documents details | [optional] 
**pre_calculated_line_item_total_value** | **float** | Please provide monetary value of the line item x quantity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

