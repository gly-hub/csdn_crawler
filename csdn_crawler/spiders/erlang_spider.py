# -*- coding: utf-8 -*-
import scrapy
from csdn_crawler.items import Article

class ErlangSpiderSpider(scrapy.Spider):
    name = 'erlang_spider'
    allowed_domains = ['csdn.net']
    def start_requests(self):
        for i in range(10):
            url = 'https://so.csdn.net/so/search/s.do?p=' + str(i+1) + '&q=erlang&t=&viparticle=&domain=&o=&s=&u=&l='
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        # print(response.text)
        urls = response.xpath('//div[@class="limit_width"]/a[1]/@href').extract()
        for url in urls:
            if 'blog.csdn.net' in url and 'article' in url:
                yield scrapy.Request(url = url, callback = self.get_articleHtml)

    def get_articleHtml(self, response):
        article = Article()
        article['Atype'] = 'erlang'
        article['title'] = response.xpath('//*[@id="mainBox"]/main/div[1]/div[1]/div/div[1]/h1/text()').extract()
        article['content'] = response.xpath('//*[@id="mainBox"]/main/div[1]/article[@class="baidu_pl"]').extract()
        yield article
