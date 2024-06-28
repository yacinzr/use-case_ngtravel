# Comparateur de Prix - Kappa Club Iberostar Palmeraie Marrakech 4*

## Description

Ce projet est un outil de comparaison de prix intelligent pour le package "Kappa Club Iberostar Palmeraie Marrakech 4*". Il collecte les prix de différents sites de voyage, les compare, et fournit des analyses pour aider à trouver les meilleures offres.

## Fonctionnalités

- Web scraping de sites de voyage populaires :
  - Booking.com
  - Leclerc Voyages
  - Carrefour Voyages
  - Promosejours.com
- Stockage des données dans une base SQL Server
- Analyse des prix avec l'API OpenAI
- Visualisation des comparaisons de prix
- Déploiement sur AWS avec SAM-CLI

## Prérequis

- Python 3.8+
- Selenium WebDriver
- BeautifulSoup4
- SQLAlchemy
- Matplotlib
- OpenAI API
- AWS SAM CLI
- requests
## Installation

1. Clonez ce dépôt :

Ce script va :
1. Scraper les prix des différents sites
2. Stocker les données dans la base SQL Server
3. Analyser les prix avec OpenAI
4. Générer un graphique de comparaison

## Déploiement sur AWS

1. Assurez-vous d'avoir configuré vos identifiants AWS
2. Exécutez :

sam build
sam deploy --guided


