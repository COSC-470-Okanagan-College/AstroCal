import tkinter
from tkinter import *

class mainApp(tkinter.Tk):

    #function for MainApp (idk why we need it we just do)
    def __init__(self, *args, **kwargs):

        #function for class app (again idk why but just go with it)
        tkinter.Tk.__init__(self, *args, **kwargs)

        #create a container
        container = tkinter.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        #initialize frame as empty array
        self.frames = {}

        #iterating trhough tuple made of differnet page frames
        for f in (MainPage, Sun, Moon):
            frame = f(container, self)
            #initialize frame of the object from Mainpage, sun, moon. for the loop
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky="nsew")#north south east west
        self.show_frame(MainPage)
    
    #display current frame passed in
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#main page frame
class MainPage(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        #label displaying current frame
        label = tkinter.Label(self, text ="Main Menu")
        #grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        
        #button to launch sun frame
        sunButton = tkinter.Button(self, text ="Sun Information",
        command = lambda : controller.show_frame(Sun))

        sunButton.grid(row = 1, column = 1, padx = 10, pady = 10)
        
        #button to launch mooon frame
        moonButton = tkinter.Button(self, text="Moon Information",
        command = lambda : controller.show_frame(Moon))
        moonButton.grid(row = 2, column = 1, padx = 10, pady = 10)

#Sun page frame
class Sun(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        #label displaying current frame
        label = tkinter.Label(self, text ="Sun Menu")
        #grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        #button to go back to menu frame
        menuButton = tkinter.Button(self, text="Main Menu",
        command = lambda : controller.show_frame(MainPage))
        menuButton.grid(row = 2, column = 1, padx = 10, pady = 10)

#Moon page frame
class Moon(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        #label displaying current frame
        label = tkinter.Label(self, text ="Moon Menu")
        #grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        #button to go back to menu frame
        menuButton = tkinter.Button(self, text="Main Menu",
        command = lambda : controller.show_frame(MainPage))
        menuButton.grid(row = 2, column = 1, padx = 10, pady = 10)



