# SupermodelIoLogisticsExpressValueAddedServices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_code** | **str** | Please enter DHL Express value added service code. For detailed list of all available service codes for your prospect shipment please invoke GET /products or GET /rates | 
**value** | **float** | Please enter monetary value of service (e.g. Insured Value) | [optional] 
**currency** | **str** | Please enter currency code (e.g. Insured Value currency code) | [optional] 
**method** | **str** | Payment method code (e.g. Cash) | [optional] 
**dangerous_goods** | [**list[SupermodelIoLogisticsExpressValueAddedServicesDangerousGoods]**](SupermodelIoLogisticsExpressValueAddedServicesDangerousGoods.md) | The DangerousGoods section indicates if there is dangerous good content within the shipment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

