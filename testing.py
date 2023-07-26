import requests
import urllib.request
import os
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

# r = requests.get("https://www.pokemon.com/us/pokedex")

# urllib.request.urlretrieve("https://www.pokemon.com/us/pokedex", "temp.html")

# filename = 'file:///'+os.getcwd()+'/'+'temp.html'
# webbrowser.open_new_tab(filename)

path = '/Users/preas/Downloads/chromedriver_win32' 
driver = webdriver.Chrome()
driver.implicitly_wait(200)
driver.get('https://www.pokemon.com/us/pokedex')
driver.maximize_window()
element = 'h5'
#time.sleep(5)
element = driver.find_elements(By.TAG_NAME,'h5')

#driver.implicitly_wait(200)
#element_text = element.text

input("Press ENTER when ready")

print("This is the print: \n")
print("This is element_test: ")

for e in element:
    print(e.text)


#.quit() dumps contents so needs to executed last
driver.quit()






#Need to make into a function, show the user the webpage before the scrape; hopefully that will allow the user to modify "see more.." buttons to get a full scrape,
#Show the user an outline of what is being scraped from the webpage, make sure this can be used with a string being fed; so we can edit attributes easier


#We must give the user time to load the entirety of the webpage, this will allow the user to scrape all elements