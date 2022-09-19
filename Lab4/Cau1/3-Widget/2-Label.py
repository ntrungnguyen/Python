#Label dùng để hiển thị text hoặc hình ảnh

from tkinter import Frame, Label, Tk
from PIL import Image, ImageTk

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title('Label')

        self.img = Image.open('../../london.jpg')
        rotunda = ImageTk.PhotoImage(self.img)

        #dùng tham số image khi khởi tạo để gán ảnh vào label
        label = Label(self, image=rotunda)

        #tạo biến để giữ tham chiếu đến ảnh, nếu không bộ tài nguyên của python sẽ xóa ảnh
        label.image = rotunda

        label.pack()
        self.pack()

    def setGeometry(self):
        #cho kích thước màn hình bằng đúng với kích thước ảnh
        w, h = self.img.size
        self.parent.geometry(('%dx%d+300+300') % (w, h))

root = Tk()
ex = Example(root)
ex.setGeometry()
root.mainloop()