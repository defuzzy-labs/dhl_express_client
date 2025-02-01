# SupermodelIoLogisticsExpressRatesProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name** | **str** | Name of the DHL Express product | [optional] 
**product_code** | **str** | This is the global DHL Express product code for which the delivery is feasible respecting the input data from the request. | [optional] 
**local_product_code** | **str** | This is the local DHL Express product code for which the delivery is feasible respecting the input data from the request. | [optional] 
**local_product_country_code** | **str** | The country code for the local service used | [optional] 
**network_type_code** | **str** | The NetworkTypeCode element indicates the product belongs to the Day Definite (DD) or Time Definite (TD) network.&lt;BR&gt;            Possible Values;&lt;BR&gt;             DD: Day Definite product&lt;BR&gt;             TD: Time Definite product | [optional] 
**is_customer_agreement** | **bool** | Indicator that the product only can be offered to customers with prior agreement. | [optional] 
**weight** | [**Weight1**](Weight1.md) |  | 
**total_price** | [**list[SupermodelIoLogisticsExpressRatesTotalPrice]**](SupermodelIoLogisticsExpressRatesTotalPrice.md) |  | 
**total_price_breakdown** | [**list[SupermodelIoLogisticsExpressRatesTotalPriceBreakdown]**](SupermodelIoLogisticsExpressRatesTotalPriceBreakdown.md) |  | [optional] 
**detailed_price_breakdown** | [**list[SupermodelIoLogisticsExpressRatesDetailedPriceBreakdown]**](SupermodelIoLogisticsExpressRatesDetailedPriceBreakdown.md) |  | [optional] 
**service_code_mutually_exclusive_groups** | [**list[SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups]**](SupermodelIoLogisticsExpressProductsServiceCodeMutuallyExclusiveGroups.md) | Group of serviceCodes that are mutually exclusive.  Only one serviceCode among the list must be applied for a shipment | [optional] 
**service_code_dependency_rule_groups** | [**list[SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups]**](SupermodelIoLogisticsExpressProductsServiceCodeDependencyRuleGroups.md) | Dependency rule groups for a particular serviceCode. | [optional] 
**pickup_capabilities** | [**SupermodelIoLogisticsExpressRatesPickupCapabilities**](SupermodelIoLogisticsExpressRatesPickupCapabilities.md) |  | [optional] 
**delivery_capabilities** | [**SupermodelIoLogisticsExpressRatesDeliveryCapabilities**](SupermodelIoLogisticsExpressRatesDeliveryCapabilities.md) |  | [optional] 
**items** | [**list[SupermodelIoLogisticsExpressRatesItems]**](SupermodelIoLogisticsExpressRatesItems.md) |  | [optional] 
**pricing_date** | **str** | The date when the rates for DHL products and services is provided | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

