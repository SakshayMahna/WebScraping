import scrapy
from ..items import AmazonItem

class AmazonWatchesSpider(scrapy.Spider):
    name = 'amazon_watches'
    allowed_domains = ['amazon.in']
    start_urls = ['https://www.amazon.in/s?i=watches&bbn=2563504031&rh=n%3A2563504031%2Cp_n_feature_sixteen_browse-bin%3A5756157031%2Cp_72%3A1318476031%2Cp_n_specials_match%3A21618256031&dc&page=1&pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=47dffcf2-a819-4fe1-bc98-0eb339b0b537&pf_rd_r=EVV8ER0NRBGAJ7ED3ENA&pf_rd_s=merchandised-search-9&qid=1628417035&rnid=21618255031&ref=sr_pg_1']

    def parse(self, response):
        items = AmazonItem()

        name = response.xpath("//span[@class='a-size-base-plus a-color-base a-text-normal']/text()").extract()
        price = response.xpath("//span[@class='a-price-whole']/text()").extract()
        rating = response.xpath("//span[@class='a-size-base']/text()").extract()

        products = zip(name, price, rating)

        for product_name, product_price, product_rating in products:
            items["product_name"] = product_name
            items["product_price"] = product_price
            items["product_ratings"] = product_rating

            yield items

        # Get next page data
        NEXT_PAGE_SELECTOR = "//li[@class='a-selected']/following-sibling::li/a/@href"
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )
        
