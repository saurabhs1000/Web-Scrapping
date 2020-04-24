# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Role = scrapy.Field()
    image_urls=scrapy.Field()
   
    #images = scrapy.Field()
    
