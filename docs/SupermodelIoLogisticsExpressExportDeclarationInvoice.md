# SupermodelIoLogisticsExpressExportDeclarationInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | Please enter commercial invoice number | 
**_date** | **str** | Please enter commercial invoice date | 
**function** | **str** | Please provide the purpose was the document details captured and are planned to be used. Note: export and import is only applicable for approve Sale In Transit customers | 
**customer_references** | [**list[SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferences]**](SupermodelIoLogisticsExpressExportDeclarationInvoiceCustomerReferences.md) | Please provide the customer references at invoice level.   Note: customerReference/0/value with typeCode &#x27;CU&#x27; is mandatory if using POST method and no shipmentTrackingNumber is provided in request. It is recommended to provide less than 20 customer references of &#x27;MRN&#x27; type code | [optional] 
**indicative_customs_values** | [**SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues**](SupermodelIoLogisticsExpressExportDeclarationInvoiceIndicativeCustomsValues.md) |  | [optional] 
**pre_calculated_total_values** | [**SupermodelIoLogisticsExpressExportDeclarationInvoicePreCalculatedTotalValues**](SupermodelIoLogisticsExpressExportDeclarationInvoicePreCalculatedTotalValues.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

