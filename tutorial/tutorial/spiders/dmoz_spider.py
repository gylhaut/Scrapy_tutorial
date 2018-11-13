#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/12 10:51
# @Author  : gylhaut
# @Site    : "http://www.cnblogs.com/gylhaut/"
# @File    : dmoz_spider.py
# @Software: PyCharm

import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    # 构建动态的header
    headers = {
        'Host': 'www.dankegongyu.com',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)