from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

global root

#Remember to always pack on a seperate line if applicable

#Declare our function that will serve as our root pane
def rootPane():

    #Initialize the pane
    root = Tk()

    #Set the size of the pane
    #root.geometry("800x800")

    #Set the title of the pane
    root.title('Web Scraper')

    #Set the pane to NOT be resizeable
    root.resizable(False,False)

    #Set the title at the top of the pane, using pack to locate the text (pady = offset for y coordinate, padx = offset for x coordinates)
    Label(root, text="Webscraper", font=('Times New Roman bold',20)).grid(row=0,column=0)

    #Creating a text box that the user can input the data into
    #bg changes the background color of the text box, fg changes the text color
    #urlText = Text(root, width = 30, height = 1, bg = "gray71",fg="#fff",font=('Times New Roman bold',10))
    #urlText.pack(pady=50)


    #Use an entry rather than a Text, entry supports single line input while text handles multi line inputs

    URLLabelText = StringVar()
    URLLabelText.set("Enter the URL:")

    URLLabel = Label(root, textvariable=URLLabelText, font=('Times New Roman bold', 10), width=50)
    #URLLabel.pack(side=LEFT)
    URLLabel.grid(row=1,column=0)
    entry1 = Entry(root,width=50)
    entry1.grid(row=2,column=0)



    #Create a button to export the input to the stdout
    buttonPrint = Button(root, height=5,width=10,text="Export",command=lambda: getInput(entry1))
    buttonPrint.grid(row=3,column=0)

    temp = entry1.get()
    print(temp)


    #Execute the pane
    root.mainloop()



def getInput(entry1):
    val = entry1.get()
    print(val)

#Calling for testing purposes
rootPane()
