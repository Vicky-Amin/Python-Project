#from tkinter import *
from Vaccination_logic import *
from tkinter import ttk


lbl_1= tkinter.Label(screen,text="Vaccination Report",font=("arial",15,"bold",),bg="white",fg="purple")
lbl_1.place(x=350,y=30)

lbl_2= tkinter.Label(screen,text="First Name: ",font=("arial",12,"bold",),bg="white",fg="purple")
lbl_2.place(x=25,y=100)

box_first = tkinter.Entry(screen,width=50,bd=5,textvariable=box_first)
box_first.place(x=300,y=100)

lbl_3= tkinter.Label(screen,text="Last Name: ",font=("arial",12,"bold",),bg="white",fg="purple")
lbl_3.place(x=25,y=150)

box_last = tkinter.Entry(screen,width=50,bd=5,textvariable=box_last)
box_last.place(x=300,y=150)

lbl_4= tkinter.Label(screen,text="Email: ",font=("arial",12,"bold",),bg="white",fg="purple")
lbl_4.place(x=25,y=200)

e_email = tkinter.Entry(screen,width=50,bd=5,textvariable=e_email)
e_email.place(x=300,y=200)

lbl_5= tkinter.Label(screen,text="Number: ",font=("arial",12,"bold",),bg="white",fg="purple")
lbl_5.place(x=25,y=250)

box_number = tkinter.Entry(screen,width=50,bd=5,textvariable=box_number)
box_number.place(x=300,y=250)

lbl_6= tkinter.Label(screen,text="Vaccination Doze: ",font=("arial",12,"bold",),bg="white",fg="purple")
lbl_6.place(x=25,y=300)

#just text box
#box_vacc = tkinter.Entry(screen,width=50,bd=5,textvariable=box_vacc)
#box_vacc.place(x=300,y=500)


box_vacc = ttk.Combobox(screen,width=50,textvariable=box_vacc)
box_vacc["state"] = "readonly"
box_vacc["values"] = ("1st Dose",
                    "2nd Dose")
box_vacc.place(x=300,y=300)

btn_submit = tkinter.Button(screen,text="Submit",font=("arial",20,"bold"),bg="white",fg="purple",bd=5,width=10,command= submit)
btn_submit.place(x=300,y=400)


screen.mainloop()