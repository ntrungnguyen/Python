import tkinter as tk

root = tk.Tk()

root.geometry('600x400')

loaivat = tk.StringVar()
ten = tk.StringVar()
giong = tk.StringVar()
tuoi = tk.StringVar()

def submit():
    loai = loaivat.get()
    tenvat = ten.get()
    giongloai = giong.get()
    tuoi = tuoi.get()

class Animal():
    def __init__(self, loai: str, ten: str, tuoi: int, giong:str) -> None:
        self._loai = loai
        self._ten = ten
        self._tuoi = tuoi
        self._giong = giong

class Dog(Animal):
    def __init__(self, loai: str, ten: str, tuoi: int, giong: str) -> None:
        super().__init__(loai, ten, tuoi, giong)
        
    def __str__(self) -> str:
        return super().__str__()
    
    def voice(self):
        return "Gau Gau Gau"
    
    
class Frog(Animal):
    def __init__(self, loai: str, ten: str, tuoi: int, giong: str) -> None:
        super().__init__(loai, ten, tuoi, giong)
        
    def __str__(self) -> str:
        return super().__str__()
    
    def voice(self):
        return "Ech Op"
    
    
class Kitten(Animal):
    def __init__(self, loai: str, ten: str, tuoi: int, giong: str) -> None:
        super().__init__(loai, ten, tuoi, giong)
        
    def __str__(self) -> str:
        return super().__str__()
    
    def voice(self):
        return "Meo Meo Meo"
    
    
class Tomcat(Animal):
    def __init__(self):
        pass


loaivat_label = tk.Label(root, text='Loài vật', font=('calibre',10,'bold'))
loaivat_entry = tk.Entry(root, textvariable=loaivat_label, font=('calibre', 10,'normal'))

ten_label = tk.Label(root, text='Tên', font=('calibre', 10, 'bold'))
ten_entry = tk.Entry(root, textvariable=ten_label, font=('calibre',10,'normal'))

giong_label = tk.Label(root, text='Giống', font=('calibre', 10, 'bold'))
giong_entry = tk.Entry(root, textvariable=giong_label, font=('calibre',10,'normal'))

tuoi_label = tk.Label(root, text='Tuổi', font=('calibre', 10, 'bold'))
tuoi_entry = tk.Entry(root, textvariable=tuoi_label, font=('calibre',10,'normal'))

sub_btn = tk.Button(root, text='Submit', command=submit)

loaivat_label.grid(row=0,column=0)
loaivat_entry.grid(row=0,column=1)
ten_label.grid(row=1,column=0)
ten_entry.grid(row=1,column=1)
giong_label.grid(row=2,column=0)
giong_entry.grid(row=2,column=1)
tuoi_label.grid(row=3,column=0)
tuoi_entry.grid(row=3,column=1)


sub_btn.grid(row=4,column=1)

root.mainloop()

