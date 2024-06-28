from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_booking_com():
    # URL de la page de recherche sur Booking.com avec des critères spécifiques (hôtel à Marrakech)
    url_Booking = 'https://www.booking.com/searchresults.fr.html?ss=Iberostar+Club+Palmeraie+Marrakech%2C+Marrakech%2C+Maroc&ssne=Iberostar+Club+Palmeraie+Marrakech%2C+Marrakech%2C+Maroc&ssne_untouched=Iberostar+Club+Palmeraie+Marrakech%2C+Marrakech%2C+Maroc&label=gen173nr-1FCAQoggJCL3NlYXJjaF9rYXBwYSBjbHViIGliZXJvc3RhciBwYWxtZXJhaWUgbWFycmFrZWNoSDNYBGhNiAEBmAENuAEXyAEM2AEB6AEB-AEDiAIBqAIDuALerfizBsACAdICJDIyM2IxMTNlLWYxNjktNDU5My1iZGUxLTJjNzMxZWU1YzU1N9gCBeACAQ&aid=304142&lang=fr&sb=1&src_elem=sb&src=searchresults&checkin=2024-08-01&checkout=2024-08-07&group_adults=1&no_rooms=1&group_children=0'

    # En-têtes HTTP pour imiter un navigateur et éviter d'être bloqué par le site
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    # Envoi de la requête HTTP GET pour récupérer la page web
    response = requests.get(url_Booking, headers=headers)

    # Parsing du contenu HTML de la réponse avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les éléments de la page correspondant à des cartes de propriétés (hôtels)
    hotels = soup.findAll('div', {'data-testid': 'property-card'})

    # Liste pour stocker les données des hôtels extraites
    hotels_data = []

    # Boucle sur chaque élément hôtel pour extraire les données souhaitées
    for hotel in hotels:
        try:
            # Extraction du nom de l'hôtel
            name_element = hotel.find('div', {'data-testid': 'title'})
            name = name_element.text.strip() if name_element else "Name not found"

            # Extraction de l'emplacement de l'hôtel
            location_element = hotel.find('span', {'data-testid': 'address'})
            location = location_element.text.strip() if location_element else "Location not found"

            # Extraction du prix de l'hôtel
            price_element = hotel.find('span', {'data-testid': "price-and-discounted-price"})
            price = price_element.text.strip() if price_element else "Price not found"
            
            # Ajout des informations de l'hôtel à la liste des données
            hotels_data.append({
                'name': name,
                'price': price,
                'web-site': 'Booking.com'
            })
        except Exception as e:
            # Affichage d'un message d'erreur en cas de problème lors de l'extraction des données de l'hôtel
            print(f"Error processing hotel: {e}")

    # Affichage du nombre d'hôtels traités
    print(f"Processed {len(hotels_data)} hotels")



def scrap_leclercvoyages():
    # URL de la page de recherche sur le site Leclerc Voyages avec des critères spécifiques (destination au Maroc, départ en août 2024)
    url_lecler = 'https://www.leclercvoyages.com/search?m_c.desti=MA&m_dd=01&m_dmy=08%2F2024&m_minMan=7%2C7&m_aj=7&m_dpci=PAR%2CCDG%2CORY%2CBVA%2CXPG&rm=rm&_gl=1*17v5p1t*_up*MQ..*_ga*MTU3MTczNDY5My4xNzE5MzcwMjgz*_ga_FRHKRHQ1CW*MTcxOTM3MDI4Mi4xLjAuMTcxOTM3MDI4Mi4wLjAuMA..'

    # En-têtes HTTP pour imiter un navigateur et éviter d'être bloqué par le site
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    # Envoi de la requête HTTP GET pour récupérer la page web
    response = requests.get(url_lecler, headers=headers)

    # Parsing du contenu HTML de la réponse avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les éléments de la page correspondant à des résultats d'hôtels
    hotels = soup.findAll('article', {'class': 'cpt-result'})

    # Liste pour stocker les données des hôtels extraites
    hotels_data = []

    # Boucle sur chaque élément hôtel pour extraire les données souhaitées
    for hotel in hotels:
        try:
            # Extraction du nom de l'hôtel
            name_element = hotel.find('h2', {'class': 'title-result quaternary', 'itemprop': 'name'})
            name = name_element.text.strip() if name_element else "Name not found"

            # Extraction de l'emplacement de l'hôtel
            location_element = hotel.find('span', {'data-testid': 'address'})
            location = location_element.text.strip() if location_element else "Location not found"

            # Extraction du prix de l'hôtel
            price_element = hotel.find('span', {'class': 'price'})
            price = price_element.text.strip() if price_element else "Price not found"
        
            # Ajout des informations de l'hôtel à la liste des données
            hotels_data.append({
                'name': name,
                'price': price,
                'web-site': 'leclerc.com'
            })
        except Exception as e:
            # Affichage d'un message d'erreur en cas de problème lors de l'extraction des données de l'hôtel
            print(f"Error processing hotel: {e}")
      



def scrap_promosjours():
    url_promosejours = 'https://www.promosejours.com/maroc/searchProducts?dpci=PAR&c.de=bm.ma&dd=01&dmy=08/2024&aj=7&minMan=6,9'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    response = requests.get(url_promosejours, headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    hotelsu = soup.findAll('div', {'class': 'clearfix'})

    print(f"Number of hotel elements found: {len(hotelsu)}")

    hotels_datau = []

    # Loop over the hotel elements and extract the desired data
    for hotel in hotelsu:
        try:
            # Extract the hotel name
            name_element = hotel.find('h4', {'class': 'trip-informations'})
            name = name_element.text.strip() if name_element else "Name not found"

            # Extract the hotel price
            price_element = hotel.find('div', {'class': 'price'})
            price = price_element.text.strip() if price_element else "Price not found"

            # Append hotels_data with info about hotel
            hotels_datau.append({
                'name': name,
                'price': price,
                'web-site': 'promojours.com'
            })
        except Exception as e:
            print(f"Error processing hotel: {e}")
            # Optionally, you can print the hotel HTML to debug
            # print(hotel.prettify())

    print(f"Processed {len(hotels_datau)} hotels")
    return hotels_datau


def process_combined_data():
    data1 = scrape_booking_com()
    data2 = scrap_leclercvoyages()
    data3 = scrap_promosjours()

    combined_data = data1 + data2 + data3
    print(f"Total number of hotels processed: {len(combined_data)}")

    return combined_data

def main():
    combined_hotel_data = process_combined_data()
    print(combined_hotel_data)


if __name__ == "__main__":
    main()

    