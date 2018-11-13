# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class RentalRoomItem(scrapy.Item):
    Id = Field()
    source_id = Field()
    room_id = Field()
    customer_cell_id = Field()
    room_address = Field()
    customer_cell_address = Field()
    village_id = Field()
    village_name = Field()
    block_id = Field()
    block_name = Field()
    district_id = Field()
    district_name = Field()
    city_id = Field()
    city_name = Field()
    province_id = Field()
    province_name = Field()
    room_orient = Field()
    toilet_staus = Field()
    rental_type = Field()
    room_area = Field()
    room_type = Field()
    total_floor = Field()
    current_floor = Field()
    current_floor_desc = Field()
    rental_price = Field()
    subway_line = Field()
    subway_station = Field()
    distance_to_subway = Field()
    tag = Field()
    longitude = Field()
    latitude = Field()
    ts = Field()
    create_time = Field()


class JiangRoomItem(scrapy.Item):
    #id
    id =scrapy.Field()
    bedroomNameAbbr =scrapy.Field()
    orientation= scrapy.Field()
    orientationName = scrapy.Field()
    usableArea = scrapy.Field()
    realityPrice = scrapy.Field()
    roomStatus = scrapy.Field()
    salesPromotion = scrapy.Field()
    floorTotal = scrapy.Field()
    floorNum = scrapy.Field()
    trafficDistance = scrapy.Field()
    premiseAddress = scrapy.Field()