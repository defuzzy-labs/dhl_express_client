# Pickup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_requested** | **bool** | Please advise if a pickup is needed for this shipment | [default to False]
**close_time** | **str** | The latest time the location premises is available to dispatch the DHL Express shipment. (HH:MM)  | [optional] 
**location** | **str** | Provides information on where the package should be picked up by DHL courier. | [optional] 
**special_instructions** | [**list[PickupSpecialInstructions]**](PickupSpecialInstructions.md) | Details special pickup instructions you may wish to send to the DHL Courier. | [optional] 
**pickup_details** | [**PickupPickupDetails**](PickupPickupDetails.md) |  | [optional] 
**pickup_requestor_details** | [**PickupPickupRequestorDetails**](PickupPickupRequestorDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

