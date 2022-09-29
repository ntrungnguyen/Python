from tkinter import Tk, ttk
import tkinter as tk


#creating tkinter window
window = Tk()
window.title('ComboBox')
window.geometry('500x250')

#Label text for title
ttk.Label(window, text = 'GFG Combobox Widget', 
        background='green',
        foreground='white',
        font=('Times New Roman', 15)).grid(row=0, column=1)

ttk.Label(window, text ='Select the Month:', 
font=('Times New Roman', 10)).grid(column=0, row=5, padx=10, pady=25)

#combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27, textvariable=n)

#adding combobox drop down list
monthchoosen['values'] = ('January', 'Februry', 'March', 'April',
'May', 'June', 'July', 'August', 'September', 'October', 
'November', 'December')

monthchoosen.grid(column=1, row=5)
monthchoosen.current()
window.mainloop()