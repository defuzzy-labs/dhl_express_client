# SupermodelIoLogisticsExpressUpdatePickupRequestShipmentDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Please provide DHL Express Global product code of the shipment | 
**local_product_code** | **str** | Please provide DHL Express Local product code of the shipment | [optional] 
**accounts** | [**list[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) |  | [optional] 
**value_added_services** | [**list[SupermodelIoLogisticsExpressValueAddedServicesRates]**](SupermodelIoLogisticsExpressValueAddedServicesRates.md) |  | [optional] 
**is_customs_declarable** | **bool** | For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false) | 
**declared_value** | **float** | For customs purposes please advise on declared value of the shipment | [optional] 
**declared_value_currency** | **str** | For customs purposes please advise on declared value currency code of the shipment | [optional] 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 
**shipment_tracking_number** | **str** | Please provide Shipment Identification number (AWB number) | [optional] 
**packages** | [**list[SupermodelIoLogisticsExpressPackageRR]**](SupermodelIoLogisticsExpressPackageRR.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

