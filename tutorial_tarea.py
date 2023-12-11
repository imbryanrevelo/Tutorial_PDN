import locale

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
driver = webdriver.Edge()
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product

driver.get('https://www.flipkart.com/laptops/pr?sid=6bo,b5g&marketplace=FLIPKART')
contenido = driver.page_source
soup = BeautifulSoup(contenido, 'html.parser')
productos = soup.find_all('div', attrs={"class": "_4rR01T"})
precios = soup.find_all('div', attrs={"class": "_30jeq3 _1_WHN1"})
raitings = soup.find_all('div', attrs={"class": "_3LWZlK"})
for producto in productos:
    products.append(producto.text)

for precio in precios:
    precio_sin_coma = precio.text.replace(',', '')
    precio_sin_simbolo = precio_sin_coma.replace('₹', '')
    print(precio_sin_simbolo)
    en_dolares = 0.012 * float(precio_sin_simbolo)
    prices.append(en_dolares)

#for rate in raitings:
    #ratings.append(rate.text)
for i, s in enumerate(raitings):
    if i < 24:
        ratings.append(s.text)
        print(s.text)
    else:
        break
print(len(products))
print(len(prices))
print(len(ratings))
df = pd.DataFrame({'producto':products,'precio':prices,'raitings':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')