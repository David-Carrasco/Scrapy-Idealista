__author__ = 'David Carrasco'
import scrapy
from idealista.items import IdealistaItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class IdealistaSpider(CrawlSpider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    ########################################################################
    ###       Add the url to crawl in the start_urls variable           ###
    ########################################################################
    start_urls = ["http://www.idealista.com/alquiler-viviendas/madrid/zona-norte/"]

    rules = (
            # Filter all the flats paginated by the website following the pattern indicated
            Rule(LinkExtractor(restrict_xpaths=("//a[@class='icon-arrow-right-after']"), unique=True),
                 callback='parse_flats',
                 follow=True),
        )

    def parse_flats(self, response):

    	# Necessary in order to create the whole link towards the website
        default_url = 'http://idealista.com'

	info_flats_xpath = response.xpath("//*[@class='item-info-container']")
	prices_flats_xpath = response.xpath("//*[@class='row price-row clearfix']/span[@class='item-price']/text()")

        links = [str(''.join(default_url + link.xpath('a/@href').extract().pop()))
                 for link in info_flats_xpath]

        prices = [int(flat.extract().replace('.','').strip())
                 for flat in prices_flats_xpath]

	addresses = [address.xpath('a/@title').extract().pop().encode('iso-8859-1') 
		     for address in info_flats_xpath]

        #rooms = [int(flat.xpath("span[@class='item-detail'][1]/text()").extract().pop().strip())
        #         for flat in info_flats_xpath]

        #sqfts_m2 = [int(flat.xpath("span[@class='item-detail'][2]/text()").extract().pop().replace('.','').strip())
        #            for flat in info_flats_xpath]

        #for flat in zip(links, prices, addresses, sqfts_m2, rooms):
	for flat in zip(links, prices, addresses):
            item = IdealistaItem(link=flat[0], price=flat[1], address=flat[2]) 
                                 #sqft_m2=flat[2], rooms=flat[3])
            yield item
