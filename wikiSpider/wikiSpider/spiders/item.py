from scrapy import Item, Field


class Article(Item):
    # define the field for item
    title = Field()
