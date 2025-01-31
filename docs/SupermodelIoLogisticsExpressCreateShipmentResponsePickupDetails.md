# SupermodelIoLogisticsExpressCreateShipmentResponsePickupDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_cutoff_date_and_time** | **str** | Pickup booking cutoff time | [optional] 
**cutoff_time_offset** | **str** | Pickup booking cutoff time in GMT offset | [optional] 
**pickup_earliest** | **str** | The DHL earliest time possible for pickup | [optional] 
**pickup_latest** | **str** | The DHL latest time possible for pickup | [optional] 
**pickup_cutoff_same_day_outbound_processing** | **str** | Local pickup cut off time which allows forwarding the shipment on the requested day. Any Pickup requested after this pickup cutoff time may have an impact on transit time. | [optional] 
**total_transit_days** | **str** | The number of transit days | [optional] 
**pickup_additional_days** | **str** | This is additional transit delays (in days) for shipment picked up from the mentioned city or postal area to arrival at the service area | [optional] 
**delivery_additional_days** | **str** | This is additional transit delays (in days) for shipment delivered to the mentioned city or postal area following arrival at the service area | [optional] 
**pickup_day_of_week** | **str** | Pickup day of the week number | [optional] 
**delivery_day_of_week** | **str** | Destination day of the week number | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

