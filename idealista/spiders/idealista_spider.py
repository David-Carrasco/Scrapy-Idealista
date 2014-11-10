__author__ = 'David Carrasco'
import scrapy
from idealista.items import IdealistaItem

class IdealistaSpider(scrapy.Spider):
    name = "idealista"
    allowed_domains = ["idealista.com"]
    start_urls = ["http://www.idealista.com/venta-viviendas/madrid/carabanchel/vista-alegre/"]

    def parse(self, response):

    	# Necessary in order to create the whole link to the website
        default_url = 'http://idealista.com'

        prices = [price.xpath('text()').extract().pop()
                  for price in response.xpath('//*[@class="col-0"]')]

        links = [''.join(default_url + link.xpath('p/a/@href').extract().pop())
                 for link in response.xpath('//*[@class="location"]')]

        print zip(prices, links)

        for flat in zip(links, prices):
            item = IdealistaItem()
            item['price'] = flat[0]
            item['link'] = flat[1]
            yield item
