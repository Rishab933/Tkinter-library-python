from tkinter import *


root = Tk()
root.geometry("750x750")
root.title("Scroll Bar")

# for connecting a scroll bar to a widget
# 1 widget (yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(300):
    lb.insert(END, f"Item {i}")

lb.pack()
scrollbar.config(command=lb.yview)

root.mainloop()

