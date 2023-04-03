# SupermodelIoLogisticsExpressLandedCostRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_details** | [**SupermodelIoLogisticsExpressLandedCostRequestCustomerDetails**](SupermodelIoLogisticsExpressLandedCostRequestCustomerDetails.md) |  | 
**accounts** | [**list[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment | 
**product_code** | **str** | Please enter DHL Express Global Product code | [optional] 
**local_product_code** | **str** | Please enter DHL Express Local Product code | [optional] 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 
**currency_code** | **str** | Currency code for the item price (the product being sold) and freight charge. The Landed Cost calculation result will be returned in this defined currency | 
**is_customs_declarable** | **bool** | Set this to true is shipment contains declarable content | 
**is_dtp_requested** | **bool** | Set this to true if you want DHL EXpress product Duties and Taxes Paid outside shipment destination | [optional] 
**is_insurance_requested** | **bool** | Set this true if you ask for DHL Express insurance service | [optional] 
**get_cost_breakdown** | **bool** | Allowed values &#x27;true&#x27; - item cost breakdown will be returned, &#x27;false&#x27; - item cost breakdown will not be returned | 
**charges** | [**list[SupermodelIoLogisticsExpressLandedCostRequestCharges]**](SupermodelIoLogisticsExpressLandedCostRequestCharges.md) | Please provide any additional charges you would like to include in total cost calculation | [optional] 
**shipment_purpose** | **str** | Possible values:&lt;BR&gt;      commercial: B2B&lt;BR&gt;      personal: B2C&lt;BR&gt;      commercia&#x27;: B2B&lt;BR&gt;      personal: B2C | [optional] 
**transportation_mode** | **str** |  | [optional] 
**merchant_selected_carrier_name** | **str** | Carrier being used to ship with. Allowed values are:&lt;BR&gt;      &#x27;DHL&#x27;,&#x27;UPS&#x27;,&#x27;FEDEX&#x27;,&#x27;TNT&#x27;,&#x27;POST&#x27;,&lt;BR&gt;      &#x27;OTHERS&#x27; | [optional] 
**packages** | [**list[SupermodelIoLogisticsExpressPackageRR]**](SupermodelIoLogisticsExpressPackageRR.md) | Here you can define properties per package | 
**items** | [**list[SupermodelIoLogisticsExpressLandedCostRequestItems]**](SupermodelIoLogisticsExpressLandedCostRequestItems.md) |  | 
**get_tariff_formula** | **bool** | Allowed values &#x27;true&#x27; - tariff formula on item and shipment level will be returned, &#x27;false&#x27; - tariff formula on item and shipment level will not be returned | [optional] 
**get_quotation_id** | **bool** | Allowed values &#x27;true&#x27; - quotation ID on shipment level will be returned, &#x27;false&#x27; - quotation ID on shipment level will not be returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

