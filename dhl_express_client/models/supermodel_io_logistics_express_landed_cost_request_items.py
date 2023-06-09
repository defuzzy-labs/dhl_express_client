# coding: utf-8

"""
    DHL Express APIs (MyDHL API)

    Welcome to the official DHL Express APIs (MyDHL API) below are the published API Documentation to fulfill your shipping needs with DHL Express.       Please follow the process described [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--get-access) to request access to the DHL Express - MyDHL API services    In case you already have DHL Express - MyDHL API Service credentials please ensure to use the endpoints/environments listed  [here](https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/user-guide--environments)   # noqa: E501

    OpenAPI spec version: 2.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SupermodelIoLogisticsExpressLandedCostRequestItems(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'number': 'float',
        'name': 'str',
        'description': 'str',
        'manufacturer_country': 'str',
        'part_number': 'str',
        'quantity': 'float',
        'quantity_type': 'str',
        'unit_price': 'float',
        'unit_price_currency_code': 'str',
        'customs_value': 'float',
        'customs_value_currency_code': 'str',
        'commodity_code': 'str',
        'weight': 'float',
        'weight_unit_of_measurement': 'str',
        'category': 'str',
        'brand': 'str',
        'goods_characteristics': 'list[SupermodelIoLogisticsExpressLandedCostRequestGoodsCharacteristics]',
        'additional_quantity_definitions': 'list[SupermodelIoLogisticsExpressLandedCostRequestAdditionalQuantityDefinitions]',
        'estimated_tariff_rate_type': 'str'
    }

    attribute_map = {
        'number': 'number',
        'name': 'name',
        'description': 'description',
        'manufacturer_country': 'manufacturerCountry',
        'part_number': 'partNumber',
        'quantity': 'quantity',
        'quantity_type': 'quantityType',
        'unit_price': 'unitPrice',
        'unit_price_currency_code': 'unitPriceCurrencyCode',
        'customs_value': 'customsValue',
        'customs_value_currency_code': 'customsValueCurrencyCode',
        'commodity_code': 'commodityCode',
        'weight': 'weight',
        'weight_unit_of_measurement': 'weightUnitOfMeasurement',
        'category': 'category',
        'brand': 'brand',
        'goods_characteristics': 'goodsCharacteristics',
        'additional_quantity_definitions': 'additionalQuantityDefinitions',
        'estimated_tariff_rate_type': 'estimatedTariffRateType'
    }

    def __init__(self, number=None, name=None, description=None, manufacturer_country=None, part_number=None, quantity=None, quantity_type=None, unit_price=None, unit_price_currency_code=None, customs_value=None, customs_value_currency_code=None, commodity_code=None, weight=None, weight_unit_of_measurement=None, category=None, brand=None, goods_characteristics=None, additional_quantity_definitions=None, estimated_tariff_rate_type=None):  # noqa: E501
        """SupermodelIoLogisticsExpressLandedCostRequestItems - a model defined in Swagger"""  # noqa: E501
        self._number = None
        self._name = None
        self._description = None
        self._manufacturer_country = None
        self._part_number = None
        self._quantity = None
        self._quantity_type = None
        self._unit_price = None
        self._unit_price_currency_code = None
        self._customs_value = None
        self._customs_value_currency_code = None
        self._commodity_code = None
        self._weight = None
        self._weight_unit_of_measurement = None
        self._category = None
        self._brand = None
        self._goods_characteristics = None
        self._additional_quantity_definitions = None
        self._estimated_tariff_rate_type = None
        self.discriminator = None
        self.number = number
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if manufacturer_country is not None:
            self.manufacturer_country = manufacturer_country
        if part_number is not None:
            self.part_number = part_number
        self.quantity = quantity
        if quantity_type is not None:
            self.quantity_type = quantity_type
        self.unit_price = unit_price
        self.unit_price_currency_code = unit_price_currency_code
        if customs_value is not None:
            self.customs_value = customs_value
        if customs_value_currency_code is not None:
            self.customs_value_currency_code = customs_value_currency_code
        if commodity_code is not None:
            self.commodity_code = commodity_code
        if weight is not None:
            self.weight = weight
        if weight_unit_of_measurement is not None:
            self.weight_unit_of_measurement = weight_unit_of_measurement
        if category is not None:
            self.category = category
        if brand is not None:
            self.brand = brand
        if goods_characteristics is not None:
            self.goods_characteristics = goods_characteristics
        if additional_quantity_definitions is not None:
            self.additional_quantity_definitions = additional_quantity_definitions
        if estimated_tariff_rate_type is not None:
            self.estimated_tariff_rate_type = estimated_tariff_rate_type

    @property
    def number(self):
        """Gets the number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Line item number  # noqa: E501

        :return: The number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: float
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Line item number  # noqa: E501

        :param number: The number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: float
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def name(self):
        """Gets the name of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Name of the item  # noqa: E501

        :return: The name of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Name of the item  # noqa: E501

        :param name: The name of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Item full description  # noqa: E501

        :return: The description of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Item full description  # noqa: E501

        :param description: The description of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def manufacturer_country(self):
        """Gets the manufacturer_country of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        ISO Country code of the goods manufacturer  # noqa: E501

        :return: The manufacturer_country of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_country

    @manufacturer_country.setter
    def manufacturer_country(self, manufacturer_country):
        """Sets the manufacturer_country of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        ISO Country code of the goods manufacturer  # noqa: E501

        :param manufacturer_country: The manufacturer_country of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._manufacturer_country = manufacturer_country

    @property
    def part_number(self):
        """Gets the part_number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        SKU number  # noqa: E501

        :return: The part_number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """Sets the part_number of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        SKU number  # noqa: E501

        :param part_number: The part_number of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._part_number = part_number

    @property
    def quantity(self):
        """Gets the quantity of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Total quantity of the item(s) to be shipped.  # noqa: E501

        :return: The quantity of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Total quantity of the item(s) to be shipped.  # noqa: E501

        :param quantity: The quantity of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def quantity_type(self):
        """Gets the quantity_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Please provide quantitiy type. prt - part, box - box  # noqa: E501

        :return: The quantity_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._quantity_type

    @quantity_type.setter
    def quantity_type(self, quantity_type):
        """Sets the quantity_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Please provide quantitiy type. prt - part, box - box  # noqa: E501

        :param quantity_type: The quantity_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["prt", "box"]  # noqa: E501
        if quantity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quantity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quantity_type, allowed_values)
            )

        self._quantity_type = quantity_type

    @property
    def unit_price(self):
        """Gets the unit_price of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Product Unit price  # noqa: E501

        :return: The unit_price of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: float
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Product Unit price  # noqa: E501

        :param unit_price: The unit_price of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: float
        """
        if unit_price is None:
            raise ValueError("Invalid value for `unit_price`, must not be `None`")  # noqa: E501

        self._unit_price = unit_price

    @property
    def unit_price_currency_code(self):
        """Gets the unit_price_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Currency code of the Unit Price  # noqa: E501

        :return: The unit_price_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._unit_price_currency_code

    @unit_price_currency_code.setter
    def unit_price_currency_code(self, unit_price_currency_code):
        """Sets the unit_price_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Currency code of the Unit Price  # noqa: E501

        :param unit_price_currency_code: The unit_price_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """
        if unit_price_currency_code is None:
            raise ValueError("Invalid value for `unit_price_currency_code`, must not be `None`")  # noqa: E501

        self._unit_price_currency_code = unit_price_currency_code

    @property
    def customs_value(self):
        """Gets the customs_value of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        not used  # noqa: E501

        :return: The customs_value of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: float
        """
        return self._customs_value

    @customs_value.setter
    def customs_value(self, customs_value):
        """Sets the customs_value of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        not used  # noqa: E501

        :param customs_value: The customs_value of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: float
        """

        self._customs_value = customs_value

    @property
    def customs_value_currency_code(self):
        """Gets the customs_value_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        not used  # noqa: E501

        :return: The customs_value_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._customs_value_currency_code

    @customs_value_currency_code.setter
    def customs_value_currency_code(self, customs_value_currency_code):
        """Sets the customs_value_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        not used  # noqa: E501

        :param customs_value_currency_code: The customs_value_currency_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._customs_value_currency_code = customs_value_currency_code

    @property
    def commodity_code(self):
        """Gets the commodity_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        commodityCode is mandatory if estimatedTariffRateType ('derived_rate' or 'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>                              'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>            Can be provided with or without dots  # noqa: E501

        :return: The commodity_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, commodity_code):
        """Sets the commodity_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        commodityCode is mandatory if estimatedTariffRateType ('derived_rate' or 'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>                              'highest_rate' or 'lowest_rate' or 'center_rate') not provided in the request otherwise it is considered as Optional.<BR>            Can be provided with or without dots  # noqa: E501

        :param commodity_code: The commodity_code of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._commodity_code = commodity_code

    @property
    def weight(self):
        """Gets the weight of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Weight of the item  # noqa: E501

        :return: The weight of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Weight of the item  # noqa: E501

        :param weight: The weight of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def weight_unit_of_measurement(self):
        """Gets the weight_unit_of_measurement of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Unit of measurement  # noqa: E501

        :return: The weight_unit_of_measurement of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit_of_measurement

    @weight_unit_of_measurement.setter
    def weight_unit_of_measurement(self, weight_unit_of_measurement):
        """Sets the weight_unit_of_measurement of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Unit of measurement  # noqa: E501

        :param weight_unit_of_measurement: The weight_unit_of_measurement of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["metric", "imperial"]  # noqa: E501
        if weight_unit_of_measurement not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_unit_of_measurement` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_unit_of_measurement, allowed_values)
            )

        self._weight_unit_of_measurement = weight_unit_of_measurement

    @property
    def category(self):
        """Gets the category of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Category code of the Item.<BR>            101 - Coats & Jacket<BR>            102 - Blazers<BR>            103 - Suits<BR>            104 - Ensembles<BR>            105 - Trousers<BR>            106 - Shirts & Blouses<BR>            107 - Dresses<BR>            108 - Skirts<BR>            109 - Jerseys, Sweatshirts & Pullovers<BR>            110 - Sports & Swimwear<BR>            111 - Night & Underwear<BR>            112 - T-Shirts<BR>            113 - Tights & Leggings<BR>            114 - Socks <BR>            115 - Baby Clothes<BR>            116 - Clothing Accessories<BR>            201 - Sneakers<BR>            202 - Athletic Footwear<BR>            203 - Leather Footwear<BR>            204 - Textile & Other Footwear<BR>            301 - Spectacle Lenses<BR>            302 - Sunglasses<BR>            303 - Eyewear Frames<BR>            304 - Contact Lenses<BR>            401 - Watches<BR>            402 - Jewelry<BR>            403 - Suitcases & Briefcases<BR>            404 - Handbags<BR>            405 - Wallets & Little Cases<BR>            406 - Bags & Containers<BR>            501 - Beer<BR>            502 - Spirits<BR>            503 - Wine<BR>            504 - Cider, Perry & Rice Wine<BR>            601 - Bottled Water<BR>            602 - Soft Drinks<BR>            603 - Juices<BR>            604 - Coffee<BR>            605 - Tea<BR>            606 - Cocoa<BR>            701 - Dairy Products & Eggs<BR>            702 - Meat<BR>            703 - Fish & Seafood<BR>            704 - Fruits & Nuts<BR>            705 - Vegetables<BR>            706 - Bread & Cereal Products<BR>            707 - Oils & Fats<BR>            708 - Sauces & Spices<BR>            709 - Convenience Food<BR>            710 - Spreads & Sweeteners<BR>            711 - Baby Food<BR>            712 - Pet Food<BR>            801 - Cigarettes<BR>            802 - Smoking Tobacco<BR>            803 - Cigars<BR>            804 - E-Cigarettes<BR>            901 - Household Cleaners<BR>            902 - Dishwashing Detergents<BR>            903 - Polishes<BR>            904 - Room Scents<BR>            905 - Insecticides<BR>            1001 - Cosmetics<BR>            1002 - Skin Care<BR>            1003 - Personal Care<BR>            1004 - Fragrances<BR>            1101 - Toilet Paper<BR>            1102 - Paper Tissues<BR>            1103 - Household Paper<BR>            1104 - Feminine Hygiene<BR>            1105 - Baby Diapers<BR>            1106 - Incontinence<BR>            1202 - TV, Radio & Multimedia<BR>            1203 - TV Peripheral Devices<BR>            1204 - Telephony<BR>            1205 - Computing<BR>            1206 - Drones<BR>            1301 - Refrigerators<BR>            1302 - Freezers<BR>            1303 - Dishwashing Machines<BR>            1304 - Washing Machines<BR>            1305 - Cookers & Oven<BR>            1306 - Vacuum Cleaners<BR>            1307 - Small Kitchen Appliances<BR>            1308 - Hair Clippers<BR>            1309 - Irons<BR>            1310 - Toasters<BR>            1311 - Grills & Roasters<BR>            1312 - Hair Dryers<BR>            1313 - Coffee Machines<BR>            1314 - Microwave Ovens<BR>            1315 - Electric Kettles<BR>            1401 - Seats & Sofas<BR>            1402 - Beds<BR>            1403 - Mattresses<BR>            1404 - Closets, Nightstands & Dressers<BR>            1405 - Lamps & Lighting<BR>            1406 - Floor Covering<BR>            1407 - Kitchen Furniture<BR>            1408 - Plastic & Other Furniture<BR>            1501 - Analgesics<BR>            1502 - Cold & Cough Remedies<BR>            1503 - Digestives & Intestinal Remedies<BR>            1504 - Skin Treatment<BR>            1505 - Vitamins & Minerals<BR>            1506 - Hand Sanitizer <BR>            1601 - Toys & Games<BR>            1602 - Musical Instruments<BR>            1603 - Sports Equipment  # noqa: E501

        :return: The category of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Category code of the Item.<BR>            101 - Coats & Jacket<BR>            102 - Blazers<BR>            103 - Suits<BR>            104 - Ensembles<BR>            105 - Trousers<BR>            106 - Shirts & Blouses<BR>            107 - Dresses<BR>            108 - Skirts<BR>            109 - Jerseys, Sweatshirts & Pullovers<BR>            110 - Sports & Swimwear<BR>            111 - Night & Underwear<BR>            112 - T-Shirts<BR>            113 - Tights & Leggings<BR>            114 - Socks <BR>            115 - Baby Clothes<BR>            116 - Clothing Accessories<BR>            201 - Sneakers<BR>            202 - Athletic Footwear<BR>            203 - Leather Footwear<BR>            204 - Textile & Other Footwear<BR>            301 - Spectacle Lenses<BR>            302 - Sunglasses<BR>            303 - Eyewear Frames<BR>            304 - Contact Lenses<BR>            401 - Watches<BR>            402 - Jewelry<BR>            403 - Suitcases & Briefcases<BR>            404 - Handbags<BR>            405 - Wallets & Little Cases<BR>            406 - Bags & Containers<BR>            501 - Beer<BR>            502 - Spirits<BR>            503 - Wine<BR>            504 - Cider, Perry & Rice Wine<BR>            601 - Bottled Water<BR>            602 - Soft Drinks<BR>            603 - Juices<BR>            604 - Coffee<BR>            605 - Tea<BR>            606 - Cocoa<BR>            701 - Dairy Products & Eggs<BR>            702 - Meat<BR>            703 - Fish & Seafood<BR>            704 - Fruits & Nuts<BR>            705 - Vegetables<BR>            706 - Bread & Cereal Products<BR>            707 - Oils & Fats<BR>            708 - Sauces & Spices<BR>            709 - Convenience Food<BR>            710 - Spreads & Sweeteners<BR>            711 - Baby Food<BR>            712 - Pet Food<BR>            801 - Cigarettes<BR>            802 - Smoking Tobacco<BR>            803 - Cigars<BR>            804 - E-Cigarettes<BR>            901 - Household Cleaners<BR>            902 - Dishwashing Detergents<BR>            903 - Polishes<BR>            904 - Room Scents<BR>            905 - Insecticides<BR>            1001 - Cosmetics<BR>            1002 - Skin Care<BR>            1003 - Personal Care<BR>            1004 - Fragrances<BR>            1101 - Toilet Paper<BR>            1102 - Paper Tissues<BR>            1103 - Household Paper<BR>            1104 - Feminine Hygiene<BR>            1105 - Baby Diapers<BR>            1106 - Incontinence<BR>            1202 - TV, Radio & Multimedia<BR>            1203 - TV Peripheral Devices<BR>            1204 - Telephony<BR>            1205 - Computing<BR>            1206 - Drones<BR>            1301 - Refrigerators<BR>            1302 - Freezers<BR>            1303 - Dishwashing Machines<BR>            1304 - Washing Machines<BR>            1305 - Cookers & Oven<BR>            1306 - Vacuum Cleaners<BR>            1307 - Small Kitchen Appliances<BR>            1308 - Hair Clippers<BR>            1309 - Irons<BR>            1310 - Toasters<BR>            1311 - Grills & Roasters<BR>            1312 - Hair Dryers<BR>            1313 - Coffee Machines<BR>            1314 - Microwave Ovens<BR>            1315 - Electric Kettles<BR>            1401 - Seats & Sofas<BR>            1402 - Beds<BR>            1403 - Mattresses<BR>            1404 - Closets, Nightstands & Dressers<BR>            1405 - Lamps & Lighting<BR>            1406 - Floor Covering<BR>            1407 - Kitchen Furniture<BR>            1408 - Plastic & Other Furniture<BR>            1501 - Analgesics<BR>            1502 - Cold & Cough Remedies<BR>            1503 - Digestives & Intestinal Remedies<BR>            1504 - Skin Treatment<BR>            1505 - Vitamins & Minerals<BR>            1506 - Hand Sanitizer <BR>            1601 - Toys & Games<BR>            1602 - Musical Instruments<BR>            1603 - Sports Equipment  # noqa: E501

        :param category: The category of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def brand(self):
        """Gets the brand of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Item's brand  # noqa: E501

        :return: The brand of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Item's brand  # noqa: E501

        :param brand: The brand of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def goods_characteristics(self):
        """Gets the goods_characteristics of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501


        :return: The goods_characteristics of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressLandedCostRequestGoodsCharacteristics]
        """
        return self._goods_characteristics

    @goods_characteristics.setter
    def goods_characteristics(self, goods_characteristics):
        """Sets the goods_characteristics of this SupermodelIoLogisticsExpressLandedCostRequestItems.


        :param goods_characteristics: The goods_characteristics of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressLandedCostRequestGoodsCharacteristics]
        """

        self._goods_characteristics = goods_characteristics

    @property
    def additional_quantity_definitions(self):
        """Gets the additional_quantity_definitions of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501


        :return: The additional_quantity_definitions of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: list[SupermodelIoLogisticsExpressLandedCostRequestAdditionalQuantityDefinitions]
        """
        return self._additional_quantity_definitions

    @additional_quantity_definitions.setter
    def additional_quantity_definitions(self, additional_quantity_definitions):
        """Sets the additional_quantity_definitions of this SupermodelIoLogisticsExpressLandedCostRequestItems.


        :param additional_quantity_definitions: The additional_quantity_definitions of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: list[SupermodelIoLogisticsExpressLandedCostRequestAdditionalQuantityDefinitions]
        """

        self._additional_quantity_definitions = additional_quantity_definitions

    @property
    def estimated_tariff_rate_type(self):
        """Gets the estimated_tariff_rate_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501

        Please enter Tariff Rate Type - default_rate,derived_rate,highest_rate,center_rate,lowest_rate  # noqa: E501

        :return: The estimated_tariff_rate_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :rtype: str
        """
        return self._estimated_tariff_rate_type

    @estimated_tariff_rate_type.setter
    def estimated_tariff_rate_type(self, estimated_tariff_rate_type):
        """Sets the estimated_tariff_rate_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.

        Please enter Tariff Rate Type - default_rate,derived_rate,highest_rate,center_rate,lowest_rate  # noqa: E501

        :param estimated_tariff_rate_type: The estimated_tariff_rate_type of this SupermodelIoLogisticsExpressLandedCostRequestItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["default_rate", "derived_rate", "highest_rate", "center_rate", "lowest_rate"]  # noqa: E501
        if estimated_tariff_rate_type not in allowed_values:
            raise ValueError(
                "Invalid value for `estimated_tariff_rate_type` ({0}), must be one of {1}"  # noqa: E501
                .format(estimated_tariff_rate_type, allowed_values)
            )

        self._estimated_tariff_rate_type = estimated_tariff_rate_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SupermodelIoLogisticsExpressLandedCostRequestItems, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SupermodelIoLogisticsExpressLandedCostRequestItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
