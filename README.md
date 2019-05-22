# Projet Walletexplorer : 


* Projet réalisé dans le cadre de l'UE POM pour l'extraction des informations relatives aux bitcoins sur les réseaux sociaux 


## Authors 


* POITEVIN Louis & AMINI Khaled

* Encadrant : CAZABET Remy


## Required 


* python : <code>sudo apt-get install python3</code>

* scrapy : <code>sudo pip3 install scrapy</code>


## Objectif


* Associer les adresses bitcoins a des noms de service et leurs catégories



## How to 


* <code>git clone https://forge.univ-lyon1.fr/p1410541/walletexplorer2</code>

* <code>chown -R [usernamesession] walletexplorer2/ </code>

* <code>cd walletexplorer2/tutorial2</code> 

* <code>scrapy crawl services</code>

* <code>scrapy crawl adresses</code> 

    ou 

* <code> scrapy runspider spiders/adressesSpider.py -o adresses2.json </code> 

    Soyez sur que le fichier "adresses2.json" n'existe pas si tel est le cas. s'il existe éxécutez la commande suivante : 
* <code>sudo rm adresses2.json </code>

## Arguments parse

* <code> scrapy crawl adresses -a p=nbPageToScrap -a a=nbAdressesParPage -a s=nbServices </code>

    ou 
* <code> scrapy runspider spiders/adressesSpider.py -o adresses2.json -a p=1 -a a=10 -a s=10</code> 

* Par défaut : 
    *-Nombre de page, p = 1
    *-Nomdre d'addresses a = 2
    *-Nombre de services s=3


* La dernière commande va extraire les données et créer des fichers json suivants :  
    * services.json : regroupe les liens des différents ressources URI du site
    * adresses.json : regroupe les adresses associés aux services bitcoin





