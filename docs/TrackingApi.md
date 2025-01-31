# swagger_client.TrackingApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_shipments_tracking**](TrackingApi.md#exp_api_shipments_tracking) | **GET** /shipments/{shipmentTrackingNumber}/tracking | Track a single DHL Express Shipment
[**exp_api_shipments_tracking_multi**](TrackingApi.md#exp_api_shipments_tracking_multi) | **GET** /tracking | Track a single or multiple DHL Express Shipments

# **exp_api_shipments_tracking**
> SupermodelIoLogisticsExpressTrackingResponse exp_api_shipments_tracking(shipment_tracking_number, x_version, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, request_gmt_offset_per_event=request_gmt_offset_per_event, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Track a single DHL Express Shipment

The Tracking service retrieves tracking statuses for a single DHL Express Shipment 

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
api_instance = swagger_client.TrackingApi(swagger_client.ApiClient(configuration))
shipment_tracking_number = 'shipment_tracking_number_example' # str | DHL Express shipment identification number
x_version = '2.12.0' # str | Interface version - do not change this field value  (default to 2.12.0)
tracking_view = 'all-checkpoints' # str |  (optional) (default to all-checkpoints)
level_of_detail = 'shipment' # str |  (optional) (default to shipment)
request_controlled_access_data_codes = true # bool | Query parameter to request to return values of controlled access code fields in response. (optional)
request_gmt_offset_per_event = true # bool | Query parameter to request to return GMT Offset of each event in response, for both shipment level and piece level. (optional)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
accept_language = 'eng' # str | Format {3-character language code} (optional) (default to eng)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Track a single DHL Express Shipment
    api_response = api_instance.exp_api_shipments_tracking(shipment_tracking_number, x_version, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, request_gmt_offset_per_event=request_gmt_offset_per_event, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingApi->exp_api_shipments_tracking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_tracking_number** | **str**| DHL Express shipment identification number | 
 **x_version** | **str**| Interface version - do not change this field value  | [default to 2.12.0]
 **tracking_view** | **str**|  | [optional] [default to all-checkpoints]
 **level_of_detail** | **str**|  | [optional] [default to shipment]
 **request_controlled_access_data_codes** | **bool**| Query parameter to request to return values of controlled access code fields in response. | [optional] 
 **request_gmt_offset_per_event** | **bool**| Query parameter to request to return GMT Offset of each event in response, for both shipment level and piece level. | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **accept_language** | **str**| Format {3-character language code} | [optional] [default to eng]
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressTrackingResponse**](SupermodelIoLogisticsExpressTrackingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exp_api_shipments_tracking_multi**
> SupermodelIoLogisticsExpressTrackingResponse exp_api_shipments_tracking_multi(x_version, shipment_tracking_number=shipment_tracking_number, piece_tracking_number=piece_tracking_number, shipment_reference=shipment_reference, shipment_reference_type=shipment_reference_type, shipper_account_number=shipper_account_number, date_range_from=date_range_from, date_range_to=date_range_to, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Track a single or multiple DHL Express Shipments

The Tracking service retrieves tracking statuses for a single or multiple DHL Express Shipments 

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
api_instance = swagger_client.TrackingApi(swagger_client.ApiClient(configuration))
x_version = '2.12.0' # str | Interface version - do not change this field value  (default to 2.12.0)
shipment_tracking_number = ['shipment_tracking_number_example'] # list[str] | DHL Express shipment identification number (optional)
piece_tracking_number = ['piece_tracking_number_example'] # list[str] | DHL Express shipment piece tracking number (optional)
shipment_reference = 'shipment_reference_example' # str | Shipment reference which was provided during the shipment label creation  (optional)
shipment_reference_type = 'shipment_reference_type_example' # str | Shipment reference type which was provided during the shipment label creation  (optional)
shipper_account_number = 'shipper_account_number_example' # str | Shipper DHL Express Account number under which the shipment label was created  (optional)
date_range_from = 'date_range_from_example' # str | When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the start of the period.  (optional)
date_range_to = 'date_range_to_example' # str | When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the end of the period.  (optional)
tracking_view = 'all-checkpoints' # str |  (optional) (default to all-checkpoints)
level_of_detail = 'shipment' # str |  (optional) (default to shipment)
request_controlled_access_data_codes = true # bool | Query parameter to request to return values of controlled access code fields in response. (optional)
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
accept_language = 'eng' # str | Format {3-character language code} (optional) (default to eng)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Track a single or multiple DHL Express Shipments
    api_response = api_instance.exp_api_shipments_tracking_multi(x_version, shipment_tracking_number=shipment_tracking_number, piece_tracking_number=piece_tracking_number, shipment_reference=shipment_reference, shipment_reference_type=shipment_reference_type, shipper_account_number=shipper_account_number, date_range_from=date_range_from, date_range_to=date_range_to, tracking_view=tracking_view, level_of_detail=level_of_detail, request_controlled_access_data_codes=request_controlled_access_data_codes, message_reference=message_reference, message_reference_date=message_reference_date, accept_language=accept_language, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TrackingApi->exp_api_shipments_tracking_multi: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_version** | **str**| Interface version - do not change this field value  | [default to 2.12.0]
 **shipment_tracking_number** | [**list[str]**](str.md)| DHL Express shipment identification number | [optional] 
 **piece_tracking_number** | [**list[str]**](str.md)| DHL Express shipment piece tracking number | [optional] 
 **shipment_reference** | **str**| Shipment reference which was provided during the shipment label creation  | [optional] 
 **shipment_reference_type** | **str**| Shipment reference type which was provided during the shipment label creation  | [optional] 
 **shipper_account_number** | **str**| Shipper DHL Express Account number under which the shipment label was created  | [optional] 
 **date_range_from** | **str**| When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the start of the period.  | [optional] 
 **date_range_to** | **str**| When tracking by Shipment reference you need to restrict the search by timeframe. Please provide the end of the period.  | [optional] 
 **tracking_view** | **str**|  | [optional] [default to all-checkpoints]
 **level_of_detail** | **str**|  | [optional] [default to shipment]
 **request_controlled_access_data_codes** | **bool**| Query parameter to request to return values of controlled access code fields in response. | [optional] 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **accept_language** | **str**| Format {3-character language code} | [optional] [default to eng]
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressTrackingResponse**](SupermodelIoLogisticsExpressTrackingResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

