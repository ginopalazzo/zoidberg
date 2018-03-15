# -*- coding: utf-8 -*-

"""
Zoidberg could be use in two different ways:
    a)  CL:
        python zoidberg args
    b)  python module:
        from zoidbderg import Zoidberg
"""

import os

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from zoidberg.scraper.spiders import es_spider
# from scraper.spiders import es_spider
import json

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s', 'LOG_LEVEL': 'WARNING'})

HERE = os.path.abspath(os.path.dirname(__file__))

class Zoidberg:
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
        if self.check_args(country, doctor, area, illness, output):
            self.stats_dic_list = []
            self.doctor = doctor
            self.area = area
            self.illness = illness
            self.output = output.lower()
            self.country = country.lower()
            print(HERE)
            self.country_db = HERE + '/scraper/db/' + country + '/' + country + '_db.json'
            if path:
                self.path = path
            else:
                self.path = 'zoidberg_output.' + self.output
            # set the ITEM_PIPELINES settings for the specific output
            self.settings = get_project_settings()
            self.settings.set('ITEM_PIPELINES', {
                'scraper.pipelines.CleanItemsPipeline': 100,
                'scraper.pipelines.%sPipeline' % output.capitalize(): 200,
            }, 0)

    def check_args(self, country, doctor, area, illness, output):
        # countries = self.get_countries()
        if type(country) is not str:
            raise ValueError("Country: must be str.")
        elif len(country) is not 2:
            raise ValueError("Country: must be ISO 3166-1 alfa-2 (2 characters).")
        # elif country not in countries:
        #     raise ValueError("Country: only %s countries is supported" % countries)
        elif doctor is None or area is None or illness is None:
            raise ValueError("Doctor, area, illness: must not be None.")
        elif type(doctor) is not str or type(area) is not str or type(illness) is not str:
            raise ValueError("Doctor, area, illness: must not be None.")
        elif output != 'csv' and output != 'json':
            raise ValueError("Output: Only csv or json outputs is supported.")
        else:
            return True

    @defer.inlineCallbacks
    def conf(self):
        runner = CrawlerRunner(self.settings)
        list_urls = self.get_list_urls(self.area, self.illness)
        doctor_words = self.get_doctor_regex_words(self.doctor)

        for i in range(0, len(list_urls)):
            domain = list_urls[i]['domain']
            urls = list_urls[i]['urls']
            #es_spider.ElAtletaComSpider
            spider = eval('es_spider.' + domain.replace('.', '').title() + 'Spider')
            zoidgber_crawler = runner.create_crawler(spider)
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
    '''
    def get_countries(self):
        import zoidberg.scraper.settings
        return zoidberg.scraper.settings.COUNTRIES
    '''

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

'''
if __name__ == "__main__":
    zoidberg = Zoidberg(country='es', doctor='margalet', area="traumatologia", illness="femoroacetabular", path='bbb.csv', output='csv')
   
    print(zoidberg.get_countries())
    print(zoidberg.get_domains())
    print(zoidberg.get_areas())
    print(zoidberg.get_illness_for_area(area='traumatologia'))
   
    zoidberg.conf()
    zoidberg.run()
'''

import argparse


def get_args():
    """This function parses and return arguments passed in"""
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description="Are you ready to operate, Doctor? - I'd love to, but first I have to perform surgery.")
    # Add arguments
    parser.add_argument(
        '-d', metavar='doctor', type=str, required=True,
        help='doctor to find')
    parser.add_argument(
        '-c', metavar='country', type=str, required=True,
        help="ISO 3166-1 alfa-2 country code. i.e. 'es' for 'Spain'.")
    parser.add_argument(
        '-a', metavar='area', type=str, required=True,
        help='medical area')
    parser.add_argument(
        '-i', metavar='illness', type=str, required=True,
        help='medical illness')
    parser.add_argument(
        '-o', metavar='output', type=str, required=False, default='csv',
        help='output file type: csv or json (default: csv)')
    parser.add_argument(
        '-p', metavar='path', type=str, required=False,
        help='file output path (default: zoidberg_output.csv/json)')
    parser.add_argument(
        '-l', metavar='log_level', type=str, required=False, default='warning',
        help='screen log level output (default: warning)')

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    zoidberg_runner = Zoidberg(country=args.c, doctor=args.d, area=args.a, illness=args.i, path=args.p, output=args.o)
    zoidberg_runner.conf()
    zoidberg_runner.run()
