from tkinter import ttk
import tkinter as tk

#creating tkinter window
window = tk.Tk()
window.resizable(width=1, height=1)

#using treeview widget
treev = ttk.Treeview(window, selectmode='browse')

treev.pack(side='right')

#constructing vertical scrollbar
verscrlbar = ttk.Scrollbar(window, orient='vertical', command=treev.yview)

verscrlbar.pack(side='right', fill='x')

#configuring treeview
treev.configure(xscrollcommand=verscrlbar.set)

#defining number of columns
treev['columns'] = ('1', '2', '3')

#defining heading
treev['show'] = 'headings'

#assigning the width and anchor to the
#respective columns

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')

# Assigning the heading names to the
# respective columns
treev.heading("1", text ="Name")
treev.heading("2", text ="Sex")
treev.heading("3", text ="Age")

# Inserting the items and their features to the
# columns built
treev.insert("", 'end', text ="L1",
             values =("Nidhi", "F", "25"))
treev.insert("", 'end', text ="L2",
             values =("Nisha", "F", "23"))
treev.insert("", 'end', text ="L3",
             values =("Preeti", "F", "27"))
treev.insert("", 'end', text ="L4",
             values =("Rahul", "M", "20"))
treev.insert("", 'end', text ="L5",
             values =("Sonu", "F", "18"))
treev.insert("", 'end', text ="L6",
             values =("Rohit", "M", "19"))
treev.insert("", 'end', text ="L7",
             values =("Geeta", "F", "25"))
treev.insert("", 'end', text ="L8",
             values =("Ankit", "M", "22"))
treev.insert("", 'end', text ="L10",
             values =("Mukul", "F", "25"))
treev.insert("", 'end', text ="L11",
             values =("Mohit", "M", "16"))
treev.insert("", 'end', text ="L12",
             values =("Vivek", "M", "22"))
treev.insert("", 'end', text ="L13",
             values =("Suman", "F", "30"))

window.mainloop()