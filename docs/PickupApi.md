# swagger_client.PickupApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_pickups**](PickupApi.md#exp_api_pickups) | **POST** /pickups | Create a DHL Express pickup booking request
[**exp_api_pickups_cancel**](PickupApi.md#exp_api_pickups_cancel) | **DELETE** /pickups/{dispatchConfirmationNumber} | Cancel a DHL Express pickup booking request
[**exp_api_pickups_update**](PickupApi.md#exp_api_pickups_update) | **PATCH** /pickups/{dispatchConfirmationNumber} | Update pickup information for an existing DHL Express pickup booking request

# **exp_api_pickups**
> SupermodelIoLogisticsExpressPickupResponse exp_api_pickups(body, x_version, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Create a DHL Express pickup booking request

The Pickup service creates a DHL Express pickup booking request 

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
api_instance = swagger_client.PickupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupermodelIoLogisticsExpressPickupRequest() # SupermodelIoLogisticsExpressPickupRequest | Details about the requested pickup
x_version = '2.12.0' # str | Interface version - do not change this field value  (default to 2.12.0)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Create a DHL Express pickup booking request
    api_response = api_instance.exp_api_pickups(body, x_version, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupApi->exp_api_pickups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupermodelIoLogisticsExpressPickupRequest**](SupermodelIoLogisticsExpressPickupRequest.md)| Details about the requested pickup | 
 **x_version** | **str**| Interface version - do not change this field value  | [default to 2.12.0]
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressPickupResponse**](SupermodelIoLogisticsExpressPickupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_pickups_cancel**
> exp_api_pickups_cancel(dispatch_confirmation_number, requestor_name, reason, x_version, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Cancel a DHL Express pickup booking request

The Cancel Pickup service can be used to cancel a DHL Express pickup booking request. Delete of a previous successful pickups are subject to entire consolidated pickup if applicable. 

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
api_instance = swagger_client.PickupApi(swagger_client.ApiClient(configuration))
dispatch_confirmation_number = 'dispatch_confirmation_number_example' # str | Shipment pickup confirmation number for example `PRG999126012345`
requestor_name = 'requestor_name_example' # str | Name of the person requesting to cancel the scheduled pickup 
reason = 'reason_example' # str | Provide why scheduled pickup is being cancelled 
x_version = '2.12.0' # str | Interface version - do not change this field value  (default to 2.12.0)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Cancel a DHL Express pickup booking request
    api_instance.exp_api_pickups_cancel(dispatch_confirmation_number, requestor_name, reason, x_version, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
except ApiException as e:
    print("Exception when calling PickupApi->exp_api_pickups_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_confirmation_number** | **str**| Shipment pickup confirmation number for example &#x60;PRG999126012345&#x60; | 
 **requestor_name** | **str**| Name of the person requesting to cancel the scheduled pickup  | 
 **reason** | **str**| Provide why scheduled pickup is being cancelled  | 
 **x_version** | **str**| Interface version - do not change this field value  | [default to 2.12.0]
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_pickups_update**
> SupermodelIoLogisticsExpressUpdatePickupResponse exp_api_pickups_update(body, x_version, dispatch_confirmation_number, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Update pickup information for an existing DHL Express pickup booking request

The Update Pickup service can be used to update pickup information for an existing DHL Express pickup booking request. Update of a previous successful pickups are subject to entire consolidated pickup if applicable. 

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
api_instance = swagger_client.PickupApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupermodelIoLogisticsExpressUpdatePickupRequest() # SupermodelIoLogisticsExpressUpdatePickupRequest | Details about the requested pickup updates
x_version = '2.12.0' # str | Interface version - do not change this field value  (default to 2.12.0)
dispatch_confirmation_number = 'dispatch_confirmation_number_example' # str | Shipment pickup confirmation number for example `PRG999126012345`
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Update pickup information for an existing DHL Express pickup booking request
    api_response = api_instance.exp_api_pickups_update(body, x_version, dispatch_confirmation_number, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PickupApi->exp_api_pickups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupermodelIoLogisticsExpressUpdatePickupRequest**](SupermodelIoLogisticsExpressUpdatePickupRequest.md)| Details about the requested pickup updates | 
 **x_version** | **str**| Interface version - do not change this field value  | [default to 2.12.0]
 **dispatch_confirmation_number** | **str**| Shipment pickup confirmation number for example &#x60;PRG999126012345&#x60; | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressUpdatePickupResponse**](SupermodelIoLogisticsExpressUpdatePickupResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

