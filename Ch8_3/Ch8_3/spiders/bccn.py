import scrapy


class BccnSpider(scrapy.Spider):
    name = 'bccn'
    allowed_domains = ['bbs.bccn.net']
    start_urls = ['https://bbs.bccn.net/forum-246-1.html']

    def parse(self, response):
    titles = response.css("td.title > a::text").extract()
    votes = response.xpath("//span[@class='l_last_t']/a/text()").extract()
    replytimes = response.xpath("//td[@class='l_last']/a/text()").extract()
    for item in zip(titles, replytimes, authors):
        scraped_info = {
            "title" : item[0],
            "replytime" : item[1],
            "author" : item[2]
            }
        yield scraped_info
        
    
