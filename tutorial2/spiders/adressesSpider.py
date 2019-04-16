import scrapy
import json
import numpy as np

class QuotesSpider(scrapy.Spider):
    name = "adresses"
   
    nbServices = 3
    nbPage = 1
    nbAdress = 5
    

    adressDictionnary = { 'adresses' : [] }
    adressTab = [] 

    page = range(1,2)  # => [1,2]

    def start_requests(self):
        urls = [
            'https://www.walletexplorer.com'
        ]
        with open('services.json') as file :
            data = json.load(file)
            for value in np.array(data['liens'][0:self.nbServices]) :
                for nbpage in self.page :
                    yield scrapy.Request(url=value['href']+'/addresses?page='+str(nbpage),callback=self.scrapAdress,meta={'service': value['href'].split('/')[-1]},priority=3, dont_filter=True)



    def scrapAdress(self,response):
        service = response.meta['service']
        
        for adresse in np.array(response.xpath("//td/a/@href").re(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')[0:self.nbAdress]):    
            yield { 
                service: adresse
            }
            self.adressDictionnary['adresses'].append( { service : adresse } )
            self.adressTab.append( {'adresse': adresse } )
            
        jsonObject = json.dumps(self.adressDictionnary)
        f = open("adresses.json","w")
        f.write(jsonObject)
        f.close()