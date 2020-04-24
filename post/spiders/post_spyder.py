import scrapy
from ..items import PostItem

class Postspider(scrapy.Spider):
    name='post'

    start_urls =[
        'https://www.imdb.com/list/ls069887650/',
        'https://www.imdb.com/list/ls041185384/',
        'https://www.imdb.com/list/ls041185364/',
        'https://www.imdb.com/list/ls025929404/'
    ]

    def parse(self,response):
        items = PostItem()
        img_urls =[]
        
       
            
        quotes = response.css('div.mode-detail')
        for quote in quotes:
            title =quote.css('a::text')[2].extract()
            role= quote.css('p::text')[0].extract()
           
            
            
           
            title=title.split('\n')
            role=role.split('\n')
            title = list(filter(None,title))
            role = list(filter(None,role))
            role = [x.strip(' ') for x in role]
            items['Name']=title
            items['Role']=role
           
            yield items
        img = response.css('div.mode-detail')
        for q in img:
           
           img_urls.append(q.css("img::attr(src)")[0].extract())
           #items["images"]=img_urls
           items["image_urls"]=img_urls
           yield items      
        