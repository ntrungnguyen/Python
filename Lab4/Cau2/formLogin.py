import tkinter as tk

root = tk.Tk()

#windows size
root.geometry('600x400')

#declaring string variable
#for storing name add password
name_var = tk.StringVar()
pass_var = tk.StringVar()

#defining a function 
#get name and pass
#print them on the screen
def submit():
    name = name_var.get()
    password = pass_var.get()

    print('The name is:' + name)
    print('The password is:' + password)

    name_var.set('trungnguyen')
    pass_var.set('trungnguyen')

#label for name
#entry for input
name_label = tk.Label(root, text='Username', font=('calibre',10,'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10,'normal'))

#label for password
pass_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))
#entry for password
pass_entry = tk.Entry(root, textvariable=pass_label, font=('calibre',10,'normal'), show='*')

#button ill call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
pass_label.grid(row=1,column=0)
pass_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

root.mainloop()

