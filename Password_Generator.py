from tkinter import *
from password_generator import PasswordGenerator

master = Tk()
master.title("Password Generator")
master.resizable(0,0)
password = PasswordGenerator()


password.minlen = 8
password.maxlen = 9
password.minuchars = 2
password.minlchars = 2
password.minnumbers = 2
password.minschars = 2

def create():
    result = password.generate()
    pw.insert(0, result)

def delete1():
    pw.delete(0,END)

label1 = Label(master, text = "Password Generator", font=("Helvetica", 15, "bold"))
pw = Entry(master)
Generate = Button(master, text = "Generate", command = create)
clear = Button(master, text="Clear", command = delete1)

label1.grid(row = 0, column = 0,  padx= 50)
pw.grid(row=1, column= 0,  padx= 50)
Generate.grid(row=2, column= 0, ipadx = 30, ipady = 15, padx= 50, pady =30 )
clear.grid(row=3, column= 0, ipadx = 35, ipady = 15, padx= 50)


master.mainloop()