import scrapy
import numpy as np
import csv, json, sys
import pandas as pd
from csv import DictWriter

class QuotesSpider(scrapy.Spider):
    name = "adresses"
    s = None
    p = None
    a = None

     


    # Variable d'initialisation
    nbServices = 3
    nbPage = 1
    nbAdressByPage = 2

    
    

    adressDictionnary = { 'adresses' : [] }
    adressTab = [] 

    page = range(1,(nbPage+1))

      

    def start_requests(self):
        page = 2
        nbservices = 3
        if self.p : 
            page = int (self.p) + 1
        
        if self.s : 
            nbservices = int(self.s) 
        
        
        
        with open('services.json') as file :
            data = json.load(file)
            for value in np.array(data['liens'][0:nbservices]) :
                for nbpage in range(1, page) :
                    yield scrapy.Request(url=value['href']+'/addresses?page='+str(nbpage),callback=self.scrapAdress,meta={'service': value['href'].split('/')[-1],'page': int(nbpage) },priority=3, dont_filter=True)

    

    def scrapAdress(self,response):
        
        #Récupération des adresses
       
        if self.a :  
            nbadressesbypage = self.a
        else : 
            nbadressesbypage = 2
        
        
        service = response.meta['service']
        page = response.meta['page']
        
        #for adresse in np.array(response.xpath("//td/a/@href").re(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')[0:self.nbAdressByPage]):
        for adresse in np.array(response.xpath("//td/a/@href").re(r'[13][a-km-zA-HJ-NP-Z1-9]{25,34}')[0:int(nbadressesbypage)]):    
            yield { 
                service: adresse
            }
            self.adressDictionnary['adresses'].append( { adresse : service, 'page' : page } )
            self.adressTab.append( {'adresse': adresse, 'page' : page } )
            
        jsonObject = json.dumps(self.adressDictionnary)
        f = open("adresses.json","w")
        f.write(jsonObject)
        f.close()

        dicts = json.dumps(self.adressDictionnary)
        dictjson = json.loads(dicts)
        the_file = open("sample.csv", "w")
        writer = DictWriter(the_file, dictjson[0].keys())
        writer.writeheader()
        writer.writerows(dicts)
        the_file.close()
        