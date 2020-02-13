# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from papers_crawler.items import PapersCrawlerItem


class SciencedirectSpider(CrawlSpider):
    name = 'sciencedirect'
    allowed_domains = ['sciencedirect.com']
    start_urls = [
        'https://www.sciencedirect.com/browse/journals-and-books?contentType=JL&contentType=BK&subject=mathematics&acceptsSubmissions=true']

    rules = (

        Rule(LinkExtractor(
            allow=("/journal/+((\w+|-)+)",
                   "/journal/+((\w+|-)+)/issue",
                   "/journal/+((\w+|-)+)/vol/\d+/suppl/"),
        )),

        # extract papers
        Rule(
            LinkExtractor(
                restrict_xpaths=("//*[@class='article-list']//ol//a[contains(@class, 'anchor article-content-title')]")
            ), callback='parse_item'
        ),
    )

    def parse_item(self, response):
        item = PapersCrawlerItem()
        item['title'] = ''.join(response.xpath("//*[@id='screen-reader-main-title']/span[@class='title-text']").getall())
        item['doi'] = response.xpath("//*[@id='doi-link']/a[1]/@href").get()
        item['journal'] = response.xpath("//*[@id='publication-title']/a/text()").get()
        item['vol'] = response.xpath("//*[@id='publication']/div[2]/div/a/text()").get() + \
                      response.xpath("//*[@id='publication']/div[2]/div[@class='text-xs']/text()").get()
        item['abstract'] = response.xpath("//*[@class='abstract author']/div/p").get()
        item['keywords'] = '; '.join(response.xpath("//div[@class='keyword']/span/text()").getall())
        item['base_url'] = response.request.url
        yield item
