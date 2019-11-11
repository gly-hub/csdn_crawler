# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from csdn_test.items import Article


class CSpiderSpider(scrapy.Spider):
    name = 'C_spider'
    allowed_domains = ['csdn.net']
    def start_requests(self):
        for i in range(10):
            url = 'https://so.csdn.net/so/search/s.do?p=' + str(i+1) + '&q=C&t=&viparticle=&domain=&o=&s=&u=&l='
            yield SplashRequest(url=url, callback=self.parse, args={'wait':5.0})
            # yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.text)
        urls = response.xpath('//div[@class="limit_width"]/a[1]/@href').extract()
        for url in urls:
            if 'blog.csdn.net' in url and 'article' in url:
                yield SplashRequest(url=url, callback=self.get_articleHtml, args={'wait': 5.0})

    def get_articleHtml(self, response):
        article = Article()
        article['Atype'] = 'C'
        article['title'] = response.xpath('//div[@id="mainBox"]/main/div[1]/div[1]/div/div[1]/h1/text()').extract()
        article['content'] = response.xpath('//div[@id="mainBox"]/main/div[1]/article[@class="baidu_pl"]').extract()
        if article['title'] != [] and article['content'] != []:
            yield article