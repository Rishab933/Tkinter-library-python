from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("750x750")
root.title("Accepting the rating in a data file")
a = Label(root, text="Moms Kitchen", font=("Arial", 24, "bold"), pady=10)
a.pack()
b = Label(root, text="Please Rate us ", font=("Arial", 14, "bold"), pady=10)
b.pack()

def getdollar():
    file = open("data.txt", "a")
    msg = f"The rating that the user gave is {food.get()}"
    print(f"The rating that the user gave is {food.get()}")
    tmsg.showinfo("Moms Kitchen Rating Page", "Thank You Visit Again!")
    file.write(msg + "\n")

    file.close()



Label(root, text="Please rate our food between 0 to 10", pady=10).pack()
food = Scale(root, from_=1, to=10, orient="horizontal",length=300, tickinterval=1)
food.pack()
Button(root, text="submit", command=getdollar, pady=2).pack()

root.mainloop()
