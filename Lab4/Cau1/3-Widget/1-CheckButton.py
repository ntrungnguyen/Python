from tkinter import BOTH, BooleanVar, Checkbutton, Frame, Tk


class Example(Frame):
    def __init__(self, parent):
      Frame.__init__(self, parent)

      self.parent = parent
      self.initUI()

    def initUI(self):
        self.parent.title('CheckButton')
        self.pack(fill=BOTH, expand=True)

        #BooleanVar: đối tượng này được kết nối với Checkbutton
        #Mỗi khi trạng thái thay đổi thì giá trị self.var cũng thay đổi
        self.var = BooleanVar()

        #Tạo Checkbutton, kết nối biển var thông qua tham số varible
        #command chỉ định phương thức nào sẽ được gọi khi check (onclick)
        cb = Checkbutton(self, text='Show Title', variable=self.var, command=self.onClick)

        #sử dụng phương thức select() để thiết lập trạng thái check cho button
        cb.select()
        cb.place(x=50, y=50)

    def onClick(self):
        #hiện/ẩn tiêu đề thông qua master.title()
        #kiểm tra checkbutton có được check hay không qua thuộc tính self.var
        if self.var.get() == True:
            self.master.title('CheckButton')
        else:
            self.master.title('')

root = Tk()
root.geometry('250x150+300+300')
app = Example(root)
root.mainloop()