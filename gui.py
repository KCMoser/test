# @author:Kyle Moser
from tkinter import*                #GUI module import

def show_button_action():           #Action for button press created
    #print('button has been pressed')#Do something
    response.print('button has been pressed')

root=Tk()                           #Build standard window object called root
root.title("Aligned Focus")         #Assign title to title bar
root.geometry("600x400")            #Set window dimensions
genericText=Label(root,text='This is a label for the window').grid(row=1,column=3,padx=5,pady=5) #Generic text for window
buttonOne=Button(root,text='button text',command=show_button_action).grid(row=2,column=1,padx=5,pady=5) #button with action
response=Label(root,text='start').grid(row=3,column=3,padx=5,pady=5) #set area for button press to show
               
root.mainloop()                     #Launch window and start event listening
