# SupermodelIoLogisticsExpressCreateShipmentRequestOnDemandDelivery

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_option** | **str** | Please choose from one of the delivery options | 
**location** | **str** | If delivery option is signatureDelivery please specify location where to leave the shipment | [optional] 
**special_instructions** | **str** | Please enter additional information that might be useful for the DHL Express courier | [optional] 
**gate_code** | **str** | Please provide entry code to gain access to an apartment complex or gate | [optional] 
**where_to_leave** | **str** | In ase your deliveryOption is &#x27;neighbour&#x27; please specify where to leave the package  | [optional] 
**neighbour_name** | **str** | In case you wish to leave the package with neighbour please provide the neighbour&#x27;s name | [optional] 
**neighbour_house_number** | **str** | In case you wish to leave the package with neighbour please provide the neighbour&#x27;s house number | [optional] 
**authorizer_name** | **str** | In case your delivery option is &#x27;signatureRelease&#x27; please provide name of the person who is authorized to sign and receive the package | [optional] 
**service_point_id** | **str** | In case your delivery option is &#x27;servicepoint&#x27; please provide unique DHL Express Service point location ID of where the parcel should be delieverd (please contact your local DHL Express Account Manager to obtain the list of the servicepoint IDs) | [optional] 
**requested_delivery_date** | **str** | for future use | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

