import pandas as pd

# Scrape Data
import scrapy

class QSpider(scrapy.Spider):
    name = "alexa"
    start_urls = [
        'https://gooyatech.com/top-sites-in-iran-by-alexa/',
    ]

    def parse(self, response):
        yield {
        'list': response.css('td.column-2::text').getall()
        }
        
        
# Importing
data = pd.read_json('alexa.json')




# Cleaning
alexa = data['list'][0]
for e in alexa:
    print('http://'+e)
    
    
    
# Conver the list to Pandas Series
pd.set_option('display.max_rows', None)
ranking = pd.Series(alexa)
ranking
