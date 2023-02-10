from tkinter import *
from tkinter import ttk
import db_access
import requests

class Table(Frame):
    
    def __init__(self,master):
        Frame.__init__(self, master,width=800)
        ref= db_access.access_db()
        self.data = ref.get()
        self.data_header = ['user_name' ,
                        'user_citizenship',
                        'user_age',
                        'user_gender',
                        'user_profession',
                        'user_edu',
                        'user_income',
                        'user_email',
                        'user_phoneno',
                        'user_homeno',
                        'user_state']
        self.create_table()
    
    def create_table(self):
        
        table_frame = Frame(self,width=850,height=500)
        table_frame.grid(row=0,column=0,padx=25,  pady=5)
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_propagate(0)

        button_frame = Frame(self)
        button_frame.grid(row=2,column=0,padx=25,  pady=20)

        self.data_header.insert(0,'num')

        self.tree = ttk.Treeview(table_frame, columns= self.data_header, show='headings')

        for i in self.data_header:
            self.tree.column(i, anchor='center')
        self.tree.grid(row=0, column=0, sticky='nsew')

        for i in self.data_header:
            self.tree.heading(i, text= i)

        names = []
        num = 0 
        for i in self.data : 
            num+=1
            names.append((num,
                        self.data[i]['user_name'],
                        self.data[i]['user_citizenship'],
                        self.data[i]['user_age'],
                        self.data[i]['user_gender'],
                        self.data[i]['user_profession'],
                        self.data[i]['user_edu'],
                        self.data[i]['user_income'],
                        self.data[i]['user_email'],
                        self.data[i]['user_phoneno'],
                        self.data[i]['user_homeno'],
                        self.data[i]['user_state']))

        for i in names:
            self.tree.insert('', END, values= i)

        scrollbary = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        scrollbary.grid(row=0, column=1, sticky='nse')
        scrollbarx = ttk.Scrollbar(self, orient=HORIZONTAL, command=self.tree.xview)
        scrollbarx.grid(row=1, column=0, sticky='wes')

        self.tree.configure(xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

        return_button = Button(button_frame,text= 'Return to Main Menu',width= 15,command =lambda: self.master.switch_frame("Main_Frame"))
        return_button.grid(row = 0,column= 0,padx= 5)
        add_button = Button(button_frame,text='add',width=15,command=lambda: self.add_item())
        add_button.grid(row=0,column=1,padx= 5)
        edit_button = Button(button_frame,text='edit',width=15,command=lambda:self.edit_item())
        edit_button.grid(row=0,column=2,padx= 5)
        del_button = Button(button_frame,text='delete',width=15,command=lambda:self.delete_data())
        del_button.grid(row=0,column=3,padx= 5)
        save_button = Button(button_frame,text='update database',width=15,command= lambda: self.update_db())
        save_button.grid(row=0,column=4,padx= 5)
        
    def add_item(self):
        add_window= Toplevel(self)
        add_window.geometry("500x500")
        add_window.title('Add Value')
        add_window.columnconfigure((0,1), minsize=100)
        add_window.rowconfigure((0), minsize=60)
        
        add_window_data_frame = Frame(add_window,width=400,height=400)
        add_window_data_frame.grid(row=0, column=0,padx=50)
        add_window_data_frame.grid_rowconfigure(0, weight=1)
        add_window_data_frame.grid_columnconfigure(0, weight=1)
        add_window_data_frame.grid_propagate(0)
            
        add_window_button_frame = Frame(add_window)
        add_window_button_frame.grid(row=1, column=0)
    
        count = 0
        self.data_input=[None]*len(self.data_header)
        for i in self.data_header:
            textlabel=Label(add_window_data_frame,text=i,width=15)
            textlabel.grid(column=0,row=count+2,sticky='e')
            self.data_input[count] = Entry(add_window_data_frame,width=30,justify=CENTER)
            self.data_input[count].grid(column=1,row=count+2,padx=35,pady = 5)
            count=count+1
            
        back_button = Button(add_window_button_frame,text='back to table',width=10,command=add_window.destroy)
        back_button.grid(row=0,column=0,padx= 5,pady= 5)
            
        save_button = Button(add_window_button_frame,text='save',width=10,command=lambda: self.append_item())
        save_button.grid(row=0,column=1,padx= 5,pady= 5)
        
    def append_item(self):
        new_data=[]
        for i in self.data_input:
            new_data.append(i.get())
        self.tree.insert('', END, values= new_data)
    
    def delete_data(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)

    def edit_item(self):
            selected = self.tree.item(self.tree.focus())
            edit_window= Toplevel(self)
            edit_window.geometry("500x500")
            edit_window.title('Edit Value')
            edit_window.columnconfigure((0,1), minsize=100)
            edit_window.rowconfigure((0), minsize=60)
            if selected.get('values')=='':
                Label(edit_window, text='Please select any row first before editing by clicking on the row').pack(side = 'top')
            else:
                edit_window_data_frame = Frame(edit_window,width=400,height=400)
                edit_window_data_frame.grid(row=0, column=0,padx=50)
                edit_window_data_frame.grid_rowconfigure(0, weight=1)
                edit_window_data_frame.grid_columnconfigure(0, weight=1)
                edit_window_data_frame.grid_propagate(0)
                
                edit_window_button_frame = Frame(edit_window)
                edit_window_button_frame.grid(row=1, column=0)
        
                count = 0
                for i in self.data_header:
                    textlabel=Label(edit_window_data_frame,text=i,width=15)
                    textlabel.grid(column=0,row=count+2,sticky='e')
                    count=count+1
                
                count = 0
                
                self.data_input=[None]*len(selected.get('values'))
                for i in selected.get('values'):
                    self.data_input[count] = Entry(edit_window_data_frame,width=30,justify=CENTER)
                    self.data_input[count].insert(0, i)
                    self.data_input[count].grid(column=1,row=count+2,padx=35,pady = 5)
                    count=count+1
                
                back_button = Button(edit_window_button_frame,text='back to table',width=10,command=edit_window.destroy)
                back_button.grid(row=0,column=0,padx= 5,pady= 5)
                
                save_button = Button(edit_window_button_frame,text='save',width=10,command=lambda: self.change_data())
                save_button.grid(row=0,column=1,padx= 5,pady= 5)

    def change_data(self):
        new_data=[]
        for i in self.data_input:
            new_data.append(i.get())
        self.tree.item(self.tree.focus(),values=new_data)
        self.popupmsg()

    def popupmsg(self):
            popup = Toplevel(self)
            popup.wm_title("")
            popup.geometry("200x100")
            label = ttk.Label(popup, text='Table updated successfully',padding=10)
            label.pack(side="top", fill="x")
            B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
            B1.pack(pady=10)

    def update_db(self):
        requests.delete(url = 'https://e-legal-84a59-default-rtdb.asia-southeast1.firebasedatabase.app/.json')
        for i in self.tree.get_children():
            user_data = {'user_name' : self.tree.item(i)['values'][1],
                        'user_citizenship' : self.tree.item(i)['values'][2],
                        'user_age' : self.tree.item(i)['values'][3],
                        'user_gender' :self.tree.item(i)['values'][4],
                        'user_profession' : self.tree.item(i)['values'][5],
                        'user_edu' : self.tree.item(i)['values'][6],
                        'user_income' : self.tree.item(i)['values'][7],
                        'user_email' :self.tree.item(i)['values'][8],
                        'user_phoneno' : self.tree.item(i)['values'][9],
                        'user_homeno' : self.tree.item(i)['values'][10],
                        'user_address' : '',
                        'user_city ' : '',
                        'user_state' : self.tree.item(i)['values'][11],
                        'user_postalcode' : '',
                        'spouse_name' : '',
                        'spouse_address' : '',
                        'spouse_no' : '',
                        'complaint_type' : '',
                        'lawyer_name' : '',
                        'lawyer_address' : '',
                        'childname' : [],
                        'childdob' : [],
                        'childschool' : []}
            db_access.add_data(user_data)

if __name__ == "__main__":
    app = Table()
    app.mainloop()