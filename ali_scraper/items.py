# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AliScraperItem(scrapy.Item):
    urls_phone = scrapy.Field()
