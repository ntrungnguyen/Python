from tkinter import Frame, Menu, Tk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Simple Menu')

        #Tạo menuBar từ lớp Menu
        menuBar = Menu(self.parent)
        self.parent.config(menu=menuBar)

        #Tạo fileMenu từ lớp Menu
        fileMenu = Menu(menuBar)

        #Để thêm các item vào menu, sử dụng phương thức add_command()
        #cho item này gọi đến phương thức onExit()
        fileMenu.add_command(label='Exit', command=self.onExit)

        #Sau khi tạo xong thì gắn menu File vào menu bar bằng phương thức add_cascade
        menuBar.add_cascade(label='File', menu=fileMenu)

    def onExit(self):
        self.quit()

root = Tk()
root.geometry('250x150+300+300')
app = Example(root)
root.mainloop()