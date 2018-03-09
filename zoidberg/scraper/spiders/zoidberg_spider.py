# -*- coding: utf-8 -*-
# Scrpay imports
import scrapy


class ZoidbergSpider(scrapy.Spider):
    """
    Base Spider for all Zoidberg's spiders that implement scrapy.Spider.
    """
    name = "zoidberg"

    def __init__(self, doctor_regex=None, urls=None, path=None, source=None, name=None, *args, **kwargs):
        """
        Init Zoidberg base spider
        :param doctor_regex: regex string of the doctor to search in the source
        :param urls: urls to start crawling
        :param path: path to save the output file
        :param source: source of the information
        :param name: name of the spider
        :param args:
        :param kwargs:
        """
        super(ZoidbergSpider, self).__init__(*args, **kwargs)
        self.doctor_regex = doctor_regex
        self.source = source
        self.start_urls = urls
        self.path = path
        self.name = name

    def parse(self, response):
        pass
