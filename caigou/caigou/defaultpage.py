import scrapy


# request = scrapy.Request("http://www.ccgp-shanxi.gov.cn/")


class ccgp_shanxiSpider(scrapy.Spider):
    name = "ccgp_shanxi"
    # 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个
    start_urls = ['http://www.ccgp-shanxi.gov.cn/view.php?ntype=fnotice&nodeid=154']

    def parse(self, response):
        scrapy.Request(start_urls, callback=self.parse, method="POST")
        yield scrapy.Request('http://books.toscrape.com/',
                             callback=self.parse_book,
                             headers={'User-Agent': 'Mozilla/5.0'},
                             dont_filter=True)
        print("sss" + response)

    # #         # 提取数据
    # #         # 每一本书的信息在<tr class="odd">中，我们使用
    # #         # css()方法找到所有这样的article 元素，并依次迭代
    #         for item in response.css('tr.odd'):
    #             # 书名信息在article > h3 > a 元素的title属性里target='_blank'
    #             # 例如: <a title="A Light in the Attic">A Light in the ...</a>
    #             name = item.xpath('./a/@target').extract_first()
    #             print(item)
    #
    #             # 书价信息在 <p class="price_color">的TEXT中。
    #             # 例如: <p class="price_color">￡51.77</p>
    #             # price = book.css('p.price_color::text').extract_first()
    #             # yield {
    #             #        'name': name,
    #             #     }
    print("sfds")
