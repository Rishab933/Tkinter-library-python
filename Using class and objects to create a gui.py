from tkinter import *


class GUI(Tk):  #GUI class is inherited from Tk class
    def __init__(self):  # constructor "root" is replaced with "self" here
        super().__init__()  # constructor of the super class Tk
        self.geometry("500x500")
        self.title("Using class and objects to create a GUI")

    def status(self):
        self.v = StringVar()
        self.v.set("Ready")
        self.sbar = Label(self, textvariable=self.v, relief=SUNKEN, anchor="w")
        self.sbar.pack(side=BOTTOM, fill=X)

    def submit(self):
        print("Button working")

    def button(self):
        self.b = Button(self, text="Upload", command=self.submit)
        self.b.pack()
        

if __name__ == '__main__':  # here "root" is replaced with "window"
    window = GUI()
    window.status()
    window.button()
    window.mainloop()
