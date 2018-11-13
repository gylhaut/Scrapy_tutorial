import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com',
    #
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = [
          'http://quotes.toscrape.com/page/1/',
     ]
    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'title': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            for href in response.css('li.next a::attr(href)'):
                yield response.follow(href, callback=self.parse)

            # next_page = response.css('li.next a::attr(href)').extract_first()
            # if next_page is not None:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)#递归
                #创建请求的快捷方式，支持相对路径
                # if next_page is not None:
                #     yield response.follow(next_page, callback=self.parse)
                # for href in response.css('li.next a::attr(href)'):
                #     yield response.follow(href, callback=self.parse)
                # for a in response.css('li.next a'):
                #     yield response.follow(a, callback=self.parse)

            # title = quote.css("span.text::text").extract_first()
            # author = quote.css("small.author::text").extract_first()
            # tags = quote.css("div.tags a.tag::text").extract()
            # print(dict(title=title,author= author,tags=tags))




