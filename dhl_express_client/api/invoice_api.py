# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services    In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments)   # noqa: E501

    OpenAPI spec version: 2.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dhl_express_client.api_client import ApiClient


class InvoiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def exp_api_shipments_invoice_data(self, body, **kwargs):  # noqa: E501
        """Upload Commercial invoice data  # noqa: E501

        ## Upload invoice data The upload invoice data service can be used to upload Commerical Invoice data without Shipment Identification Number for your DHL Express shipment. Customer can provide Commercial Invoice data before Shipment Data via Create Shipment flow or vice versa.  Important Note: UploadInvoiceData service is not enabled by default and must be requested per customer.Use of this service is only enabled on exceptional basis and DHL Express recommends to submit shipment requests together with a commercial invoice data. To enable use of UploadInvoiceData service, please contact your DHL Express IT representative. To use UploadInvoiceData service, it is required that \"PM\" service code is provided in MyDHL API Create Shipment request. \"PM\" service code is not enabled by default for the customers, and needs to be enabled upon request.  When Shipment is created via MyDHL API Create Shipment service before uploading the Commercial Invoice (CIN) data,it is mandatory to provide the Shipment Identification Number as received in MyDHL API Create Shipment service Response. When Commercial Invoice (CIN) data is uploaded prior to creating a shipment via MyDHL API Create Shipment service, it is  mandatory to provide Invoice Reference Number with Invoice Reference Type value \"CU\" and Shipper Account Number.  These elements are mandatory to facilitate an effective data merge of the Commercial Invoice (CIN) data with Shipment Data. As an output customer will receive Notification element value '0' on successful upload of Commercial Invoice (CIN) data. DHL backend application performs the subsequent data merging process of the Shipment Data and Commercial Invoice data.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exp_api_shipments_invoice_data(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID body: Details about the Commercial Invoice data to be uploaded (required)
        :param str message_reference: Please provide message reference 
        :param str message_reference_date: Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2
        :param str plugin_name: Please provide name of the plugin (applicable to 3PV only) 
        :param str plugin_version: Please provide version of the plugin (applicable to 3PV only) 
        :param str shipping_system_platform_name: Please provide name of the shipping platform(applicable to 3PV only) 
        :param str shipping_system_platform_version: Please provide version of the shipping platform (applicable to 3PV only) 
        :param str webstore_platform_name: Please provide name of the webstore platform (applicable to 3PV only) 
        :param str webstore_platform_version: Please provide version of the webstore platform (applicable to 3PV only) 
        :return: SupermodelIoLogisticsExpressUploadInvoiceDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.exp_api_shipments_invoice_data_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.exp_api_shipments_invoice_data_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def exp_api_shipments_invoice_data_with_http_info(self, body, **kwargs):  # noqa: E501
        """Upload Commercial invoice data  # noqa: E501

        ## Upload invoice data The upload invoice data service can be used to upload Commerical Invoice data without Shipment Identification Number for your DHL Express shipment. Customer can provide Commercial Invoice data before Shipment Data via Create Shipment flow or vice versa.  Important Note: UploadInvoiceData service is not enabled by default and must be requested per customer.Use of this service is only enabled on exceptional basis and DHL Express recommends to submit shipment requests together with a commercial invoice data. To enable use of UploadInvoiceData service, please contact your DHL Express IT representative. To use UploadInvoiceData service, it is required that \"PM\" service code is provided in MyDHL API Create Shipment request. \"PM\" service code is not enabled by default for the customers, and needs to be enabled upon request.  When Shipment is created via MyDHL API Create Shipment service before uploading the Commercial Invoice (CIN) data,it is mandatory to provide the Shipment Identification Number as received in MyDHL API Create Shipment service Response. When Commercial Invoice (CIN) data is uploaded prior to creating a shipment via MyDHL API Create Shipment service, it is  mandatory to provide Invoice Reference Number with Invoice Reference Type value \"CU\" and Shipper Account Number.  These elements are mandatory to facilitate an effective data merge of the Commercial Invoice (CIN) data with Shipment Data. As an output customer will receive Notification element value '0' on successful upload of Commercial Invoice (CIN) data. DHL backend application performs the subsequent data merging process of the Shipment Data and Commercial Invoice data.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.exp_api_shipments_invoice_data_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SupermodelIoLogisticsExpressUploadInvoiceDataRequestSID body: Details about the Commercial Invoice data to be uploaded (required)
        :param str message_reference: Please provide message reference 
        :param str message_reference_date: Optional reference date in the  HTTP-date format https://tools.ietf.org/html/rfc7231#section-7.1.1.2
        :param str plugin_name: Please provide name of the plugin (applicable to 3PV only) 
        :param str plugin_version: Please provide version of the plugin (applicable to 3PV only) 
        :param str shipping_system_platform_name: Please provide name of the shipping platform(applicable to 3PV only) 
        :param str shipping_system_platform_version: Please provide version of the shipping platform (applicable to 3PV only) 
        :param str webstore_platform_name: Please provide name of the webstore platform (applicable to 3PV only) 
        :param str webstore_platform_version: Please provide version of the webstore platform (applicable to 3PV only) 
        :return: SupermodelIoLogisticsExpressUploadInvoiceDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'message_reference', 'message_reference_date', 'plugin_name', 'plugin_version', 'shipping_system_platform_name', 'shipping_system_platform_version', 'webstore_platform_name', 'webstore_platform_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method exp_api_shipments_invoice_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `exp_api_shipments_invoice_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'message_reference' in params:
            header_params['Message-Reference'] = params['message_reference']  # noqa: E501
        if 'message_reference_date' in params:
            header_params['Message-Reference-Date'] = params['message_reference_date']  # noqa: E501
        if 'plugin_name' in params:
            header_params['Plugin-Name'] = params['plugin_name']  # noqa: E501
        if 'plugin_version' in params:
            header_params['Plugin-Version'] = params['plugin_version']  # noqa: E501
        if 'shipping_system_platform_name' in params:
            header_params['Shipping-System-Platform-Name'] = params['shipping_system_platform_name']  # noqa: E501
        if 'shipping_system_platform_version' in params:
            header_params['Shipping-System-Platform-Version'] = params['shipping_system_platform_version']  # noqa: E501
        if 'webstore_platform_name' in params:
            header_params['Webstore-Platform-Name'] = params['webstore_platform_name']  # noqa: E501
        if 'webstore_platform_version' in params:
            header_params['Webstore-Platform-Version'] = params['webstore_platform_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/invoices/upload-invoice-data', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SupermodelIoLogisticsExpressUploadInvoiceDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
