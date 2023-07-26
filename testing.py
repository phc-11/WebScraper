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
path = '/Users/preas/Downloads/chromedriver_win32/chromedriver.exe' 

#Establish ChromeOptions which will allow us to control extra options for our browser driver
options = webdriver.ChromeOptions()

#ChromeOption to set the window to start maximized
options.add_argument("--start-maximized")

#ChromeOption to limit the console bound errors
options.add_experimental_option('excludeSwitches',['enable-logging'])

#Try & Exception to handle error logging through the CLI
try:
#Enitialize the instance of our browser driver
    driver = webdriver.Chrome(options=options)

#Tell the driver to wait for the page to initizalize
    driver.implicitly_wait(200)

#Give the driver the webpage we are going to scrape
    driver.get('https://www.pokemon.com/us/pokedex')

#Set what element we are going to scrape for
#element = 'h5'

#Search for the element by TAG WORKS
#element = driver.find_elements(By.TAG_NAME,'h5')

#Search for the element by CLASS WORKS
    element = driver.find_elements(By.CLASS_NAME,'id')

#Except to print an error to the CLI and exit gracefully
except:
    print("An error has occurred.")
    print("Please try again.")
    driver.quit()
    exit(0)


#Holds the program so the user can load all elements on the page
input("Press ENTER when ready")


#Try & Except to handle manual browser closing.
try:

    #For loop to print the elements from out element list
    for e in element:
        print(e.text)

#Except to print an error message, quit the driver, and exit the program gracefully
except: 
    print("Please do not close the browser.")
    print("Please try again.")
    driver.quit()
    exit(0)


#.quit() dumps contents so needs to executed last
driver.quit()






#Need to make into a function, show the user the webpage before the scrape; hopefully that will allow the user to modify "see more.." buttons to get a full scrape,
#Show the user an outline of what is being scraped from the webpage, make sure this can be used with a string being fed; so we can edit attributes easier


#We must give the user time to load the entirety of the webpage, this will allow the user to scrape all elements