from tkinter import Tk, Frame, BOTH
from tkinter.ttk import Button, Style

class Example(Frame):
    def __init__(self, parent) -> None:
        Frame.__init__(self, parent) #, background='white'# 
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        #Thay đổi tiêu đề của cửa sổ
        self.parent.title('SimpleQuitButton')
        #fill = BOTH sẽ dãn widget ra chiều ngang và chiều rộng
        #Tức là widget đó chiếm toàn bộ không gian cửa sổ
        self.pack(fill = BOTH, expand = 1)
        self.style = Style()
        self.style.theme_use('default')
        
        quitButton = Button(self, text='Quit', command=self.quit)
        quitButton.place(x=50, y=50)

#Tạo cửa sổ gán vào biến root để quản lý
#Cửa sổ luôn phải được tạo trước khi tạo widget   
root = Tk()

#Phương thức geometry quy định kích thước cửa sổ và vị trí
#2 tham số đầu là kích thước cửa sổ
#2 phương thức sau là vị trí cửa sổ
root.geometry('250x150+300+300')

#Tạo 1 frame và gắn vào cửa sổ chính
app = Example(root)
root.mainloop()



# Tạo cửa sổ bằng Tkinter
# from tkinter import Tk, Frame, BOTH
# class Example(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent, background="white")
#         self.parent = parent
#         self.initUI()

#     def initUI(self):
#         self.parent.title("Simple")
#         self.pack(fill=BOTH, expand=1)

# root = Tk()
# root.geometry("250x150+300+300")
# app = Example(root)
# root.mainloop()