import scrapy

class FlipkartGamesSpider(scrapy.Spider):
    name = 'flipkart_games'
    allowed_domains = ['flipkart.com']
    start_urls = ['https://www.flipkart.com/gaming/games/pr?sid=4rr,fa6&otracker=categorytree/']

    def parse(self, response):
        print("Processing " + response.url)

        # Extract data using XPath
        name = response.xpath("//a[@class='s1Q9rs']/text()").extract()
        rating = response.xpath("//div[@class='_3LWZlK']/text()").extract()
        price = response.xpath("//div[@class='_30jeq3']/text()").extract()

        # Zip all data and iterate over it
        row_data = zip(name, rating, price)

        for item in row_data:
            scraped_info = {
                'page'      :   response.url,
                'name'      :   item[0],
                'rating'    :   item[1],
                'price'     :   item[2]
            }

            yield scraped_info

        # Get next page data
        NEXT_PAGE_SELECTOR = "//a[@class='ge-49M _2Kfbh8']/following-sibling::a/@href"
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse
            )

