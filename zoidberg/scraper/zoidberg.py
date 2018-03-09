# -*- coding: utf-8 -*-

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import json
import os

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s', 'LOG_LEVEL': 'WARNING'})


class ZoidbergReactor:
    """
    Start a new CrawlerRunner object for the zoidberg scraper
    """
    def __init__(self, country='es', doctor=None, area=None, illness=None, output='csv', path=None,*args, **kwargs):
        """
        Initialize the CrawlPropertyReactor object
        :param country: country scope
        :param doctor: doctor to search
        :param area: area of medicine of scope
        :param illness: illness to search
        :param output: file output type: csv or json
        :param path: path of the output
        :param args:
        :param kwargs:
        """
        # will populate the statistics of the scrapper
        self.stats_dic_list = []
        self.doctor = doctor
        self.area = area
        self.illness = illness
        self.output = output
        self.country = country.lower()
        self.country_db = 'db/' + country + '/' + country + '_db.json'
        if path:
            self.path = path
        else:
            self.path = 'zoigber_output.' + self.output
        # set the ITEM_PIPELINES settings for the specific output
        self.settings = get_project_settings()
        self.settings.set('ITEM_PIPELINES', {
            'scraper.pipelines.CleanItemsPipeline': 100,
            'scraper.pipelines.%sPipeline' % output.capitalize(): 200,
        }, 0)


    @defer.inlineCallbacks
    def conf(self):
        runner = CrawlerRunner(self.settings)
        list_urls = self.get_list_urls(self.area, self.illness)
        doctor_words = self.get_doctor_regex_words(self.doctor)

        for i in range(0, len(list_urls)):
            domain = list_urls[i]['domain']
            urls = list_urls[i]['urls']
            zoidgber_crawler = runner.create_crawler(domain)
            yield runner.crawl(zoidgber_crawler, doctor_regex=doctor_words, urls=urls, path=self.path)
        reactor.stop()  # the script will block here until the crawling is finished

    def run(self):
        reactor.run()

    def stop(self):
        reactor.stop()

    def get_doctor_regex_words(self, doctor):
        name_list = [doctor, doctor.capitalize(), doctor.upper(), doctor.lower(), doctor.title()]
        regex = ""
        for w in name_list:
            regex += '(\s' + w + '\s)|'
        return regex[:-1]

    def get_list_urls(self, area_raw, illness_raw):
        list_urls = []
        data = json.load(open(self.country_db))
        for area in data['area']:
            if area['slug'] == area_raw:
                for illness in area['illness']:
                    if illness['slug'] == illness_raw:
                        list_urls = illness['webs']

        return list_urls

    def get_countries(self):
        return next(os.walk('./db/'))[1]

    def get_domains(self):
        data = json.load(open(self.country_db))
        return data['domains']

    def get_areas(self):
        data = json.load(open(self.country_db))
        return [area['slug'] for area in data['area']]

    def get_illness_for_area(self, area=None):
        data = json.load(open(self.country_db))
        if area not in self.get_areas():
            return 'Please, insert a valid area. use get_areas() function to get a list of valid areas.'
        else:
            return [illness['slug'] for _area in data['area'] for illness in _area['illness'] if _area['slug'] == area]

"""
if __name__ == "__main__":
    zoidberg = ZoidbergReactor(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='spiders/aah.csv', output='csv')
    '''
    print(zoidberg.get_countries())
    print(zoidberg.get_domains())
    print(zoidberg.get_areas())
    print(zoidberg.get_illness_for_area(area='traumatologia'))
    '''
    zoidberg.conf()
    zoidberg.run()
"""
