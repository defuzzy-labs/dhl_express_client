# swagger_client.InvoiceApi

All URIs are relative to *https://api-mock.dhl.com/mydhlapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exp_api_shipments_invoice_data**](InvoiceApi.md#exp_api_shipments_invoice_data) | **POST** /invoices/upload-invoice-data | Upload Commercial invoice data

# **exp_api_shipments_invoice_data**
> SupermodelIoLogisticsExpressUploadInvoiceDataResponse exp_api_shipments_invoice_data(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)

Upload Commercial invoice data

## Upload invoice data The upload invoice data service can be used to upload Commerical Invoice data without Shipment Identification Number for your DHL Express shipment. Customer can provide Commercial Invoice data before Shipment Data via Create Shipment flow or vice versa.  Important Note: UploadInvoiceData service is not enabled by default and must be requested per customer.Use of this service is only enabled on exceptional basis and DHL Express recommends to submit shipment requests together with a commercial invoice data. To enable use of UploadInvoiceData service, please contact your DHL Express IT representative. To use UploadInvoiceData service, it is required that \"PM\" service code is provided in MyDHL API Create Shipment request. \"PM\" service code is not enabled by default for the customers, and needs to be enabled upon request.  When Shipment is created via MyDHL API Create Shipment service before uploading the Commercial Invoice (CIN) data,it is mandatory to provide the Shipment Identification Number as received in MyDHL API Create Shipment service Response. When Commercial Invoice (CIN) data is uploaded prior to creating a shipment via MyDHL API Create Shipment service, it is  mandatory to provide Invoice Reference Number with Invoice Reference Type value \"CU\" and Shipper Account Number.  These elements are mandatory to facilitate an effective data merge of the Commercial Invoice (CIN) data with Shipment Data. As an output customer will receive Notification element value '0' on successful upload of Commercial Invoice (CIN) data. DHL backend application performs the subsequent data merging process of the Shipment Data and Commercial Invoice data. 

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
api_instance = swagger_client.InvoiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID() # SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID | Details about the Commercial Invoice data to be uploaded
message_reference = 'message_reference_example' # str | Please provide message reference  (optional)
message_reference_date = 'message_reference_date_example' # str | Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 (optional)
plugin_name = 'plugin_name_example' # str | Please provide name of the plugin (applicable to 3PV only)  (optional)
plugin_version = 'plugin_version_example' # str | Please provide version of the plugin (applicable to 3PV only)  (optional)
shipping_system_platform_name = 'shipping_system_platform_name_example' # str | Please provide name of the shipping platform(applicable to 3PV only)  (optional)
shipping_system_platform_version = 'shipping_system_platform_version_example' # str | Please provide version of the shipping platform (applicable to 3PV only)  (optional)
webstore_platform_name = 'webstore_platform_name_example' # str | Please provide name of the webstore platform (applicable to 3PV only)  (optional)
webstore_platform_version = 'webstore_platform_version_example' # str | Please provide version of the webstore platform (applicable to 3PV only)  (optional)

try:
    # Upload Commercial invoice data
    api_response = api_instance.exp_api_shipments_invoice_data(body, message_reference=message_reference, message_reference_date=message_reference_date, plugin_name=plugin_name, plugin_version=plugin_version, shipping_system_platform_name=shipping_system_platform_name, shipping_system_platform_version=shipping_system_platform_version, webstore_platform_name=webstore_platform_name, webstore_platform_version=webstore_platform_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoiceApi->exp_api_shipments_invoice_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID**](SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID.md)| Details about the Commercial Invoice data to be uploaded | 
 **message_reference** | **str**| Please provide message reference  | [optional] 
 **message_reference_date** | **str**| Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2 | [optional] 
 **plugin_name** | **str**| Please provide name of the plugin (applicable to 3PV only)  | [optional] 
 **plugin_version** | **str**| Please provide version of the plugin (applicable to 3PV only)  | [optional] 
 **shipping_system_platform_name** | **str**| Please provide name of the shipping platform(applicable to 3PV only)  | [optional] 
 **shipping_system_platform_version** | **str**| Please provide version of the shipping platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_name** | **str**| Please provide name of the webstore platform (applicable to 3PV only)  | [optional] 
 **webstore_platform_version** | **str**| Please provide version of the webstore platform (applicable to 3PV only)  | [optional] 

### Return type

[**SupermodelIoLogisticsExpressUploadInvoiceDataResponse**](SupermodelIoLogisticsExpressUploadInvoiceDataResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

