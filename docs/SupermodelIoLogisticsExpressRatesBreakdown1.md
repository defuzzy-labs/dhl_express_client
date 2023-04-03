# SupermodelIoLogisticsExpressRatesBreakdown1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the charge | [optional] 
**service_code** | **str** | Special service or extra charge code. This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery | [optional] 
**local_service_code** | **str** | Local service code | [optional] 
**type_code** | **str** | Charge type or category.&lt;BR&gt;                        Possible values;&lt;BR&gt;                        - DUTY&lt;BR&gt;                        - TAX&lt;BR&gt;                        - FEE | 
**service_type_code** | **str** | Special service charge code type for service. XCH type charge codes are Optional Services and should be displayed to users for selection.&lt;BR&gt;                        The possible values are;&lt;BR&gt;                        - XCH &#x3D; Extra charge&lt;BR&gt;                        - FEE &#x3D; Fee&lt;BR&gt;                        - SCH &#x3D; Surcharge&lt;BR&gt;                        - NRI &#x3D; Non Revenue Item&lt;BR&gt;                        Other charges may be automatically returned when applicable. | [optional] 
**price** | **float** | The charge amount of the line item charge. | 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | [optional] 
**is_customer_agreement** | **bool** | Customer agreement indicator for product and services, if service is offered with prior customer agreement | [optional] 
**is_marketed_service** | **bool** | Indicator if the special service is marketed service | [optional] 
**is_billing_service_indicator** | **bool** | Indicator if there is any discount allowed | [optional] 
**price_breakdown** | [**list[SupermodelIoLogisticsExpressRatesPriceBreakdown2]**](SupermodelIoLogisticsExpressRatesPriceBreakdown2.md) |  | [optional] 
**tariff_rate_formula** | **str** | Tariff Rate Formula on Line Item Level | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

