# ServicePointsRestResponseV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RestResponseStatus**](RestResponseStatus.md) |  | [optional] 
**search_address** | **str** | The address used for the search (value of request parameter &#x27;address&#x27;) | [optional] 
**search_location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**map_culture** | **str** | The culture parameter for Bing Maps API (derived from the country parameter in the request) | [optional] 
**map_language** | **str** | Map Culture Used for Third party Maps | [optional] 
**service_points** | [**list[ServicePoint]**](ServicePoint.md) | Array of the found Service Points. Each Service Point entity contains details about the service point. | [optional] 
**messages** | **list[str]** | Array of strings. Contains information messages  - e.g. required language is not available, result was filtered due to incoming holidays. | [optional] 
**translations** | [**Translations**](Translations.md) |  | [optional] 
**lite_mode** | **bool** | Indicates whether lite mode is acitvated or not. | [optional] 
**promotion** | [**Promotion**](Promotion.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

