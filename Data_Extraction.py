import scrapy


class DataExtractionSpider(scrapy.Spider):
    name = 'Data_Extraction'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
