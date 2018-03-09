# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter, CsvItemExporter
from pathlib import Path


class CleanItemsPipeline(object):
    """
    Function to clean the items
    TODO: make uniform data format
    """
    def process_item(self, item, spider):
        item['text'] = item['text'].replace('\r', '').replace('\n', '').replace('\t', '')
        print('object: ')
        print(object)
        item['date'] = item['date']
        return item


class JsonPipeline(object):
    """
    PipeLine that writes a jsonline file
    """
    def open_spider(self, spider):
        self.file = open(spider.path, 'ab')
        self.exporter = JsonLinesItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class CsvPipeline(object):
    """
    PipeLine that writes a csv file
    """
    def open_spider(self, spider):
        include_headers_line = not Path(spider.path).is_file()
        self.file = open(spider.path, 'ab')
        self.exporter = CsvItemExporter(self.file, include_headers_line=include_headers_line, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
