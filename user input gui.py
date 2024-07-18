from tkinter import *


def apply():
    width = int(width_entry.get())
    height = int(height_entry.get())
    root.geometry(f"{width}x{height}")


root = Tk()
root.title("User Input GUI")

x = Label(root, text="User Input GUI", fg="black", padx=20, pady=20, font=("Arial", 24, "bold"))
x.grid(row=0, column=0, columnspan=7, pady=20)

a = Label(root, text="Enter width of GUI", font=("Arial", 12))
b = Label(root, text="Enter height of GUI", font=("Arial", 12))
a.grid(row=1, column=0, padx=50, pady=10, sticky=W)
b.grid(row=2, column=0, padx=50, pady=10, sticky=W)

width_value = IntVar()
height_value = IntVar()

width_entry = Entry(root, textvariable=width_value)
height_entry = Entry(root, textvariable=height_value)

width_entry.grid(row=1, column=1, padx=20, pady=10)
height_entry.grid(row=2, column=1, padx=20, pady=10)

submit_button = Button(root, text="Submit", command=apply)
submit_button.grid(row=3, column=0, columnspan=2, padx=50, pady=20)

root.mainloop()
