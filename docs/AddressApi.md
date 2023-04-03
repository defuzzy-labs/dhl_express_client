# swagger_client.AddressApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_address_validate**](AddressApi.md#exp_api_address_validate) | **GET** /address-validate | Validate DHL Express pickup/delivery capabilities at origin/destination

# **exp_api_address_validate**
> SupermodelIoLogisticsExpressAddressValidateResponse exp_api_address_validate(type, country_code, postal_code=postal_code, city_name=city_name, county_name=county_name, strict_validation=strict_validation, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Validate DHL Express pickup/delivery capabilities at origin/destination

Validates if DHL Express has got pickup/delivery capabilities at origin/destination 

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
api_instance = swagger_client.AddressApi(swagger_client.ApiClient(configuration))
type = 'type_example' # str | 
country_code = 'country_code_example' # str | A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code
postal_code = 'postal_code_example' # str | Text specifying the postal code for an address. https://gs1.org/voc/postalCode (optional)
city_name = 'city_name_example' # str | Text specifying the city name (optional)
county_name = 'county_name_example' # str | Text specifying the county name (optional)
strict_validation = true # bool | If set to true service will return no records when exact valid match not found (optional) (default to true)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Validate DHL Express pickup/delivery capabilities at origin/destination
    api_response = api_instance.exp_api_address_validate(type, country_code, postal_code=postal_code, city_name=city_name, county_name=county_name, strict_validation=strict_validation, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->exp_api_address_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **country_code** | **str**| A short text string code (see values defined in ISO 3166) specifying the shipment origin country. https://gs1.org/voc/Country, Alpha-2 Code | 
 **postal_code** | **str**| Text specifying the postal code for an address. https://gs1.org/voc/postalCode | [optional] 
 **city_name** | **str**| Text specifying the city name | [optional] 
 **county_name** | **str**| Text specifying the county name | [optional] 
 **strict_validation** | **bool**| If set to true service will return no records when exact valid match not found | [optional] [default to true]
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressAddressValidateResponse**](SupermodelIoLogisticsExpressAddressValidateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

