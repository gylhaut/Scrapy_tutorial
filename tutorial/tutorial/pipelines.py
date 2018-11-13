# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class JiangRoompagePipeline(object):
    def __init__(self):
        # 初始化一个文件
        self.file_name = open("jiangroom.json", "w")

    def process_item(self, item, spider):
        # 这里是将item先转换成字典，在又字典转换成字符串
        # json.dumps转换时对中文默认使用的ascii编码.想输出真正的中文需要指定 ensure_ascii=False
        # 将最后的item 写入到文件中
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file_name.write(text)
        return item

    def close_spider(self):
        self.file_name.close()