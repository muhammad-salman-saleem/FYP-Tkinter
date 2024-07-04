import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("400x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
font1=('Times',18,'normal')
sel=tk.StringVar() # string variable 
my_opts=['Show Two','Show Three'] # options
cb1 = ttk.Combobox(my_w, values=my_opts,width=25,
        textvariable=sel,font=font1) # Combobox
cb1.grid(row=0,column=0,padx=10,pady=20,columnspan=3) # adding to grid
def my_upd(*args):
    for w in my_w.grid_slaves(1): # all elements 
        w.grid_remove()                  # delete elements 
    if(sel.get()=='Show Two'):
        t1 = tk.Text(my_w,  height=1, width=8,bg='yellow') # 
        t1.grid(row=1,column=0,padx=10,pady=20)
        t2 = tk.Text(my_w,  height=1, width=8,bg='yellow') # 
        t2.grid(row=1,column=1,padx=10,pady=20)
    elif(sel.get()=='Show Three'):
        t1 = tk.Text(my_w,  height=1, width=8,bg='yellow') # 
        t1.grid(row=1,column=0,padx=1,pady=20)
        t2 = tk.Text(my_w,  height=1, width=8,bg='yellow') # 
        t2.grid(row=1,column=1,padx=1,pady=20)
        t3 = tk.Text(my_w,  height=1, width=8,bg='yellow') # 
        t3.grid(row=1,column=2,padx=1,pady=20)   
sel.trace('w',my_upd) # on change of string variable 
my_w.mainloop()  # Keep the window open