# -*- coding: utf-8 -*-
# Scrapy imports
import scrapy
from ..zoidberg_spider import ZoidbergSpider
"""
Spiders for the Spain.
country:
 name: spain
 code: es
 domains: ["elatleta.com", "femede.es"]
"""

class ElAtletaComSpider(ZoidbergSpider):
    """
    Extends Zoidberg Base Spider for elatleta.com domain/source
    """
    name = "elatleta.com"

    def __init__(self, doctor_regex=None, urls=None, path='default', *args, **kwargs):
        super(ElAtletaComSpider, self).__init__(doctor_regex=doctor_regex, urls=urls, path=path, name=self.name, *args,
                                                **kwargs)

    def parse(self, response):
        """
        :param response: response of the web page
        :return: item and next page to parse
        """
        message_list = response.xpath(
            '//li[@class="postbit postbitim postcontainer old"]')
        # ITERATE MESSAGE IN A PAGE
        for m in message_list:
            author = m.xpath('.//a[@class="username offline popupctrl"]/strong/text()').extract_first()
            date = m.xpath('.//span[@class="date"]/text()').extract()[0]
            text = m.xpath('.//blockquote[@class="postcontent restore"]/text()')[0]
            find = text.re(self.doctor_regex)
            if len(find) > 0:
                yield {
                    'author': author,
                    'text': text.extract(),
                    'source': self.name,
                    'date': date,
                    'url': response.url
                }

        # NEXT PAGE FOLLOW LINK
        next_page = response.xpath(
            '//a[@rel="next"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


class FemedeEsSpider(ZoidbergSpider):
    """
    Extends Zoidberg Base Spider for femede.es domain/source
    """
    name = "femede.es"

    def __init__(self, doctor_regex=None, urls=None, path='default', *args, **kwargs):
        super(FemedeEsSpider, self).__init__(doctor_regex=doctor_regex, urls=urls, path=path, name=self.name, *args,
                                             **kwargs)

    def parse(self, response):
        """
        :param response: response of the web page
        :return: item and next page to parse
        """
        text_list = response.xpath('//span[@class="postbody"]')
        author_list = response.xpath('//span[@class="name"]/b/text()').extract()
        info_list = response.xpath('//span[@class="postdetails"]/text()').extract()
        date_list = [i.replace('Publicado: ', '') for i in info_list if "Publicado" in i]
        # ITERATE MESSAGE IN A PAGE
        for i in range(0, len(text_list)):
            text = text_list[i].xpath('.//text()')
            find = text.re(self.doctor_regex)
            if len(find) > 0:
                yield {
                    'author': author_list[i],
                    'text': "".join(text.extract()),
                    'source': self.name,
                    'date': date_list[i],
                    'url': response.url
                }

        # NEXT PAGE FOLLOW LINK
        next_page = response.xpath(
            '//a[text()="Siguiente"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
