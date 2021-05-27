from tkinter import *
from random import randint
root=Tk()
root.title("Password classifier")

def classify():
    pass_len=len(textbox.get())
    
    if(pass_len>7) and (".","?","_","$","@" in textbox.get()):
        textbox1=Entry(root,text="Strong",font=("Calibri",24))
        textbox1.pack(pady=20,padx=20)
        t="Strong"
        textbox1.insert(0,t)
    else:
        textbox1=Entry(root,text="Weak",font=("Calibri",24))
        textbox1.pack(pady=20,padx=20)
        w="Weak"
        textbox1.insert(0,w)
    textbox.delete(0,END)

my_password=chr(randint(33,126))
lf=LabelFrame(root,text="Enter your text here")
lf.pack(pady=20)
textbox=Entry(lf,font=("Calibri",24))
textbox.pack(pady=20,padx=20)
my_frame=Frame(root)
my_frame.pack(pady=20)
my_button=Button(my_frame,text="Ok",command=classify)
my_button2=Button(my_frame,text="Cancel",command=classify)
my_button.grid(row=0,column=0,padx=10)
my_button2.grid(row=0,column=1,padx=20)

