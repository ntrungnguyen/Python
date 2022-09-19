#listbox: hiển thị 1 danh sách các item, người dùng có thể chọn 1 hoặc nhiều item

from tkinter import BOTH, END, Frame, Label, Listbox, StringVar, Tk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Listbox')
        self.pack(fill=BOTH, expand=1)

        #danh sách diễn viên
        acts = ['Scarlet Johansson', 'Rachel Weiss', 'Natalie Portman', 'Jessica Alba']

        #tạo 1 đối tượng Listbox và thêm bằng phương thức insert()
        lb = Listbox(self)

        for i in acts:
            lb.insert(END, i)
        #####

        #khi chọn 1 item thì sự kiện <<ListboxSelect>> được thực thi
        #gán sự kiện này vào phương thức onSelect()
        lb.bind('<<ListboxSelect>>', self.onSelect)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def onSelect(self, val):
        #lấy tham chiếu đến Listbox thông qua thuộc tính val.widget và gán vào sender
        sender = val.widget

        #phương thức curselection() lấy về chỉ số của item được chọn
        idx = sender.curselection()

        #từ chỉ số, lấy giá trị text của item bằng phương thức get(), sau đó bắng vào label
        value = sender.get(idx)

        self.var.set(value)

root = Tk()
ex = Example(root)
root.geometry('300x250+300+300')
root.mainloop()
