# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse


class JianshuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JianshuDownloaderMiddleware(object):
    def __init__(self):
        # 加载测试浏览器
        self.driver = webdriver.Chrome(executable_path=r"/Applications/chromedriver")

    # request：则scrapy框架会去服务器加载资源
    # reponse：则跳过资源下载直接交给解析器方法
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        # 模拟人类访问页面的行为，并且单击收入的专题按钮（按钮存在的话）
        self.driver.get(request.url)
        # 为了防止页面加载过慢，则等待1秒
        time.sleep(1)
        # 目前页面已经在测试浏览器中
        try:
            while True:
                show_more = self.driver.find_element_by_class_name('H7E3vT')
                show_more.click()
                print("-----------")
                time.sleep(1)
        except:
            print("别再单击了")
        source = self.driver.page_source
        HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
        return response

