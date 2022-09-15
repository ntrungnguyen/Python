from tkinter import BOTH, Label, Tk
from tkinter.ttk import Style, Frame
from PIL import Image, ImageTk

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        self.parent.title('Absolute positioning')
        self.pack(fill=BOTH, expand=1)
        
        #Tô màu nền là màu xám
        Style().configure('TFrame', background='#333')
        
        #Tạo đối tượng ảnh và tải chúng vào chương trình
        bard = Image.open('UseCase_N01.png')
        bard = bard.resize((100,100), Image.Resampling.LANCZOS)
        bardejov = ImageTk.PhotoImage(bard)
        
        #Tạo lớp dùng để hiển thị chữ và hình ảnh
        label11 = Label(self, image=bardejov)
        label11.image = bardejov
        
        #Lưu lại tham chiếu đến ảnh, nếu không sẽ bị xóa
        label11.place(x=20,y=20)
        
        
        rot = Image.open('UseCase_N01.png')
        rot = rot.resize((100,100), Image.Resampling.LANCZOS)
        rotunda = ImageTk.PhotoImage(rot)
        label12 = Label(self, image=rotunda)
        label12.image = rotunda
        label12.place(x=40, y=160)
        
        
        minc = Image.open('UseCase_N01.png')
        minc = minc.resize((100,100), Image.Resampling.LANCZOS)
        mincol = ImageTk.PhotoImage(minc)
        label13 = Label(self, image=mincol)
        label13.image = mincol
        label13.place(x=170, y=50)
        
root = Tk()
root.geometry('300x280+300+300')
app = Example(root)
root.mainloop()