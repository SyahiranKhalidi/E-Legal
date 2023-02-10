from tkinter import *
from E_Legal_Main import Main_Frame
from E_Legal_Form import Form
from E_Legal_Table import Table

pages = {
    "Main_Frame": Main_Frame, 
    "Form": Form,
    "Table": Table
}

class App(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame("Main_Frame")
    
    def switch_frame(self, page_name):
        cls = pages[page_name]
        new_frame = cls(master = self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        self.geometry('900x600')

if __name__ == "__main__":
    app = App()
    app.mainloop()