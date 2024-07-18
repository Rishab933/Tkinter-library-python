from tkinter import *

root = Tk()
root.geometry("735x735")
root.title("Simple Menu")


def myfunc():
    print("working fine")


main_menu = Menu(root)
main_menu.add_command(label="file", command=myfunc)
main_menu.add_command(label="exit", command=quit)

root.config(menu=main_menu)

root.mainloop()

