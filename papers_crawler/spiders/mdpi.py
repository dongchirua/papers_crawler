# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from papers_crawler.items import PapersCrawlerItem


class MdpiSpider(CrawlSpider):
    name = 'mdpi_mca'
    allowed_domains = ['mdpi.com']
    start_urls = ['https://www.mdpi.com/search?q=&journal=mca&sort=pubdate&page_count=50']

    def start_requests(self):
        yield scrapy.Request('http://www.example.com/1.html', self.parse)
        yield scrapy.Request('http://www.example.com/2.html', self.parse)
        yield scrapy.Request('http://www.example.com/3.html', self.parse)

    def parse(self, response):
        for h3 in response.xpath('//h3').getall():
            yield MyItem(title=h3)

        for href in response.xpath('//a/@href').getall():
            yield scrapy.Request(response.urljoin(href), self.parse)