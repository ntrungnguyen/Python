from tkinter import BOTH, SUNKEN, Button, Frame, Tk
from tkinter.colorchooser import askcolor


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Color chooser')
        self.pack(fill=BOTH, expand=1)

        self.btn = Button(self, text='Choose Color', command=self.onChoose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def onChoose(self):
        #Gọi hàm askcolor để hiển thị hộp thoại chọn màu
        #Hàm này trả về 1 tuple, bên trong tuple này có 2 phần tử
        #1 tuple gồm 3 giấ trị R-G-B
        #1 giá trị màu dạng hexa
        #Xài print(hx) bên trong onChoose() để biết giá trị hexa
        #dùng giá trị hexa để đặt làm màu nền cho Frame
        (rbg, hx) = askcolor()
        self.frame.config(bg=hx)

root = Tk()
ex = Example(root)
root.geometry('300x150+300+300')
root.mainloop()