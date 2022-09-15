from tkinter import BOTH
from tkinter.ttk import Frame


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title('Review')
        self.pack(fill=BOTH, expand=True)
    