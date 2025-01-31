# SupermodelIoLogisticsExpressTrackingResponseShipments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_tracking_number** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**shipment_timestamp** | **str** |  | [optional] 
**product_code** | **str** | DHL product code | [optional] 
**description** | **str** |  | [optional] 
**shipper_details** | [**SupermodelIoLogisticsExpressTrackingResponseShipperDetails**](SupermodelIoLogisticsExpressTrackingResponseShipperDetails.md) |  | [optional] 
**receiver_details** | [**SupermodelIoLogisticsExpressTrackingResponseReceiverDetails**](SupermodelIoLogisticsExpressTrackingResponseReceiverDetails.md) |  | [optional] 
**total_weight** | **float** |  | [optional] 
**unit_of_measurements** | **str** |  | [optional] 
**shipper_references** | [**list[SupermodelIoLogisticsExpressReference]**](SupermodelIoLogisticsExpressReference.md) |  | [optional] 
**events** | [**list[SupermodelIoLogisticsExpressTrackingResponseEvents]**](SupermodelIoLogisticsExpressTrackingResponseEvents.md) |  | 
**number_of_pieces** | **float** |  | [optional] 
**pieces** | [**list[SupermodelIoLogisticsExpressTrackingResponsePieces]**](SupermodelIoLogisticsExpressTrackingResponsePieces.md) |  | [optional] 
**estimated_delivery_date** | **str** |  | [optional] 
**children_shipment_identification_numbers** | **list[str]** |  | [optional] 
**controlled_access_data_codes** | **list[str]** | controlled access data codes such as &#x27;SHPR_CTY&#x27; for shipper&#x27;s city, &#x27;CNSGN_CTY&#x27; for consignee&#x27;s city, &#x27;SVP_URL&#x27; for service point URL, &#x27;SVP_FAC&#x27; for service point facility code and &#x27;SIGN_NM&#x27; for signatory name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

