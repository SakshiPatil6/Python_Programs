from tkinter import *  
parent = Tk() 
parent.title("Registration Form") 
parent.geometry("350x400")

Title = Label(parent,text = "Registration Form").place(x=110,y=30) 

name = Label(parent,text = "Name").place(x=50,y=80) 
e1 = Entry(parent).place(x=140,y=80)

email = Label(parent,text = "Email").place(x=50,y=120) 
e2 = Entry(parent).place(x=140,y=120)

Mobile = Label(parent,text = "number").place(x=50,y=160) 
e3 = Entry(parent).place(x=140,y=160)

Gender = Label(parent,text = "Gender").place(x=50,y=200) 
e3 = Entry(parent).place(x=140,y=200)

password = Label(parent,text = "Password").place(x=50,y=240) 
e4 = Entry(parent).place(x=140,y=240) 

submit = Button(parent, text = "Submit").place(x=130,y=290)   
parent.mainloop()  