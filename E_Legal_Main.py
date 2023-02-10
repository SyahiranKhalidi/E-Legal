from tkinter import *

class Main_Frame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master,width=800)
        # Main_Frame.grid(row=0,column=0)

        MainPage_Title = Label(self,text = 'Welcome to E-Legal',font=('Times',25),width=20)
        MainPage_Title.grid(row=0,column=0,padx = 10,pady=30)

        Form_Button = Button(self,text = 'Complaint Form',width=15,command = lambda: master.switch_frame("Form"))
        Form_Button.grid(row=1,column=0,pady=5)

        Table_Button = Button(self,text = 'View Database',width=15,command = lambda: master.switch_frame("Table"))
        Table_Button.grid(row=2,column=0,pady=10)
    

# def changeto_FormFrame(Main_Frame):
#     Main_Frame.destroy()
#     Form
    
# create_MainMenu()