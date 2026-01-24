import requests
from bs4 import BeautifulSoup

url = "https://arzdigital.com/coins/bitcoin/"

response = requests.get(url).text

soup = BeautifulSoup(response, "html.parser")

price = soup.find("div", class_="arz-coin-page-data__coin-price coinPrice btcprice pulser-dollar-bitcoin")
print(price.text)

price_toman = soup.find("div", class_="arz-coin-page-data__coin-toman-price")
print(price_toman.text)