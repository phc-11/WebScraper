import os
import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup

URL = "https://pokemondb.net/pokedex/all"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

results = soup.find(class_="cell-name")

print(results.text)