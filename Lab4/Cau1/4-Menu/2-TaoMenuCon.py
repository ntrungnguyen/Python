from tkinter import Frame, Menu, Tk


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('SubMenu')

        menuBar = Menu(self.parent)
        self.parent.config(menu = menuBar)

        fileMenu = Menu(menuBar)
        
        #Tạo menu con như tạo menu thường ở lớp Menu
        submenu = Menu(fileMenu)
        submenu.add_command(label='New feed')
        submenu.add_command(label='Bookmarks')
        submenu.add_command(label='Mail')

        #Thêm menu con bằng phương thức add_cascade từ menu cha
        #truyền tham chiếu đến menu con vào tham số menu
        fileMenu.add_cascade(label='Import', menu=submenu)

        #hiển thị separator (đường kẻ ngang) 
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.onExit)

        menuBar.add_cascade(label='File', menu=fileMenu)

    def onExit(self):
        self.quit()

root = Tk()
root.geometry('250x150+300+300')
app = Example(root)
root.mainloop()