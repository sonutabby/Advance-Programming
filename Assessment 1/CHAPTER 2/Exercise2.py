from tkinter import *
import random

#Main application window
app = Tk()
app.title("Managing Layout") #Title of the window

#Constructing four Label widgets with various attributes
bA = Label(app, text="A", width=12, bg='red', relief=GROOVE, bd=5)
bB = Label(app, text="B", width=12, bg='yellow')
bC = Label(app, text="C", width=12, bg='blue')
bD = Label(app, text="D", width=12, bg='white')

#Arranging and configuring the widgets in the window according to their designated locations
bA.pack(side='top', fill=X, expand=1) #Placed at the top, expands in the X direction
bB.pack(side='bottom') #Placed at the bottom
bC.pack(side='left', fill=Y, expand=1) #Placed on the left, expands in the Y direction
bD.pack(side='right') #Placed on the right

app.mainloop() #Running the main event loop to display the window
