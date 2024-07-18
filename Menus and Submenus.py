from tkinter import *


def new_project():
    print("New project is been created")


def save():
    print("project is been saved")


def save_as():
    print("project is been saved as: xyz")


def xyz():
    print("pass")


root = Tk()
root.geometry("735x735")
root.title("Menus & Submenus")

main_menu = Menu(root)

m1 = Menu(main_menu)
m1.add_command(label="New Project", command=new_project)
m1.add_command(label="Save", command=save)
m1.add_command(label="Save as", command=save_as)
m1.add_separator()
m1.add_command(label="Quit", command=quit)

main_menu.add_cascade(label="Project", menu=m1)

m2 = Menu(main_menu,tearoff=0)
m2.add_command(label="cut", command=xyz)
m2.add_command(label="copy", command=xyz)
m2.add_command(label="paste", command=xyz)

main_menu.add_cascade(label="Edit", menu=m2)
root.config(menu=main_menu)


root.mainloop()
