# swagger_client.RatingApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_landed_cost**](RatingApi.md#exp_api_landed_cost) | **POST** /landed-cost | Landed Cost
[**exp_api_rates**](RatingApi.md#exp_api_rates) | **GET** /rates | Retrieve Rates for a one piece Shipment
[**exp_api_rates_many**](RatingApi.md#exp_api_rates_many) | **POST** /rates | Retrieve Rates for Multi-piece Shipments

# **exp_api_landed_cost**
> SupermodelIoLogisticsExpressRates exp_api_landed_cost(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Landed Cost

The Landed Cost section allows further information around products being sold to be provided. In return the duty, tax and shipping charges are calculated in real time and provides transparency about any extra costs the buyer may have to pay before they reach them. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupermodelIoLogisticsExpressLandedCostRequest() # SupermodelIoLogisticsExpressLandedCostRequest | Details about the requested shipment
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Landed Cost
    api_response = api_instance.exp_api_landed_cost(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->exp_api_landed_cost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupermodelIoLogisticsExpressLandedCostRequest**](SupermodelIoLogisticsExpressLandedCostRequest.md)| Details about the requested shipment | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_rates**
> SupermodelIoLogisticsExpressRates exp_api_rates(account_number, origin_country_code, origin_city_name, destination_country_code, destination_city_name, weight, length, width, height, planned_shipping_date, is_customs_declarable, unit_of_measurement, origin_postal_code=origin_postal_code, destination_postal_code=destination_postal_code, next_business_day=next_business_day, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, get_all_value_added_services=get_all_value_added_services, request_estimated_delivery_date=request_estimated_delivery_date, estimated_delivery_date_type=estimated_delivery_date_type)

Retrieve Rates for a one piece Shipment

The Rate request will return DHL's product capabilities and prices (where applicable) based on the input data. Using the shipper and receiver address as well as the dimension and weights of the pieces belonging to a shipment, this operation returns the available products including the shipping price (where applicable) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
account_number = 'account_number_example' # str | DHL Express customer account number
origin_country_code = 'origin_country_code_example' # str | A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code
origin_city_name = 'origin_city_name_example' # str | Text specifying the city name
destination_country_code = 'destination_country_code_example' # str | A short text string code (see values defined in ISO 3166) specifying the shipment destination country. https://gs1.org/voc/Country, Alpha-2 Code
destination_city_name = 'destination_city_name_example' # str | Text specifying the city name
weight = 1.2 # float | Gross weight of the shipment including packaging.
length = 1.2 # float | Total length of the shipment including packaging.
width = 1.2 # float | Total width of the shipment including packaging.
height = 1.2 # float | Total height of the shipment including packaging.
planned_shipping_date = 'planned_shipping_date_example' # str | Timestamp represents the date you plan to ship your prospected shipment 
is_customs_declarable = true # bool | 
unit_of_measurement = 'unit_of_measurement_example' # str | The UnitOfMeasurement node conveys the unit of measurements used in the operation. This single value corresponds to the units of weight and measurement which are used throughout the message processing. 
origin_postal_code = 'origin_postal_code_example' # str | Text specifying the postal code for an address. https://gs1.org/voc/postalCode (optional)
destination_postal_code = 'destination_postal_code_example' # str | Text specifying the postal code for an address. https://gs1.org/voc/postalCode (optional)
next_business_day = true # bool | When set to true and there are no products available for given plannedShippingDate then products available for the next possible pickup date are returned  (optional)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)
strict_validation = false # bool | If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. (optional) (default to false)
get_all_value_added_services = false # bool | Option to return list of all value added services and its rule groups if applicable (optional) (default to false)
request_estimated_delivery_date = true # bool | Option to return Estimated Delivery Date in response (optional) (default to true)
estimated_delivery_date_type = 'QDDF' # str | Estimated Delivery Date Type. QDDF: is the fastest 'docs' transit time as quoted to the customer at booking or shipment creation. No custom clearance is considered. QDDC: constitutes DHL's service commitment as quoted at booking or shipment creation. QDDc builds in clearance time, and potentially other special perational non-transport component(s), when relevant.  (optional) (default to QDDF)

try:
    # Retrieve Rates for a one piece Shipment
    api_response = api_instance.exp_api_rates(account_number, origin_country_code, origin_city_name, destination_country_code, destination_city_name, weight, length, width, height, planned_shipping_date, is_customs_declarable, unit_of_measurement, origin_postal_code=origin_postal_code, destination_postal_code=destination_postal_code, next_business_day=next_business_day, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation, get_all_value_added_services=get_all_value_added_services, request_estimated_delivery_date=request_estimated_delivery_date, estimated_delivery_date_type=estimated_delivery_date_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->exp_api_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_number** | **str**| DHL Express customer account number | 
 **origin_country_code** | **str**| A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code | 
 **origin_city_name** | **str**| Text specifying the city name | 
 **destination_country_code** | **str**| A short text string code (see values defined in ISO 3166) specifying the shipment destination country. https://gs1.org/voc/Country, Alpha-2 Code | 
 **destination_city_name** | **str**| Text specifying the city name | 
 **weight** | **float**| Gross weight of the shipment including packaging. | 
 **length** | **float**| Total length of the shipment including packaging. | 
 **width** | **float**| Total width of the shipment including packaging. | 
 **height** | **float**| Total height of the shipment including packaging. | 
 **planned_shipping_date** | **str**| Timestamp represents the date you plan to ship your prospected shipment  | 
 **is_customs_declarable** | **bool**|  | 
 **unit_of_measurement** | **str**| The UnitOfMeasurement node conveys the unit of measurements used in the operation. This single value corresponds to the units of weight and measurement which are used throughout the message processing.  | 
 **origin_postal_code** | **str**| Text specifying the postal code for an address. https://gs1.org/voc/postalCode | [optional] 
 **destination_postal_code** | **str**| Text specifying the postal code for an address. https://gs1.org/voc/postalCode | [optional] 
 **next_business_day** | **bool**| When set to true and there are no products available for given plannedShippingDate then products available for the next possible pickup date are returned  | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 
 **strict_validation** | **bool**| If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. | [optional] [default to false]
 **get_all_value_added_services** | **bool**| Option to return list of all value added services and its rule groups if applicable | [optional] [default to false]
 **request_estimated_delivery_date** | **bool**| Option to return Estimated Delivery Date in response | [optional] [default to true]
 **estimated_delivery_date_type** | **str**| Estimated Delivery Date Type. QDDF: is the fastest &#x27;docs&#x27; transit time as quoted to the customer at booking or shipment creation. No custom clearance is considered. QDDC: constitutes DHL&#x27;s service commitment as quoted at booking or shipment creation. QDDc builds in clearance time, and potentially other special perational non-transport component(s), when relevant.  | [optional] [default to QDDF]

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_rates_many**
> SupermodelIoLogisticsExpressRates exp_api_rates_many(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation)

Retrieve Rates for Multi-piece Shipments

The Rate request will return DHL's product capabilities and prices (where applicable) based on the input data. Using the shipper and receiver address as well as the dimension and weights of the pieces belonging to a shipment, this operation returns the available products including the shipping price (where applicable) 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RatingApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupermodelIoLogisticsExpressRateRequest() # SupermodelIoLogisticsExpressRateRequest | Details about the requested shipment
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)
strict_validation = false # bool | If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. (optional) (default to false)

try:
    # Retrieve Rates for Multi-piece Shipments
    api_response = api_instance.exp_api_rates_many(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version, strict_validation=strict_validation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RatingApi->exp_api_rates_many: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupermodelIoLogisticsExpressRateRequest**](SupermodelIoLogisticsExpressRateRequest.md)| Details about the requested shipment | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 
 **strict_validation** | **bool**| If set to true, indicate strict DCT validation of address details, and validation of product and service(s) combination provided in request. | [optional] [default to false]

### Return type

[**SupermodelIoLogisticsExpressRates**](SupermodelIoLogisticsExpressRates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

