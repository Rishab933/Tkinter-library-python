from tkinter import *


root = Tk()
root.geometry("350x350")
root.title("Scroll Bar")

scrollbar_y = Scrollbar(root)
scrollbar_y.pack(side=RIGHT, fill=Y)

scrollbar_x = Scrollbar(root)
scrollbar_x.pack(side=BOTTOM, fill=X)

lb = Listbox(root, yscrollcommand = scrollbar_y.set)
for i in range(300):
    lb.insert(END, f"Item {i}")

lb.pack()
scrollbar_y.config(command=lb.yview)
scrollbar_x.config(command=lb.xview)

root.mainloop()

