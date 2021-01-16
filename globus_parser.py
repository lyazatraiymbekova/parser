from bs4 import BeautifulSoup as bs
import requests
from requests.sessions import default_headers 
from re import split
from sys import stderr
import psycopg2


connection = psycopg2.connect(
    dbname = 'globus',
    user = 'postgres',
    password = 'liazat123',
    host = 'localhost'
)
cursor = connection.cursor()



HOST = 'https://globus-online.kg/catalog/myaso_ptitsa_ryba/'



globus_page = requests.get(HOST).text

data = bs(globus_page, 'html.parser')

view_showcase = data.find('div', attrs={"id": "view-showcase"})

all_cards = view_showcase.find_all('div', class_='list-showcase__part-main')

for card in all_cards:
    image_link = card.find('div', class_='list-showcase__picture').a.img.get('src')
    product_name = card.find('div', class_='list-showcase__name-rating').a.text
    price = card.find('div', class_='list-showcase__prices').find('span', class_='c-prices__value js-prices_pdv_ГЛОБУС Розничная').text
    
#     cursor.execute(
#         f'INSERT INTO meats(image, product_name, price) VALUES(\'{image_link}\', \'{product_name}\', \'{price}\');'
#     )
#     connection.commit()
# connection.close()


