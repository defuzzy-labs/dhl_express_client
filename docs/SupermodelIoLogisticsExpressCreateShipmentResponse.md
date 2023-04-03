# SupermodelIoLogisticsExpressCreateShipmentResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | URL where the request has been sent to | [optional] 
**shipment_tracking_number** | **str** | Here you will receive Shipment Identification Number of your package | [optional] 
**cancel_pickup_url** | **str** | If you requested pickup for your shipment you can use this URL to cancel the pickup | [optional] 
**tracking_url** | **str** | You can use ths URL to track your shipment | [optional] 
**dispatch_confirmation_number** | **str** | If you asked for pickup service here you will find Dispach Confirmation Number which identifies your pickup booking | [optional] 
**packages** | [**list[SupermodelIoLogisticsExpressCreateShipmentResponsePackages]**](SupermodelIoLogisticsExpressCreateShipmentResponsePackages.md) | Here you can find information for all pieces your shipment is having like Piece Identification Number  | [optional] 
**documents** | [**list[SupermodelIoLogisticsExpressCreateShipmentResponseDocuments1]**](SupermodelIoLogisticsExpressCreateShipmentResponseDocuments1.md) | Here you can find all documents created for the shipment like Transport and WaybillDoc labels, Invoice, Receipt | [optional] 
**on_demand_delivery_url** | **str** | In this field you will find the On Demand Delivery (ODD) URL link if requested | [optional] 
**shipment_details** | [**list[SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails]**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentDetails.md) | Here you can find additional information related to your shipment when you ask for it in the request | [optional] 
**shipment_charges** | [**list[SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges]**](SupermodelIoLogisticsExpressCreateShipmentResponseShipmentCharges.md) | Here you can find rates related to your shipment | [optional] 
**barcode_info** | [**SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo**](SupermodelIoLogisticsExpressCreateShipmentResponseBarcodeInfo.md) |  | [optional] 
**estimated_delivery_date** | [**SupermodelIoLogisticsExpressCreateShipmentResponseEstimatedDeliveryDate**](SupermodelIoLogisticsExpressCreateShipmentResponseEstimatedDeliveryDate.md) |  | [optional] 
**warnings** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

