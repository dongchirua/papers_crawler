# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PapersCrawlerItem(scrapy.Item):
    title = scrapy.Field()
    doi = scrapy.Field()
    journal = scrapy.Field()
    vol = scrapy.Field()
    abstract = scrapy.Field()
    keywords = scrapy.Field()
    base_url = scrapy.Field()
