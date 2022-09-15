from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title('Button')
        self.style = Style()
        self.style.theme_use('default')
        
        #Tạo frame, frame này chiếm phần lớn S frame chính
        #Tham số relief mổ phỏng hiệu ứng 3D của Frame
        #Giá trị khác: FLAT, SUNKEN, GROOVE, RIDGE
        #Borderwidth: đường viền. Mặc định = 0
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        
        #Tạo nút close
        #Phương thức Pack quy định cách hiển thị trên cửa sổ
        #side = RIGHT, đưa button vào vị trí bến phải
        #padx pady: khoảng cách button với widget khác và với
        #đường viền cửa sổ chính (5px)
        closeButton = Button(self, text='Close')
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        
        okButton = Button(self, text='OK')
        okButton.pack(side=RIGHT)
        
root = Tk()
root.geometry('300x200+300+300')
app = Example(root)
root.mainloop()