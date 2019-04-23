# Projet Walletexplorer : 


* Projet réalisé dans le cadre de l'UE POM pour l'extraction des informations relatives aux bitcoins sur les réseaux sociaux 


## Authors 


* POITEVIN Louis & AMINI Khaled

* Encadrant : CAZABET Remy


## Required 


* python : <code>sudo apt-get install python</code>

* scrapy : <code>sudo pip install scrapy</code>


## Objectif


* Associer les adresses bitcoins a des noms de service et leurs catégories


## Avancement


* Possibilité de récupérer toutes les adresses bitcoin de la premiere page de chaque service


## How to 


* <code>git clone https://forge.univ-lyon1.fr/p1410541/walletexplorer</code>

* <code>cd walletexplorer/tutorial/tutorial</code> 

* <code>scrapy crawl services</code>

* <code>scrapy crawl adresses</code> 


* La dernière commande va extraire les données et créer des fichers json suivants :  
    * services.json : regroupe les liens des différents ressources URI du site
    * adresses.json : regroupe les adresses associés aux services bitcoin

## Remarque 

* Le framework scrapy s'éxécute de manière asynchrone, c'est à dire que l'ordre des requêtes dans laquelles elles sont écrites n'est pas forcément respecté lors de l'envoie.
* Comme il est nécéssaire de d'abord récupérer les liens de chaque service avant de récupérer les adresses, il se peut que vous deviez répéter la derniere commande deux fois.



