from tkinter import *
from tkinter import ttk
from db_access import *
import db_filler_databanks  
import random
import names

class Form(Canvas):
    def __init__(self,master):
        Canvas.__init__(self,master)
        
        self.window_frame = Frame(self)
        # self.scroll_frame = Frame(self).grid(row=0,column=1)
        self.create_window(0, 0, anchor='nw', window=self.window_frame)

        self.user_name = StringVar()
        self.user_citizenship = StringVar()
        self.user_gender= StringVar()
        self.user_age = StringVar()
        self.user_profession = StringVar()
        self.user_edu = StringVar()
        self.user_income = StringVar()
        self.user_email = StringVar()
        self.user_phoneno= StringVar()
        self.user_homeno = StringVar()
        self.user_address = StringVar()
        self.user_city = StringVar()
        self.user_state = StringVar()
        self.user_postalcode = StringVar()
        self.spouse_name = StringVar()
        self.spouse_no= StringVar()
        self.spouse_address = StringVar()
        self.complaint_type = StringVar()
        self.lawyer_name= StringVar()
        self.lawyer_address = StringVar()
        self.total_rows = 2
        self.total_columns = 3
        self.childname = []
        self.childdob = []
        self.childschool = []
        self.main_frames_setup()
        
        scroll_y = Scrollbar(self, orient="vertical", command=self.yview)
        self.update_idletasks()
        self.configure(scrollregion=self.bbox('all'), 
                        yscrollcommand=scroll_y.set)
        self.pack(fill='both', expand=True, side='left')
        scroll_y.pack(fill='y', side='right',anchor='w')
        
    def main_frames_setup(self):
        self.header_frame = LabelFrame(self.window_frame,bg = 'brown',width=850,height=100)
        self.header_frame.grid(row=0,column=0,padx=25,  pady=5)
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_propagate(0)
        self.create_header_frame()
        
        self.personaldetails_frame = LabelFrame(self.window_frame,bg='grey',width=850,height=310)
        self.personaldetails_frame.grid(row=1,column=0,padx=25,pady=5)
        self.personaldetails_frame.grid_propagate(0)
        self.create_personaldetails_frame()
        
        self.other_frame = LabelFrame(self.window_frame,bg='grey',width=850,height=200)
        self.other_frame.grid(row=2,column=0,padx=25,pady=5,sticky='w')
        self.other_frame.grid_propagate(0)
        self.create_other_frame()

        self.child_frame = LabelFrame(self.window_frame,bg='grey',width=850,height=250)
        self.child_frame.grid(row=3,column=0,padx=25,pady=5,sticky='w')
        self.child_frame.grid_propagate(0)
        self.create_child_frame()
        
        self.button_frame = Frame(self.window_frame,bg = 'grey')
        self.button_frame.grid(row=4,column=0,padx=25,pady=5)
        self.create_button_frame()

    def create_header_frame(self):
        form_title = Message(self.header_frame, text='Complaint Form',width=500, font= ('Times', 25))
        form_title.grid(row=0,column=0)
        form_title.grid_rowconfigure(1, weight=1)
        form_title.grid_columnconfigure(1, weight=1)

    def create_personaldetails_frame(self):
        
        personaldetails_header = Label(self.personaldetails_frame,text = "Personal Information",bg='grey',font= ('Times', 15))
        personaldetails_header.grid(row = 0,column = 0,sticky='w',padx = 10, pady= 5)
        
        bottom_lframe = Frame(self.personaldetails_frame,bg='grey',width=400,height=250)
        bottom_lframe.grid(row=1,column=0,padx=10,pady=5,sticky='w')
        bottom_lframe.grid_propagate(0)

        Label(bottom_lframe ,text = "Full Name",bg='grey').grid(row = 0,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Citizenship",bg='grey').grid(row = 1,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Gender",bg='grey').grid(row = 2,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Age",bg='grey').grid(row = 3,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Profession",bg='grey').grid(row = 4,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Education",bg='grey').grid(row = 5,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_lframe ,text = "Gross Income",bg='grey').grid(row = 6,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)

        genders = ['Male','Female']
        educations = ['SPM','Degree','Masters','Others']
        income_lvl = ['RM 1500.00 and less','RM 1500.00 to RM 5000.00','RM 5000.00 to RM 10000.00', 'RM 10000.00 and above']

        Entry(bottom_lframe,width=45,textvariable= self.user_name).grid(row = 0,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_lframe,width=20,textvariable = self.user_citizenship).grid(row = 1,column = 1,padx = 5, pady= 5,sticky='w')
        ttk.Combobox(bottom_lframe,state= 'readonly',values = genders,textvariable= self.user_gender,width=7).grid(row = 2,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_lframe,width=10,textvariable = self.user_age).grid(row = 3,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_lframe,width=20,textvariable = self.user_profession).grid(row = 4,column = 1,padx = 5, pady= 5,sticky='w')
        ttk.Combobox(bottom_lframe,state= 'readonly',values = educations,textvariable = self.user_edu,width=10).grid(row = 5,column = 1,padx = 5, pady= 5,sticky='w')
        ttk.Combobox(bottom_lframe,state= 'readonly',values = income_lvl, textvariable= self.user_income,width=25).grid(row = 6,column = 1,padx = 5, pady= 5,sticky='w')

        bottom_rframe = Frame(self.personaldetails_frame,bg='grey',width=400,height=250)
        bottom_rframe.grid(row=1,column=1,padx=10,pady=5,sticky='e')
        bottom_rframe.grid_propagate(0)

        Label(bottom_rframe ,text = "Email",bg='grey').grid(row = 0,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "Phone Number",bg='grey').grid(row = 1,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "Home Number",bg='grey').grid(row = 2,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "Address",bg='grey').grid(row = 3,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "City",bg='grey').grid(row = 4,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "State",bg='grey').grid(row = 5,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)
        Label(bottom_rframe ,text = "Postal Code",bg='grey').grid(row = 6,column = 0,sticky='w'+'e'+'n'+'s',padx = 5, pady= 5)

        states = ['Perlis','Kelantan','Kedah','Perak','Pulau Pinang','Terengganu','Pahang','Selangor','Kuala Lumpur','Negeri Sembilan','Johor','Melaka','Sabah','Sarawak']

        Entry(bottom_rframe,width=30,textvariable = self.user_email).grid(row = 0,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_rframe,width=20,textvariable = self.user_phoneno).grid(row = 1,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_rframe,width=20,textvariable = self.user_homeno).grid(row = 2,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_rframe,width=45,textvariable = self.user_address).grid(row = 3,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_rframe,width=20,textvariable = self.user_city).grid(row = 4,column = 1,padx = 5, pady= 5,sticky='w')
        ttk.Combobox(bottom_rframe,state= 'readonly',values = states,textvariable=self.user_state).grid(row = 5,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(bottom_rframe,width=10,textvariable = self.user_postalcode).grid(row = 6,column = 1,padx = 5, pady= 5,sticky='w')

    def create_other_frame(self):

        spouse_frame = Frame(self.other_frame,bg='grey',width=400,height= 150)
        spouse_frame.grid(row=0,column=0,padx=10,pady=5,sticky='w')
        spouse_frame.grid_propagate(0)

        Label(spouse_frame,text = "Spouse/Company/Employeer Details",bg='grey',font= ('Times', 15)).grid(row = 0,column = 0,sticky='w', padx = 10, pady= 5)

        spouse_frame_data = Frame(spouse_frame,bg='grey',width=400,height=200)
        spouse_frame_data.grid(row=2,column=0,padx=10,pady=5,sticky='w')
        spouse_frame.grid_propagate(0)

        Label(spouse_frame_data ,text = "Full Name",bg='grey').grid(row = 1,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)
        Label(spouse_frame_data ,text = "Contact No.",bg='grey').grid(row = 2,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)
        Label(spouse_frame_data ,text = "Address",bg='grey').grid(row = 3,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)

        Entry(spouse_frame_data,width=45,textvariable = self.spouse_name ).grid(row = 1,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(spouse_frame_data, width=45,textvariable = self.spouse_no).grid(row = 2,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(spouse_frame_data,width=45,textvariable = self.spouse_address).grid(row = 3,column = 1,padx = 5, pady= 5,sticky='w')

        complaint_frame = Frame(self.other_frame,bg='grey',width=400,height=180)
        complaint_frame.grid(row=0,column=1,padx=10,pady=5,sticky='w')
        complaint_frame.grid_propagate(0)

        Label(complaint_frame ,text = "Lawyer's Detail (if any)",bg='grey',font= ('Times', 15)).grid(row = 1,column = 0,sticky='w', padx = 5, pady= 5)

        complaint_type_frame = Frame(complaint_frame,bg='grey',width=375,height=50)
        complaint_type_frame.grid(row=0,column=0,padx=10,pady=5,sticky='w')
        complaint_type_frame.grid_propagate(0)

        complaint_choice = ['Family & Divorce','Employment','Tenancy','Business/Commercial']

        Label(complaint_type_frame ,text = "Type of complaint",bg='grey').grid(row = 0,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)
        ttk.Combobox(complaint_type_frame,state= 'readonly',values =complaint_choice,textvariable= self.complaint_type,width=20).grid(row = 0,column = 1,padx = 5, pady= 5,sticky='w')

        lawyer_frame = Frame(complaint_frame,bg='grey',width=375,height=100)
        lawyer_frame.grid(row=2,column=0,padx=10,pady=5,sticky='w')
        lawyer_frame.grid_propagate(0)

        Label(lawyer_frame ,text = "Name:",bg='grey').grid(row = 0,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)
        Label(lawyer_frame ,text = "Address",bg='grey').grid(row = 1,column = 0,sticky='w'+'e'+'n'+'s', padx = 5, pady= 5)

        Entry(lawyer_frame, width=45,textvariable = self.lawyer_name).grid(row = 0,column = 1,padx = 5, pady= 5,sticky='w')
        Entry(lawyer_frame,width=45,textvariable = self.lawyer_address).grid(row = 1,column = 1,padx = 5, pady= 5,sticky='w')

    def create_child_frame(self):
        
        global child_table_frame

        Label(self.child_frame,text = "Detail of child (if any):",bg='grey',font= ('Times', 15)).grid(row = 0,column = 0,sticky='w', padx = 10, pady= 20)

        self.child_table_frame = Frame(self.child_frame,bg='grey',width=775,height=300)
        self.child_table_frame.grid(row=1,column=0,padx=10)

        t = self.create_table()
        add_button = Button(self.child_table_frame,text= 'Add Rows',width= 10, command= self.add_tablerows)
        add_button.grid(row = 8,column= 1,pady= 10)
    
    def create_button_frame(self):
        
        return_button = Button(self.button_frame,text= 'Return to Main Menu',width= 15,command =lambda: self.master.switch_frame("Main_Frame"))
        return_button.grid(row = 0,column= 0)
        
        submit_button = Button(self.button_frame,text= 'Submit',width= 10,command= self.submit)
        submit_button.grid(row = 0,column= 1)

        autofill_button = Button(self.button_frame,text= 'Autofill',width= 10,command= self.autofill)
        autofill_button.grid(row = 0,column= 2)       
    
    def create_table(self):
        header = ['Name','Date of Birth','School']
        for i in range(3):
            e = Label(self.child_table_frame, width=20,text=header[i])
            e.grid(row=0, column=i,padx = 2, pady= 2,sticky='w'+'e'+'n'+'s')
        self.add_tablerows()    

    def add_tablerows(self):
        
        if self.total_rows < 5 : self.total_rows +=1
        self.childname = []
        self.childdob = []
        self.childschool = []
        for i in range(self.total_rows):
            for j in range(self.total_columns):
                e = Entry(self.child_table_frame, width=45)
                e.grid(row=i+1, column=j,padx = 2, pady= 2)
                if j == 0 : self.childname.append(e)
                elif j == 1 : self.childdob.append(e)
                elif j == 2 : self.childschool.append(e)

    def autofill(self):
        
        access_db()
        for i in range(30):
            user_data = { 'user_name' : names.get_full_name(),
                        'user_citizenship' : (random.choice(db_filler_databanks.countries))[1],
                        'user_age' : random.randint(18,60),
                        'user_gender' : random.choice(db_filler_databanks.genders),
                        'user_profession' : random.choice(db_filler_databanks.profession),
                        'user_edu' : random.choice(db_filler_databanks.edu),
                        'user_income' : random.choice(db_filler_databanks.income),
                        'user_email' : f'{random.randint(0000000000,9999999999)}@gmail.com',
                        'user_phoneno' : random.randint(0000000000,9999999999),
                        'user_homeno' : random.randint(0000000000,9999999999),
                        'user_address' : self.user_address.get(),
                        'user_city ' : self.user_city.get(),
                        'user_state' : random.choice(db_filler_databanks.state),
                        'user_postalcode' : self.user_postalcode.get(),
                        'spouse_name' : self.spouse_name.get(),
                        'spouse_address' : self.spouse_address.get(),
                        'spouse_no' : self.spouse_no.get(),
                        'complaint_type' : random.choice(db_filler_databanks.complaint),
                        'lawyer_name' : self.lawyer_name.get(),
                        'lawyer_address' : self.lawyer_address.get(),
                        'childname' : [cell.get() for cell in self.childname],
                        'childdob' : [cell.get() for cell in self.childdob],
                        'childschool' : [cell.get() for cell in self.childschool]}
            add_data(user_data)

    def submit(self):
        user_data = { 'user_name' : self.user_name.get(),
                    'user_citizenship' : self.user_citizenship.get(),
                    'user_gender' : self.user_gender.get(),
                    'user_age' : self.user_age.get(),
                    'user_profession' : self.user_profession.get(),
                    'user_edu' : self.user_edu.get(),
                    'user_income' : self.user_income.get(),
                    'user_email' :self.user_email.get(),
                    'user_phoneno' : self.user_phoneno.get(),
                    'user_homeno' : self.user_homeno.get(),
                    'user_address' : self.user_address.get(),
                    'user_city ' : self.user_city.get(),
                    'user_state' : self.user_state.get(),
                    'user_postalcode' : self.user_postalcode.get(),
                    'spouse_name' : self.spouse_name.get(),
                    'spouse_address' : self.spouse_address.get(),
                    'spouse_no' : self.spouse_no.get(),
                    'complaint_type' : self.complaint_type.get(),
                    'lawyer_name' : self.lawyer_name.get(),
                    'lawyer_address' : self.lawyer_address.get(),
                    'childname' : [cell.get() for cell in self.childname],
                    'childdob' : [cell.get() for cell in self.childdob],
                    'childschool' : [cell.get() for cell in self.childschool]}
        access_db()
        add_data(user_data)

if __name__ == "__main__":
    app = Form()
    app.mainloop()