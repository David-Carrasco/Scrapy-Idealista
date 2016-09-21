__author__ = 'David Carrasco'
import scrapy
from idealista.items import IdealistaItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from datetime import datetime

class IdealistaSpider(CrawlSpider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    ########################################################################
    ###       Add the url to crawl in the start_urls variable           ###
    ########################################################################
    #start_urls = ["https://www.idealista.com/venta-viviendas/leganes/el-carrascal/"]
    #start_urls = ['https://www.idealista.com/alquiler-viviendas/madrid/zona-norte/']

    start_urls = ['https://www.idealista.com/venta-viviendas/leganes/las-dehesillas-vereda-de-los-estudiantes/']

    rules = (
            # Filter all the flats paginated by the website following the pattern indicated
            Rule(LinkExtractor(restrict_xpaths=("//a[@class='icon-arrow-right-after']")),
                 callback='parse_flats',
                 follow=True),
        )

    def parse_flats(self, response):

    	# Necessary in order to create the whole link towards the website
        default_url = 'http://idealista.com'

	info_flats_xpath = response.xpath("//*[@class='item-info-container']")
	prices_flats_xpath = response.xpath("//*[@class='row price-row clearfix']/span[@class='item-price']/text()")
	discounts_xpath = response.xpath("//*[@class='row price-row clearfix']")

        links = [str(''.join(default_url + link.xpath('a/@href').extract().pop()))
                 for link in info_flats_xpath]

        prices = [int(flat.extract().replace('.','').strip())
                 for flat in prices_flats_xpath]

	discounts = [0 if len(discount.xpath("./*[@class='item-price-down icon-pricedown']/text()").extract()) < 1 else discount.xpath("./*[@class='item-price-down icon-pricedown']/text()").extract().pop().replace('.','').strip().split(' ').pop(0) for discount in discounts_xpath]
	
	addresses = [address.xpath('a/@title').extract().pop().encode('iso-8859-1') 
		     for address in info_flats_xpath]
	
        rooms = [int(flat.xpath("span[@class='item-detail'][1]/text()").extract().pop().strip())
                 for flat in info_flats_xpath]

        sqfts_m2 = [int(flat.xpath("span[@class='item-detail'][2]/text()").extract().pop().replace('.','').strip()) for flat in info_flats_xpath]

        #for flat in zip(links, prices, addresses, sqfts_m2, rooms):
	for flat in zip(links, prices, addresses, discounts, rooms, sqfts_m2):
            item = IdealistaItem(date=datetime.now().strftime('%Y-%m-%d'),
				 link=flat[0], price=flat[1], address=flat[2], discount=flat[3]) 
                                 #sqft_m2=flat[2], rooms=flat[3])
            yield item

    #Overriding parse_start_url to get the first page
    parse_start_url = parse_flats



