# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
from jianshu.items import JianshuItem


class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    # 可以指定爬虫抓取的规则，支持正则表达式
    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = JianshuItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        html = etree.HTML(response.text)
        # self.open_file(response.text)
        item['title'] = html.xpath("//title/text()")[0].split('-')[0]
        item['name'] = html.xpath('//span[@class="_22gUMi"]/text()')[0]
        item['url'] = response.url.split("?")[0]
        collection = html.xpath("//div[@class='_2Nttfz']/a/spen/text()")
        if collection:
            item['collection'] = ','.join(collection)
        yield item

    def open_file(self, html):
        with open('/Users/smh/Desktop/1.html', 'w+') as f:
            f.write(html)
