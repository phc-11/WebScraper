from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import *
from selenium.common.exceptions import *
import time


global driver

def Input():
    return 0

def ScrapeInput():
    return 0

def Scrape():
    return 0

#Function to display the webpage before the scrape and initiliaze the driven browser
#Parameters - 
def Initial():
    #Establish ChromeOptions which will allow us to control extra options for our browser driver
    options = webdriver.ChromeOptions()

    #ChromeOption to limit the console bound errors
    options.add_experimental_option('excludeSwitches',['enable-logging'])

    #Try & Exception to handle error logging through the CLI

    try:

    #Enitialize the instance of our browser driver
        driver = webdriver.Chrome(options=options)

    #Tell the driver to wait for the page to initizalize
        driver.implicitly_wait(200)

    #Calls function Input() to prompt user for webpage that we are going to scrape then feeds that string to driver
        driver.get(webpageInput())

    #Call function scrapeInput() to get input from the user about what elements we will scrape from the webpage
        elementGroup, tempTag = scrapeInput()

        element = Scrape(elementGroup, tempTag, driver)




        #Search for the element by CLASS WORKS
            #element = driver.find_elements(By.CLASS_NAME,'id')

    #Except to print an error to the CLI and exit gracefully
 

    except (NoSuchElementException, UnboundLocalError, NoSuchWindowException):
        driver.quit()
        print("An error has occurred.")
        print("Please try again.")
        #driver.quit()
        exit(0)

    except (KeyboardInterrupt):
        driver.quit()
        print("The program was exited by the user's keyboard")
        exit(0)

    except(NoSuchWindowException):
        driver.quit()
        print("The browser was closed! Please keep the browser open until the scrape is completed.")



    #Holds the program so the user can load all elements on the page
    input("Press ENTER when ready")


    #Try & Except to handle manual browser closing.
    try:

        #For loop to print the elements from out element list
        OutputScrape(element)

    #Except to print an error message, quit the driver, and exit the program gracefully
    except: 
        print("Please do not close the browser.")
        print("Please try again.")
        print("Closing program...")
        driver.quit()
        exit(0)



    #.quit() dumps contents so needs to executed last
    driver.quit()





#Will be called to while loop to hold the webpage prepping so user can load all elements, until button is pressed
def Hold():
    return 0






#Will execute the scrape
def Scrape(elementGroup, tempTag, driver):
    scrapeResults = []
    print(elementGroup[0])
    for i in range(len(elementGroup)):
        match elementGroup[i]:
            case "Class":
                print("here2")
                element = driver.find_elements(By.CLASS_NAME,r"{}".format(tempTag))
                print("Here3")


    return element





#Will output the scrape as the user requests
def OutputScrape(elements):

    #For loop to iterate through all elements(e) in list elements
    for e in elements:

        #Print e.text which holds the readable value for the element
        print(e.text)

    #Graceful exit
    return 0




#Takes webpage (String) from the user as input
def webpageInput():

    #Takes input from the user to get the webpage 
    webpage = input("Please enter the webpage:")

    #Returns the string respresentation of the webpage
    return webpage




#Takes input from the user for the Element groups and names of the groups we are going to scrape
def scrapeInput():

    #Takes input from the user for the amount of elements that will be scraped
    scrapeAmount = input("How many elements would you like to scrape?")

    #Establish the array of the Group of the elements (Class, Tag, Div, etc.)
    elementGroup = []

    #Establish the array of the name of the Groups we are going to scrape
    elementTags = []

    #For loop to iterate through the amount of scrapes given by the user.
    for i in scrapeAmount:

        #Print message to the user
        print("What type of group is used for element i *FIX*?(Class,Tag,Etc.):")

        #Take the input from the user for the type of group
        tempIdentifier = input()

        #Append to our array of groups
        elementGroup.append(tempIdentifier)


        #Print message to the user
        print("What is the name of the tag for elementi *FIX*:?")

        #Take the input from the user
        tempTag = input()

        #Append to our array of group names
        elementTags.append(tempTag)

    #Return both arrays
    return elementGroup, tempTag

Initial()
#Need to make into a function, show the user the webpage before the scrape; hopefully that will allow the user to modify "see more.." buttons to get a full scrape,
#Show the user an outline of what is being scraped from the webpage, make sure this can be used with a string being fed; so we can edit attributes easier


#We must give the user time to load the entirety of the webpage, this will allow the user to scrape all elements



#Code that could be used later:

    #Set what element we are going to scrape for
    #element = 'h5'

    #Search for the element by TAG WORKS
    #element = driver.find_elements(By.TAG_NAME,'h5')


    #ChromeOption to set the window to start maximized
    #options.add_argument("--start-maximized")


#TODO: NEED TO FIX SCRAPE(), currently when calling the driver to scrape it wont take our array of strings that hold the Group name. Handle Keyboard Interrupt
#NOTE: I have disbaled some try & except to see error logging