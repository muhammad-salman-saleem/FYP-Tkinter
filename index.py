import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Prize Bond Checker")
root.geometry("900x450+300+100")
# heading = Label(text="Prize Bond Checker", bg="black", fg="white",height="2", width="30",font="20")
# heading.pack()
root.resizable(False,False)
root.configure(bg="#305065")

# icon
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

# top Frame
Top_frame=Frame(root,bg="white",width="900",height="80")
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file="logo2.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)
Label(Top_frame,text="Prize Bond Checker",font="arial 25 bold",bg="white",fg="black").place(x=70,y=10)


# text frame
Text_frame=Frame(root,bg="lightgray",width="550",height="320")
Text_frame.place(x=17,y=100)

# def Select_Bond_Price(choice):
#     choice = variable.get()
#     dropdown.config(width=choice)
 # Bond prize box
Label(Text_frame,text="Select Bond Prize",font="arial 12 bold",bg="lightgray",fg="black").place(x=20,y=40)
font1=('Times',18,'normal')
sel=tk.StringVar()
my_opts=['100','200','300','500','1000','1500'] # options
cb1 = ttk.Combobox(Text_frame, values=my_opts,width=25,
        textvariable=sel,font=font1) # Combobox
cb1.grid(row=0,column=0,padx=10,pady=20,columnspan=3) # adding to grid
cb1.place(x=200,y=40)
def bond_price():
        if my_opts is 100:
                pass



"""
# Date option
Label(Text_frame,text="Select Date",font="arial 12 bold",bg="lightgray",fg="black").place(x=20,y=70)
font1=('Times',18,'normal')
sel=tk.StringVar()
my_opts=[] # options
cb2 = ttk.Combobox(Text_frame, values=my_opts,width=25,
        textvariable=sel,font=font1) # Combobox
cb2.grid(row=0,column=0,padx=10,pady=20,columnspan=3) # adding to grid
cb2.place(x=200,y=70)


"""
# Bond number
Label(Text_frame,text="Enter Bond Number",font="arial 12 bold",bg="lightgray",fg="black").place(x=20,y=110)
inputtxt = Text(Text_frame, height = 1, width = 26, bg = "white",font=font1).place(x=200,y=110)



# Button Brouser
Label(Text_frame,text="Picture (Optional)",font="arial 12 bold",bg="lightgray",fg="black").place(x=20,y=189)
button = tk.Button(Text_frame,bg = "black",fg="White", text='Uplod Pitcure', width="24",font=font1,).place(x=200,y=180)
# button = tk.Button(Text_frame,bg = "white",fg="black", text='Submit', width="8",font=font1,).place(x=400,y=180)



#Button Search
button = tk.Button(Text_frame,bg = "green",fg="black", text='Search', width="38",font=font1,).place(x=20,y=250)
# result Frame
Result_frame=Frame(root,bg="white",width="300",height="320")
Result_frame.place(x=585,y=100)
Label(Result_frame,text="Bond Result",font="arial 18 bold",fg="black").place(x=80,y=15)








# Coppy Right Frame
Result_frame=Frame(root,bg="black",width="900",height="20")
Result_frame.place(x=0,y=430)
Label(Result_frame,text="@ Copyright by graphictech",font="arial 8 bold",bg="black",fg="white").place(x=400,y=1)
root.mainloop()
