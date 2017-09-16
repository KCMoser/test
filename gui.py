# @author:Kyle Moser
from tkinter import*                       #GUI module import
class App(Frame):                          #Defines class called App based on Frame class
    def__init__(self,master):              #Define constructor method
        super(App, self).__init__(master)  #Use frame attributes and methods & frame's master is root window
#Define variables, storage locations
#Define widgets
#--End of Constructor--

# Main
root=Tk()                             #Build standard window object called root
root.title("Aligned Focus")                #Assign title to title bar
root.geometry("400x600")                   #Set window dimensions
app=App(root)        #Create object called app based on App class defined above and pass to root
root.mainloop()                        #Launch window and start event listening