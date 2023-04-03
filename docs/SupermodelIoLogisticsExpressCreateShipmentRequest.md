# SupermodelIoLogisticsExpressCreateShipmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**planned_shipping_date_and_time** | **str** | Identifies the date and time the package is tendered. Both the date and time portions of the string are expected to be used. The date should not be a past date or a date more than 10 days in the future. The time is the local time of the shipment based on the shipper&#x27;s time zone. The date component must be in the format: YYYY-MM-DD; the time component must be in the format: HH:MM:SS using a 24 hour clock. The date and time parts are separated by the letter T (e.g. 2006-06-26T17:00:00 GMT+01:00). | 
**pickup** | [**Pickup**](Pickup.md) |  | 
**product_code** | **str** | Please enter DHL Express Global Product code | 
**local_product_code** | **str** | Please enter DHL Express Local Product code. Important when shipping domestic products. | [optional] 
**get_rate_estimates** | **bool** | Please advise if you want to get rate estimates for given shipment | [optional] [default to False]
**accounts** | [**list[SupermodelIoLogisticsExpressAccount]**](SupermodelIoLogisticsExpressAccount.md) | Please enter all the DHL Express accounts and types to be used for this shipment | 
**value_added_services** | [**list[SupermodelIoLogisticsExpressValueAddedServices]**](SupermodelIoLogisticsExpressValueAddedServices.md) | This section communicates additional shipping services, such as Insurance (or Shipment Value Protection). | [optional] 
**output_image_properties** | [**SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties**](SupermodelIoLogisticsExpressCreateShipmentRequestOutputImageProperties.md) |  | [optional] 
**customer_references** | [**list[SupermodelIoLogisticsExpressReference]**](SupermodelIoLogisticsExpressReference.md) | Here you can declare your customer references | [optional] 
**identifiers** | [**list[SupermodelIoLogisticsExpressIdentifier]**](SupermodelIoLogisticsExpressIdentifier.md) | Identifiers section is on the shipment level where you can optionaly provide a DHL Express waybill number. This has to be enabled by your DHL Express IT contact. | [optional] 
**customer_details** | [**SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails**](SupermodelIoLogisticsExpressCreateShipmentRequestCustomerDetails.md) |  | 
**content** | [**SupermodelIoLogisticsExpressCreateShipmentRequestContent**](SupermodelIoLogisticsExpressCreateShipmentRequestContent.md) |  | 
**document_images** | [**SupermodelIoLogisticsExpressDocumentImages**](SupermodelIoLogisticsExpressDocumentImages.md) |  | [optional] 
**on_demand_delivery** | [**SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery**](SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery.md) |  | [optional] 
**request_ondemand_delivery_url** | **bool** | Determines whether to request the On Demand Delivery (ODD) link. When set to true it will provide an URL link for the specified Waybill Number, Shipper Account Number. The default value is false, no ODD link URL is provided in the response message. | [optional] 
**shipment_notification** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification]**](SupermodelIoLogisticsExpressCreateShipmentRequestShipmentNotification.md) | This is to support sending email notification once the shipment is created. The email will contain the basic information on the shipper, recipient, waybill number, and shipment information | [optional] 
**prepaid_charges** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidCharges]**](SupermodelIoLogisticsExpressCreateShipmentRequestPrepaidCharges.md) | Please provide any charges you have already paid for this shipment, like freight paid upfront. To allow using this section please contact your DHL Express representative | [optional] 
**get_transliterated_response** | **bool** | If set to true, response will return transliterated text of shipper and receiver details. | [optional] 
**estimated_delivery_date** | [**EstimatedDeliveryDate**](EstimatedDeliveryDate.md) |  | [optional] 
**get_additional_information** | [**list[SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformation]**](SupermodelIoLogisticsExpressCreateShipmentRequestGetAdditionalInformation.md) | Provides additional information in the response like service area details, routing code and pickup-related information | [optional] 
**parent_shipment** | [**SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment**](SupermodelIoLogisticsExpressCreateShipmentRequestParentShipment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

