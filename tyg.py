# import tkinter module
from tkinter import *

# create a tkinter window
master = Tk()

# Open window having dimension 200x100
master.geometry('200x100')

# Create a Button
button = Button(master,
                text='Submit',
                bg='white',
                activebackground='blue').pack()

master.mainloop()