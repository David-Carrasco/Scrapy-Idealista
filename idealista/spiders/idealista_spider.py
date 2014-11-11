__author__ = 'David Carrasco'
import scrapy
from idealista.items import IdealistaItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class IdealistaSpider(CrawlSpider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    ########################################################################
    ###       Add the urls to crawl in the start_urls variable           ###
    ########################################################################
    start_urls = ["http://www.idealista.com/alquiler-viviendas/madrid/zona-norte/"]

    rules = (
            # Filter all the flats paginated by the website following the pattern indicated
            Rule(LinkExtractor(restrict_xpaths=('//*[@class="std16"]/a[last()]'), unique=True),
                 callback='parse_flats',
                 follow=True),
        )

    def parse_flats(self, response):

    	# Necessary in order to create the whole link towards the website
        default_url = 'http://idealista.com'

        links = [str(''.join(default_url + link.xpath('p/a/@href').extract().pop()))
                 for link in response.xpath('//*[@class="location"]')]

        flats_features = response.xpath('//*[@class="features"]')

        prices = [int(flat.xpath('li[1]/text()').extract().pop().strip(' eur').replace('.',''))
                 for flat in flats_features]

        sqfts = [int(flat.xpath('li[2]/text()').extract().pop().split(' ').pop(0))
                 for flat in flats_features]

        rooms = [int(flat.xpath('li[3]/text()').extract().pop().split(' ').pop(0))
                 for flat in flats_features]

        sqtfs_m2 = [int(flat.xpath('li[4]/text()').extract().pop().split(' ').pop(0).replace('.',''))
                    for flat in flats_features]

        for flat in zip(links, prices, sqfts, sqtfs_m2, rooms):
            item = IdealistaItem(link=flat[0], price=flat[1], sqft=flat[2],
                                 sqft_m2=flat[3], rooms=flat[4])
            yield item
