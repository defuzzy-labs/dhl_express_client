# SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_tracking_number** | **str** | Please provide Shipment Identification number (AWB number) | [optional] 
**planned_ship_date** | **str** | The planned shipment date for the provided shipmentTrackingNumber.  The date must be in the format: YYYY-MM-DD | [optional] 
**accounts** | [**list[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment.   Note: accounts/0/number with typeCode &#x27;shipper&#x27; is mandatory if using POST method and no shipmentTrackingNumber is provided in request. | [optional] 
**content** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestContent.md) |  | 
**output_image_properties** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestOutputImageProperties.md) |  | [optional] 
**customer_details** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestCustomerDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

