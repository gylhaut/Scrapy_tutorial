#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from tutorial.items import JiangRoomItem

from tutorial.items import RentalRoomItem

class QuotesSpider(scrapy.Spider):
    name = "JiangRoomSpider"
    allowed_domains = ['http://www.jiangroom.com/']

    # 构建动态的header
    headers = {
        'Host': 'http://www.jiangroom.com',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }

    def start_requests(self):
        url_rooms_count = 'http://www.jiangroom.com/queryRoomsCount'
        my_data = {'shortFlag': '0'}
        r = requests.post(url_rooms_count, data=my_data)
        rooms_count = float(r.text)
        print(type(rooms_count))
        # 这里规定只爬10次
       ## laypage_last
        for i in range(int(rooms_count)):
            # 拿到当前时间戳 拼接成url
            offset =i*12
            url = "http://www.jiangroom.com/queryRoomsAsync?offset=" + str(offset)
            # 发送请求 在pares中处理最后的返回结果
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # 拿到json数据
        datas = json.loads(response.text)
        # for data in datas:
        #     item =RentalRoomItem()
        #     item["source_id"] = 6 #jiangrooms
        #     item["room_id"] = data['id']
        #     item["customer_cell_id"]

        for data in datas:
            # 将我们需要的数据都解析出来 并交给CsdnhomepagePipeline管道处理
            item = JiangRoomItem()
            item["id"] = data['id']
            item["bedroomNameAbbr"] = data['bedroomNameAbbr']
            item["orientation"] = data['orientation']
            item["orientationName"] = data['orientationName']
            item["usableArea"] = data['usableArea']
            item["realityPrice"] = data['realityPrice']
            item["roomStatus"] = data['roomStatus']
            item["salesPromotion"] = data['salesPromotion']
            item["floorTotal"] = data['floorTotal']
            item["floorNum"] = data['floorNum']
            item["trafficDistance"] = data['trafficDistance']
            item["premiseAddress"] = data['premiseAddress']
            yield item
    # # def start_requests(self):
    # #     url = 'http://www.jycinema.com/frontUIWebapp/appserver/cinCinemaFilmViewService/findFilm'
    # #     form_data = {
    # #         'params': '''{"type":"queryFilm","cityName":"深圳市","cinemaId":"","statusRE":"RELEASE","channelCode":"J0002","channelId":"3"}'''
    # #     }
    # #     return [scrapy.FormRequest(url, formdata=form_data, headers=self.headers, callback=self.parse_item)]
    # #
    # # def parse(self, response):
    # #     # follow links to author pages
    # #     for href in response.css('.author + a::attr(href)'):
    # #         yield response.follow(href, self.parse_author)
    # #
    # #     # follow pagination links
    # #     for href in response.css('li.next a::attr(href)'):
    # #         yield response.follow(href, self.parse)
    #
    # # def parse_author(self, response):
    # #     def extract_with_css(query):
    # #         return response.css(query).extract_first().strip()
    # #
    # #     yield {
    # #         'name': extract_with_css('h3.author-title::text'),
    # #         'birthdate': extract_with_css('.author-born-date::text'),
    # #         'bio': extract_with_css('.author-description::text'),
    # #     }




