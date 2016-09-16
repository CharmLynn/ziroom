

from scrapy.spider import Spider  
from scrapy.selector import Selector 
from ziroom.items import ZiroomItem
import sys
import re 
reload(sys)
sys.setdefaultencoding('gb2312')  

class ZiroomSpider(Spider):
    name = "ziroom"
    allowed_domains = ["http://www.ziroom.com/"]

    sourceurl = "http://www.ziroom.com/z/nl/r1400TO2500.html?p=%s"
    #sourceurl = "http://www.ziroom.com/z/nl/z3-r2.html?p=%s"
    start_urls = [sourceurl % (x) for x in xrange(1,142)  ]

    def parse(self, response):  
        pattern = re.compile('/z/vr/(\d+).html')

        sel = Selector(response)  
        # sites = sel.xpath('//ul/li')  
        items = []
        sites = sel.xpath('//ul[@id="houseList"]/li')  
        for site in sites: 
            item = ZiroomItem()

            imageurl = site.xpath('div[1]/a/img/@src').extract() 
            title = site.xpath('div[2]/h3/a/text()').extract() 
            url = site.xpath('div[2]/h3/a/@href').extract() 
            location = site.xpath('div[2]/h4/a/text()').extract()  
            area = site.xpath('div[2]/div[@class="detail"]/p[1]/span[1]/text()').extract()  
            floor = site.xpath('div[2]/div[@class="detail"]/p[1]/span[2]/text()').extract()  
            layout = site.xpath('div[2]/div[@class="detail"]/p[1]/span[3]/text()').extract()  
            subway = site.xpath('div[2]/div[@class="detail"]/p[2]/span/text()').extract()  

            # subway = site.xpath('div[2]/p[@class="room_tags clearfix"]/span[1]/text()').extract()  
            balcony = site.xpath('div[2]/p[@class="room_tags clearfix"]/span[2]/text()').extract() 
            style = site.xpath('div[2]/p[@class="room_tags clearfix"]/a/span[1]/text()').extract() 

            price = site.xpath('div[3]/p[@class="price"]/text()').extract() 


            item['title'] = title
            item['url'] = "http://www.ziroom.com/" + url[0]
            item['imageurl'] = imageurl
            item['houseid'] = pattern.findall(url[0])
            item['area'] = area
            item['layout'] = layout
            item['floor'] = floor
            item['subway'] = subway
            item['balcony'] = balcony
            item['style'] = style
            item['price'] = price
            item['location'] = location

            items.append(item)
        return items
