import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "services"
    walletUrl = 'https://www.walletexplorer.com/wallet/Bittrex.com/addresses'
    baseUrl = 'https://www.walletexplorer.com'
    
    hrefTab = []
    hrefDictionnary = { 'liens' : []}
    adressDictionnary = { 'adresses' : [] }
    adressTab = [] 

    def start_requests(self):
        urls = [
            'https://www.walletexplorer.com'
        ]
        
        for url in urls:
            #yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url=url, callback=self.scrapLink)
        #with open('services.json') as file :
            #data = json.load(file)
            #for value in data['liens'] :
                #yield scrapy.Request(url=value['href']+'/addresses?page=1',callback=self.scrapAdress,meta={'service': value['href'].split('/')[-2]},priority=3, dont_filter=True)


        

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    def scrapLink(self,response):
        # Récupération de l'ensemble des liens

        hrefs = response.xpath("//li/a/@href").extract()
        for ref in hrefs :
            yield {
                'href': self.baseUrl+ref
            }
            self.hrefTab.append(self.baseUrl+ref)
            self.hrefDictionnary['liens'].append( {'href': self.baseUrl+ref } )
        jsonObject = json.dumps(self.hrefDictionnary)
        f = open("services.json","w")
        f.write(jsonObject)
        f.close()

