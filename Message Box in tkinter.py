from tkinter import *
import tkinter.messagebox as tmsg


def new_project():
    print("New project is been created")


def save():
    print("project is been saved")


def save_as():
    print("project is been saved as: xyz")


def xyz():
    print("pass")


def help():
    print("I will help you out")
    a = tmsg.showinfo("help", "I will help you with this gui")


def rate():
    print("Rate us")
    a = tmsg.askquestion("What was your experience?", "Was your experience good?")
    print(a)
    if a == "yes":
        msg = "great!!"
    else:
        msg = "we will reach you out soon"

    tmsg.showinfo("Experience", msg)


root = Tk()
root.geometry("735x735")
root.title("Message Box")

main_menu = Menu(root)

m1 = Menu(main_menu)
m1.add_command(label="New Project", command=new_project)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save as", command=save_as)
m1.add_separator()
m1.add_command(label="Quit", command=quit)

main_menu.add_cascade(label="Project", menu=m1)

m2 = Menu(main_menu, tearoff=0)
m2.add_command(label="cut", command=xyz)
m2.add_command(label="copy", command=xyz)
m2.add_command(label="paste", command=xyz)

main_menu.add_cascade(label="Edit", menu=m2)
root.config(menu=main_menu)

m3 = Menu(main_menu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate", command=rate)
main_menu.add_cascade(label="Help", menu=m3)
root.config(menu=main_menu)

root.mainloop()
