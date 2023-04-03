# SupermodelIoLogisticsExpressRateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_details** | [**SupermodelIoLogisticsExpressRateRequestCustomerDetails**](SupermodelIoLogisticsExpressRateRequestCustomerDetails.md) |  | 
**accounts** | [**list[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment | [optional] 
**product_code** | **str** | Please enter DHL Express Global Product code | [optional] 
**local_product_code** | **str** | Please enter DHL Express Local Product code | [optional] 
**value_added_services** | [**list[SupermodelIoLogisticsExpressValueAddedServicesRates]**](SupermodelIoLogisticsExpressValueAddedServicesRates.md) | Please use if you wish to filter the response by value added services | [optional] 
**products_and_services** | [**list[SupermodelIoLogisticsExpressRateRequestProductsAndServices]**](SupermodelIoLogisticsExpressRateRequestProductsAndServices.md) | Please use if you wish to filter the response by product(s) and/or value added services | [optional] 
**payer_country_code** | **str** | payerCountryCode is to be provided if your profile has been enabled to view rates without an account number (this will provide DHL Express published rates for the payer country) | [optional] 
**planned_shipping_date_and_time** | **str** | Identifies the date and time the package is tendered. Both the date and time portions of the string are expected to be used. The date should not be a past date or a date more than 10 days in the future. The time is the local time of the shipment based on the shipper&#x27;s time zone. The date component must be in the format: YYYY-MM-DD; the time component must be in the format: HH:MM:SS using a 24 hour clock. The date and time parts are separated by the letter T (e.g. 2006-06-26T17:00:00 GMT+01:00). | 
**unit_of_measurement** | **str** | Please enter Unit of measurement - metric,imperial | 
**is_customs_declarable** | **bool** | For customs purposes please advise if your shipment is dutiable (true) or non dutiable (false) | 
**monetary_amount** | [**list[SupermodelIoLogisticsExpressRateRequestMonetaryAmount]**](SupermodelIoLogisticsExpressRateRequestMonetaryAmount.md) | Please provide monetary amount related to your shipment, for example shipment declared value | [optional] 
**request_all_value_added_services** | **bool** | Legacy field and replaced by newer field getAdditionalInformation. Please set this to true to receive all value added services for each product available | [optional] 
**estimated_delivery_date** | [**EstimatedDeliveryDate1**](EstimatedDeliveryDate1.md) |  | [optional] 
**get_additional_information** | [**list[SupermodelIoLogisticsExpressRateRequestGetAdditionalInformation]**](SupermodelIoLogisticsExpressRateRequestGetAdditionalInformation.md) | Provides additional information in the response like all value added services, and rule groups | [optional] 
**return_standard_products_only** | **bool** | Please set this to true to filter out all products which needs DHL Express special customer agreement | [optional] 
**next_business_day** | **bool** | Please set this to true in case you want to receive products which are not available on planned shipping date but next available day | [optional] [default to False]
**product_type_code** | **str** | Please select which type of priducts you are interested in | [optional] 
**packages** | [**list[SupermodelIoLogisticsExpressPackageRR]**](SupermodelIoLogisticsExpressPackageRR.md) | Here you can define properties per package | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

