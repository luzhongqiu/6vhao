# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from pachong.items import PachongItem


class A6vhaoSpider(CrawlSpider):
    name = '6vhao'
    allowed_domains = ['6vhao.com']
    start_urls = ['http://www.6vhao.com']

    rules = (
        Rule(LinkExtractor(allow=r'/\w+/\d+-\d+-\d+/\w+.\w+'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'.*'), follow=True),
    )

    def parse_item(self, response):
        i = PachongItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()



        try:
            i['name'] = response.xpath('//div[@class="box"]/h1/text()').extract()[0].strip()
            i['url']=response.xpath('//td[@bgcolor="#ffffbb"]/a/@href').extract()[0]
            i['data']=re.search(r'(\d+-\d+-\d+)',response.url).group(1)
            return i
        except:
            with open('log.txt','a') as f:
                f.write(response.url)
                f.write('\n')


