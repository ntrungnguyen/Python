#Scale là widget hiển thị một thanh cuộn gắn với một khoảng giá trị nào đó
#ví dụ cho hiển thị scale và label, text trên label sẽ thay đổi khi kéo thanh cuộn scale

from tkinter import BOTH, LEFT, Frame, IntVar, Label, Scale, Tk
from tkinter.ttk import Style


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Scale')
        self.style = Style()
        self.style.theme_use('default')

        self.pack(fill=BOTH, expand=1)

        #tạo đối tượng scale, tham số from và to là phạm vi giá trị scale
        #tham số command chỉ định phương thức sẽ được gọi khi di chuyển thanh cuộn
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)

        #giống checkbutton, đối tượng IntVar kết nối đối tượng label bằng tham số textvarible
        #giá trị biến này sẽ được hiển thị trên label
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)

    #khi di chuyển thanh cuộn, phương thức onScale() sẽ được gọi kèm theo giá trị hiện tại của Scale
    #ép từ float sang int đặt làm giá trị của đối tượng intVar
    #text hiển thị trên label sẽ thay đổi theo
    def onScale(self, val):
        v = int(float(val))
        self.var.set(v)

root = Tk()
ex = Example(root)
root.geometry('250x100+300+300')
root.mainloop()