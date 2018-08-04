import scrapy
from ..items import PostItem


class MySpider(scrapy.Spider):
    name = "habr_scrap"
    start_urls = ['https://habr.com/', ]

    def parse(self, response):
        urls = response.xpath('//a[@class="post__title_link"]/@href').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_post)

    def parse_post(self, response):

        item = PostItem()

        title = response.xpath(
            '//span[@class="post__title-text"]/text()'
        ).extract()
        item['title'] = title

        text = response.xpath(
            '//div[contains(@class, "post__body_full")]/div/descendant::text()'
        ).extract()
        text = [x.strip('\r') for x in text]
        text = [x.strip('\n') for x in text]
        text = [x for x in text if x]
        item['text'] = text

        img = response.xpath(
            '//div[contains(@class, "post__body_full")]/div//img/@src'
        ).extract()
        item['img'] = img

        yield item
