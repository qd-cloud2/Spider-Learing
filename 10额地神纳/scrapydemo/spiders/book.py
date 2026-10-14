from scrapy import Request, Spider

class BookSpider(Spider):
    name = "book"
    allowed_domains = ["antispider7.scrape.center"]
    base_url = "https://antispider7.scrape.center"
    max_page = 512

    def start_requests(self):
        for page in range(1, self.max_page + 1):
            url = f'{self.base_url}/api/book/?limit=1&offset={(page - 1) * 18}'
            yield Request(url, callback=self.parse)
    
    def parse(self, response):
        print(response)
