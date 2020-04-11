import scrapy

class TheVillagePeopleSpider(scrapy.Spider):
    name = 'Articles from "The Village - People"'
    start_urls = ['https://www.the-village.ru/village/people']

    def parse(self, response):
        article = response.css('.article-text').extract_first()
        if article:
            yield {
                'url': response.url,
                'text': article
            }

        for post in response.css('.post-link'):
            link = post.css('::attr(href)').extract_first()
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse
            )

        next_page = response.css('.pages-arrow.next::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )