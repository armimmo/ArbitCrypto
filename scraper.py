import logging

import scrapy

logging.basicConfig(filename='log.txt', level=logging.DEBUG)


class BrickSetSpider(scrapy.Spider):
    name = 'binance'
    start_urls = ['https://global.bittrex.com/home/markets']

    def parse(self, response):
        UNORDERED_LIST = '//tr'

        # item['var1'] = div.select('./td[2]/p/span[2]/text()').extract()
        # item['var2'] = div.select('./td[3]/p/span[2]/text()').extract()
        # item['var3'] = div.select('./td[4]/p/text()').extract()

        for title in response.xpath(UNORDERED_LIST):
            # TITLE = 'tr/td[5]'
            yield {
                'item' : title.xpath('table/tbody/tr[*]/td[5]/text()').extract()
            }
        # {'price': row.xpath(title)}

# /html/body/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[5]
# /html/body/div[3]/div[2]/div/div[2]/div[2]/table/tbody/tr[3]/td[5]