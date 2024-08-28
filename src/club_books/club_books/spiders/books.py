import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            book_url = book.css('h3 a::attr(href)').get()
            if book_url is not None:
                yield response.follow(book_url, callback=self.parse_book)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response):
        yield {
            'name': response.css('h1::text').get(),
            'category': response.css('ul.breadcrumb li:nth-of-type(3) a::text').get(),
            'stars': response.css('p.star-rating::attr(class)').get().replace('star-rating ', ''),
            'price': response.css('p.price_color::text').get(),
            'in_stock': response.css('p.instock.availability::text').get().strip(),
        }
