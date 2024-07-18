from tkinter import *
from tkinter import StringVar
from typing import TextIO


def sub():
    file = open("data.txt", "a")
    file.write(user_name.get() + "\n")
    file.write(user_age.get() + "\n")
    file.write(user_contact.get() + "\n\n")

    file.close()


root = Tk()

root.geometry("750x750")
root.minsize(500, 500)
root.maxsize(1000, 1000)
root.title("Dance Competition Registration Form")
x = Label(text="XYZ Dance School", fg="black", padx=20, pady=15, font=("Arial", 24, "bold"))
x.grid(row=0, column=10, columnspan=2, pady=20)

a = Label(root, text="Name", padx=10, pady=10, font=20)
b = Label(root, text="Age", padx=10, pady=10, font=20)
c = Label(root, text="contact number", padx=10, pady=10, font=20)
a.grid()
b.grid()
c.grid()

user_name: StringVar = StringVar()
user_age = StringVar()
user_contact = StringVar()

x = Entry(root, textvariable=user_name)
y = Entry(root, textvariable=user_age)
z = Entry(root, textvariable=user_contact)

x.grid(row=1, column=1)
y.grid(row=2, column=1)
z.grid(row=3, column=1)

Button(text="SUBMIT", command=sub).grid(row=4, column=10)

root.mainloop()
