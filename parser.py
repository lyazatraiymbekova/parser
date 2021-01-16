from re import split
from sys import stderr
from bs4 import BeautifulSoup as bs
import requests
import psycopg2


connection = psycopg2.connect(
    dbname = 'postgres',
    user = 'postgres',
    password = 'liazat123',
    host = 'localhost'
)
cursor = connection.cursor()

itc_page = requests.get(
    url='https://www.itc.kg/'
)
data = bs(itc_page.text, 'html.parser')

section = data.find('section', attrs={"id": "service"})
all_col_md_4 = section.find_all('div', class_="col-md-4")


for col in all_col_md_4:
    name = col.h2.get_text()

    definition = col.p.text.strip().split('\n')

    if definition[-1] == 'Подробнее':
        definition.pop(-1)

    description = ' '.join([i.strip() for i in definition])

    # print(description)


    a = f'''INSERT INTO parser (name, text)
        VALUES (\'{name}\', \'{description}\');'''

    # cursor.execute(a)
    # connection.commit()
    


create = '''CREATE TABLE parser(
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    text VARCHAR(250) NOT NULL
);'''
# cursor.execute(create)
# cursor.connection.commit()






















