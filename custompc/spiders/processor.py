# -*- coding: utf-8 -*-
from pytest import Item
import scrapy
import csv
from scrapy.http import Request
from custompc.items import Processor
from lxml import etree


class ProcessorSpider(scrapy.Spider):
    name = 'processor'
    allowed_domains = ['dummy']
    start_urls = ['http://dummy/']


    def start_requests(self):
        no_pagination = ["TPSTech","ThinkPC"]
        meta = { 'dont_redirect': True, 'handle_httpstatus_list': [302] }
        with open("/home/harry/github/custompc/csvFiles/processors.csv", "rU") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['process'] == '0':
                    continue
                url = row['url']
                link_urls = [url.format(i) for i in range(1, 2)]
                for link_url in link_urls:
                    site = row['site']
                    if site == "MDComputers":
                        request = Request(
                            link_url, callback=self.mdcomputers_processors)
                    elif site == "PCShop":
                        request = Request(
                            link_url, callback=self.pcshop_processors)
                    elif site == "ThinkPC":
                        request = Request(
                            link_url, callback=self.thinkpc_processors)
                    elif site == "VedantComputers":
                        request = Request(
                            link_url, callback=self.vedant_processors)
                    elif site == "TPSTech":
                        request = Request(
                            link_url, callback=self.tsptech_processors)
                    #FIXME:: Amzaon redirecting to different urls to avoid scraping
                    # elif site == "Amazon":
                        # request = Request(
                        #     link_url,callback=self.amazon_processors)
                    yield request
                    if site in no_pagination:
                        break
    def amazon_processors(self, response):
        print("inside amazon_processors")
        item = Processor()
        content = response.xpath(
            '//div[contains(@class,"octopus-pc-card")]')
        for product_content in content:
            item['site'] = "Amazon"
            yield (item)
    def tsptech_processors(self, response):
        print("inside tpstech_processors")
        item = Processor()
        content = response.xpath(
            '//div[starts-with(@class,"eachPordBlock")]')
        for product_content in content:
            item['site'] = "TPSTech"
            item['processorName'] = product_content.xpath('.//div[starts-with(@class,"product-card__name")]/text()').extract_first()
            # item['processorLink'] = product_content.xpath(
            #     './/a[starts-with(@class="woocommerce-LoopProduct-link")]/@href').extract_first()
            item['processorPrice'] = product_content.xpath(
                './/span[@class="collection_price"]/text()').extract_first()
            yield (item)

    def vedant_processors(self, response):
        print("inside vedant_processors")
        item = Processor()
        content = response.xpath(
            '//div[starts-with(@class,"product-layout")]')
        for product_content in content:
            item['site'] = "Vedant"
            item['processorName'] = product_content.xpath('.//div[@class="name"]/a/text()').extract_first()
            item['processorLink'] = product_content.xpath(
                './/div[@class="name"]/a/@href').extract_first()
            item['processorPrice'] = product_content.xpath(
                './/span[@class="price-normal"]/text()').extract_first()
            yield (item)

    def thinkpc_processors(self, response):
        print("inside thinkpc_processors")
        item = Processor()
        content = response.xpath(
            '//li[starts-with(@class,"product")]')
        for product_content in content:
            item['site'] = "ThinkPC"
            item['processorName'] = product_content.xpath('.//a/h2/text()').extract_first()
            item['processorLink'] = product_content.xpath(
                './/a[starts-with(@class,"woocommerce-LoopProduct-link")]/@href').extract_first()
            item['processorPrice'] = product_content.xpath(
                './/span[starts-with(@class,"price")]//text()').extract()[1]
            yield (item)

    def pcshop_processors(self, response):
        print("inside pcshop_processors")
        item = Processor()
        content = response.xpath(
            '//li[starts-with(@class,"product")]')
        for product_content in content:
            item['site'] = "PCShop"
            item['processorName'] = product_content.xpath('.//div[@class="product-loop-header product-item__header"]//h2[@class="woocommerce-loop-product__title"]/text()').extract_first()
            item['processorLink'] = product_content.xpath(
                './/a[starts-with(@class,"woocommerce-LoopProduct-link")]/@href').extract_first()
            item['processorPrice'] = product_content.xpath(
                './/span[starts-with(@class,"woocommerce-Price-amount")]//text()').extract()[1]
            yield (item)

    def mdcomputers_processors(self, response):
        print("inside mdcomputers_processors")
        item = Processor()
        content = response.xpath(
            '//div[starts-with(@class,"product-item-container")]')
        for product_content in content:
            item['site'] = "MDComputers"
            item['processorName'] = product_content.xpath(
                './/div[@class="product-image-container"]//a/@title').extract_first()
            item['processorLink'] = product_content.xpath(
                './/div[@class="product-image-container"]//a/@href').extract_first()
            item['processorPrice'] = product_content.xpath(
                './/span[@class="price-new"]/text()').extract_first()

            yield (item)

    def parse(self, response):
        pass
