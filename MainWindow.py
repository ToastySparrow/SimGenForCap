from tkinter import  ttk, Tk
from tkinter.constants import DISABLED, NORMAL
from SimsGenerator import *


class SimWindow():

    def __init__(self):
        pass


    def ButtonAction(): # This is for when the button is pressed, the text will be destroyed if it exists and a new set up random values will take its place
        global Label #Im not sure why... but if this isnt global "Label.destroy" doesnt work... probably has to do with it being created after...
        try:
            Label.destroy()
        except:
            pass
        Label = ttk.Label(Root, text=TraitsClass(AllTraits,Jobs).NumberOfSims(AllTraits,Jobs),font=("Times",15))
        Label.pack()



    def window(): #General window init and the main loop
        global Root
        Root = Tk()
        Root.title("Sim Household Generator")
        Root.geometry("1280x720")
        Button1 = ttk.Button(Root,text="New Sims",command=SimWindow.ButtonAction,state=NORMAL).pack()
        
        Root.mainloop()

        
