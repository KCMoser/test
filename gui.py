# @author:Kyle Moser
from tkinter import*                        #GUI module import
import logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')   #Set up timestamp and logfile name

def show_button_action(*args):              #Action for button press created, the *args allows enter or button click to work
    print('button has been pressed')        #Do something
    resultText.config(text='I am pressed')  #Changes placeholder from empty to have text
    logging.info('Button pressed')          #Add a logging event to button use
        
root=Tk()                                   #Build standard window object called root
logging.info('App Started')                 #Add a logging event to App Start
root.bind("<Return>", show_button_action)   #Allows for button press or pressing enter to work
root.title("Aligned Focus")                 #Assign title to title bar
root.geometry("600x400")                    #Set window dimensions
genericText=Label(root,text='This is a label for the window',bg="blue",fg="white") #Generic text for window with formatting
genericText.pack(fill=X,padx=5,pady=5)      #Makes text visible in GUI and fills space with formatting
buttonOne=Button(root,text='button text',command=show_button_action) #button with action
buttonOne.pack(padx=5,pady=5)               #Makes button visible in GUI
resultText=Label(root)                      #Creates a placeholder under the button
resultText.pack()                           #Makes placeholder visible in GUI
               
root.mainloop()                             #Launch window and start event listening
logging.info('App Stopped')                 #Add a logging event to App Stop
