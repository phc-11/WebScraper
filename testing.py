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

#Establish the path to the Chrome Driver
path = '/Users/preas/Downloads/chromedriver_win32' 

#Enitialize the instance of our browser driver
driver = webdriver.Chrome()

#Tell the driver to wait for the page to initizalize
driver.implicitly_wait(200)

#Give the driver the webpage we are going to scrape
driver.get('https://www.pokemon.com/us/pokedex')

#Set the browser window to maximum size
#driver.maximize_window()

#Set what element we are going to scrape for
#element = 'h5'

#Search for the element by TAG WORKS
#element = driver.find_elements(By.TAG_NAME,'h5')

#Search for the element by CLASS WORKS
element = driver.find_elements(By.CLASS_NAME,'id')

#Holds the program so the user can load all elements on the page
input("Press ENTER when ready")

#Error checking
print("This is the print: \n")
print("This is element_test: ")

#For loop to print the elements from out element list
for e in element:
    print(e.text)


#.quit() dumps contents so needs to executed last
driver.quit()






#Need to make into a function, show the user the webpage before the scrape; hopefully that will allow the user to modify "see more.." buttons to get a full scrape,
#Show the user an outline of what is being scraped from the webpage, make sure this can be used with a string being fed; so we can edit attributes easier


#We must give the user time to load the entirety of the webpage, this will allow the user to scrape all elements