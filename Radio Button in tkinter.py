from tkinter import *
import tkinter.messagebox as tmsg


def order():
    tmsg.showinfo("Order Confirmation", f"Your Order for {var.get()} have been placed, kindly wait patiently!")


root = Tk()
root.geometry("750x750")
root.title("Radio Button")

var = IntVar()
# To set a initial value to the variable var
# var.set(1)

Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT, padx=14).pack()
# To give options only we use radio buttons
Radiobutton(root, text="Dosa", padx=14, variable=var, value=1).pack(anchor="w")
Radiobutton(root, text="Idly", padx=14, variable=var, value=2).pack(anchor="w")
Radiobutton(root, text="Pasta", padx=14, variable=var, value=3).pack(anchor="w")
Radiobutton(root, text="Kachori", padx=14, variable=var, value=4).pack(anchor="w")
Radiobutton(root, text="Maggie", padx=14, variable=var, value=5).pack(anchor="w")

Button(text="Order Now", command=order).pack()
# Now we will see how to retrieve the values


root.mainloop()
