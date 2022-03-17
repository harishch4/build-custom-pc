# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

# from dataclasses import Field
import scrapy
from scrapy.item import Item, Field


class Processor(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #processor related fields
    site=Field()
    processorName=Field()
    processorPrice=Field()
    processorLink=Field()
    pass

