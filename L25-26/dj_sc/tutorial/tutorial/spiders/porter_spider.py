import json

import scrapy
from tutorial.items import PorterItem
from scrapy_redis.spiders import RedisSpider


class PorterSpider(RedisSpider):
    name = "porter_scrap"
    allowed_domains = ["www.net-a-porter.com"]

    # start_urls = [
    #     'https://www.net-a-porter.com/us/en/d/Shop/Clothing/All',
    #     'https://www.net-a-porter.com/us/en/d/Shop/Shoes/All',
    # ]
    visited_urls = []

    def parse(self, response):
        if response.url not in self.visited_urls:
            self.visited_urls.append(response.url)

            urls = response.xpath(
                '//div[@id="product-list"]/ul[@class="products"]/li/div[@class="description"]/a/@href'
            ).extract()
            # for url in urls:
            for url in urls[:2]:
                yield scrapy.Request(
                    url="https://www.net-a-porter.com" + url,
                    callback=self.parse_product
                )

            last_page = response.xpath(
                '//div[@class="pagination-links"]/@data-lastpage'
            ).extract_first()
            current_page = response.xpath(
                '//div[@class="pagination-links"]/span[@class="pagination-page-current"]/text()'
            ).extract_first()
            # if int(current_page) <= int(last_page):
            if int(current_page) <= 2:
                base_url = response.url.split("?")[0]
                page = base_url + "?pn={}".format(int(current_page) + 1)
                yield response.follow(url=page, callback=self.parse)

    def parse_product(self, response):

        item = PorterItem()

        item['designer_name'] = response.xpath(
            '//a[@class="designer-name"]/span[@itemprop="name"]/text()'
        ).extract_first()

        item['link'] = response.url

        item['product_name'] = response.xpath(
            '//h2[@class="product-name"]/text()'
        ).extract_first()

        nap_price = response.xpath(
            '//nap-price[@class="product-price"]/@price'
        ).extract_first()
        nap_price = json.loads(nap_price)
        item['price'] = nap_price["amount"] / nap_price["divisor"]
        item['currency'] = nap_price["currency"]

        size = response.xpath(
            '//div[@class="sizing-container"]/select-dropdown/@options'
        ).extract_first()
        size = json.loads(size)
        item['size'] = [
            el["displaySize"]
            for el in size
        ]

        description = response.xpath(
            '//div[@id="product-details-accordion"]/widget-show-hide[@id="accordion-2"]//div[@class="wrapper"]//text()'
        ).extract()
        item['description'] = " ".join(description)

        item['images'] = response.xpath(
            '//div[@id="main-image-carousel"]//img[contains(@class, "product-image")]/@src'
        ).extract()

        yield item
