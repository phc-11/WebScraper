import os
import pip._vendor.requests 
import requests
from bs4 import BeautifulSoup
import scraperControl
import scraperView

URL = input("Enter the webpage you would like to scrape:").rstrip()
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

elementType = input("What HTML element would you like to scrape for (Class, Div, ID, etc.)")

elementName = input("What is the name of the element(s) you would like to scrape?")


if (elementType == "Class"):
    results = soup.find(class_=elementName)


print(results.text)