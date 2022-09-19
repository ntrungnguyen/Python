from tkinter import BOTH, Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title('Review')

        #frame chính chứa các widget còn lại và frame khác 
        self.pack(fill=BOTH, expand=True)

        #Tạo frame đặt 2 widget (label (hiển thị text) và entry (nhập text).
        #Label có độ dài cố định
        #Entry có độ dài tự động thay đổi theo kích thước cửa sổ nhờ vào fill và expand)
        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text='Title', width = 6)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        #tương tự như frame1
        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text='Author', width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        #label đặt phía trên của frame, text tự động co dãn theo kích thước cửa sổ
        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text='Review', width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

root = Tk()
root.geometry('300x300+300+300')
app = Example(root)
root.mainloop()
    