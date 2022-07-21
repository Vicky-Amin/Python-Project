import tkinter

screen = tkinter.Tk()
screen.title("Vaccination")
screen.iconbitmap("vaccine.ico")
screen.config(background="purple")
screen.geometry("900x600")

 
box_first = tkinter.StringVar()
box_last = tkinter.StringVar()
e_email = tkinter.StringVar()
box_number = tkinter.IntVar()
box_vacc = tkinter.StringVar()


def submit():
    first = box_first.get()
    last = box_last.get()
    email = e_email.get()
    num = box_number.get()
    vacc = box_vacc.get()
    
    print(first)
    print(last)
    print(email)
    print(num)
    print(vacc)