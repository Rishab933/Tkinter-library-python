from tkinter import *


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            try:
                value = eval(svalue.get())
            except Exception as e:
                svalue.set("Error")
                result.update()
                return
        svalue.set(value)
        result.update()
    elif text == "AC":
        svalue.set("")
        result.update()
    else:
        svalue.set(svalue.get() + text)
        result.update()


root = Tk()
root.title("Calculator 2")
root.geometry("570x580+100+200")
root.resizable(False, False)
root.configure(bg="Black")

svalue = StringVar()
svalue.set("")
result = Entry(root, textvariable=svalue, width=25, font="arial 30 bold")
result.pack(fill=Y, pady=10)

b = Button(root, text="AC", width=5, height=1, font="arial 30 bold", bd=1, bg="orange")
b.place(x=10, y=80)
b.bind("<Button-1>", click)

b = Button(root, text="%", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=150, y=80)
b.bind("<Button-1>", click)

b = Button(root, text="<x", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=290, y=80)
b.bind("<Button-1>", click)

b = Button(root, text="/", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=430, y=80)
b.bind("<Button-1>", click)

b = Button(root, text="7", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=10, y=180)
b.bind("<Button-1>", click)

b = Button(root, text="8", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=150, y=180)
b.bind("<Button-1>", click)

b = Button(root, text="9", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=290, y=180)
b.bind("<Button-1>", click)

b = Button(root, text="*", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=430, y=180)
b.bind("<Button-1>", click)

b = Button(root, text="4", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=10, y=280)
b.bind("<Button-1>", click)

b = Button(root, text="5", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=150, y=280)
b.bind("<Button-1>", click)

b = Button(root, text="6", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=290, y=280)
b.bind("<Button-1>", click)

b = Button(root, text="-", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=430, y=280)
b.bind("<Button-1>", click)

b = Button(root, text="1", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=10, y=380)
b.bind("<Button-1>", click)

b = Button(root, text="2", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=150, y=380)
b.bind("<Button-1>", click)

b = Button(root, text="3", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=290, y=380)
b.bind("<Button-1>", click)

b = Button(root, text="+", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=430, y=380)
b.bind("<Button-1>", click)

b = Button(root, text="00", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=10, y=480)
b.bind("<Button-1>", click)

b = Button(root, text="0", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=150, y=480)
b.bind("<Button-1>", click)

b = Button(root, text=".", width=5, height=1, font="arial 30 bold", bd=1, bg="grey")
b.place(x=290, y=480)
b.bind("<Button-1>", click)

b = Button(root, text="=", width=5, height=1, font="arial 30 bold", bd=1, bg="blue")
b.place(x=430, y=480)
b.bind("<Button-1>", click)

root.mainloop()

