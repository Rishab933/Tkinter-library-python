from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("750x750")
root.title("Sliders")


def getdollar():
    msg = f"Request of {myslider1.get()} dollars creadited!"
    print(f"Request of {myslider1.get()} dollars creadited!")
    tmsg.showinfo("Amount Creadited!", msg)


# vertical sliders from 0-50            to set a specific interval
myslider = Scale(root, from_=0, to=100, tickinterval=50)
# for setting an initial value in the slider
myslider.set(50)
myslider.pack()

Label(root, text="how many dollars you want?").pack()
# horizontal sliders from 1-100
myslider1 = Scale(root, from_=1, to=100, orient="horizontal")
myslider1.pack()
Button(root, text="submit", command=getdollar).pack()

root.mainloop()
