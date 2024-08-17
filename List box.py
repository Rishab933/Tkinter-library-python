from tkinter import *


def add():
    global i
    lb.insert(ACTIVE, f"{i}")
    i = i + 1


i = 0

root = Tk()
root.geometry("750x750")
root.title("List Box")

lb = Listbox(root)
lb.pack()
lb.insert(END, "First item")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
