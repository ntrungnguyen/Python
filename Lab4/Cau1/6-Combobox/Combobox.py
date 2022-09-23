from tkinter import Tk, ttk


#creating tkinter window
window = Tk()
window.title('ComboBox')
window.geometry('500x250')

#Label text for title
ttk.Label(window, text = 'GFG Combobox Widget', 
        background='green',
        foreground='white',
        font=('Times New Roman', 15)).grid(row=0, column=1)

ttk.Label(window, text ='Select the Month:')