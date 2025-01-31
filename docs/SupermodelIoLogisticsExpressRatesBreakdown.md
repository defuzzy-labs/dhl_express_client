# SupermodelIoLogisticsExpressRatesBreakdown

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | For /rates:&lt;BR&gt;  name within the first occurrence of breakdown will be the Global Product Name.&lt;BR&gt;&lt;BR&gt; For /landed-cost:&lt;BR&gt; When landed-cost is requested then following items name (Charge Types) might be returned: &lt;BR&gt;                        Charge Type : Description &lt;BR&gt;                        STDIS : Quoted shipment total discount &lt;BR&gt;                        SCUSV : Shipment Customs value &lt;BR&gt;                        SINSV : Insured value &lt;BR&gt;                        SPRQD : Shipment product quote discount&lt;BR&gt;                        SPRQN : The price quoted to the Customer by DHL at the time of the booking. This quote covers the weight price including discounts and without taxes. &lt;BR&gt;                        STSCH : The total of service charges quoted to customer for DHL Express value added services, the amount is after discounts and doesn&#x27;t include tax amounts. &lt;BR&gt;                        MACHG : The total of service charges as provided by Merchant for the purpose of landed cost calculation. &lt;BR&gt;                        MFCHG : The freight charge as provided by Merchant for the purpose of landed cost calculation. | [optional] 
**service_code** | **str** | Special service or extra charge code. This is the code you would have to use in the /shipment service if you wish to add an optional Service such as Saturday delivery | [optional] 
**local_service_code** | **str** | Local service code | [optional] 
**type_code** | **str** | Price breakdown type code. &lt;BR&gt;typeCode within the first occurrence of breakdown will be the Local Product Name. | [optional] 
**service_type_code** | **str** | Special service charge code type for service. | [optional] 
**price** | **float** | Price breakdown value | [optional] 
**price_currency** | **str** | This the currency of the rated shipment for the prices listed. | [optional] 
**is_customer_agreement** | **bool** | Customer agreement indicator for product and services, if service is offered with prior customer agreement | [optional] 
**is_marketed_service** | **bool** | Indicator if the special service is marketed service | [optional] 
**is_billing_service_indicator** | **bool** | Indicator if there is any discount allowed | [optional] 
**price_breakdown** | [**list[SupermodelIoLogisticsExpressRatesPriceBreakdown1]**](SupermodelIoLogisticsExpressRatesPriceBreakdown1.md) |  | [optional] 
**tariff_rate_formula** | **str** | Tariff Rate Formula on Shipment Level | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

