from tkinter import *


def click(event):
    global svalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "ERROR"

        svalue.set(value)
        screen.update()

    elif text == "AC":
        svalue.set("")
        screen.update()

    elif text == "<x":
        s = svalue.get()
        n = s[:-1]
        #print(n)
        svalue.set(n)
        screen.update()

    else:
        svalue.set(svalue.get() + text)
        screen.update()


root = Tk()
root.geometry("570x600+100+200")
root.resizable(False,False)
root.title("Calculator")
root.config(bg="black")

fr = Frame(root, bg="grey", padx=10, pady=10)

svalue = StringVar()
svalue.set("")
screen = Entry(root, textvariable=svalue, font="lucida 40 bold")
screen.pack(fill=X, padx=25.5, pady=10)

f = Frame(fr, bg="grey")

b = Button(f, text="AC", padx=27, pady=25.5, font="lucida 15 bold")
b.pack(side=LEFT, padx=17, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=21, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=15, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="<x", padx=24, pady=18, font="lucida 18 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=28.5, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(fr, bg="grey")

b = Button(f, text="7", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(fr, bg="grey")

b = Button(f, text="4", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(fr, bg="grey")

b = Button(f, text="1", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

f = Frame(fr, bg="grey")

b = Button(f, text="00", padx=24, pady=18, font="lucida 18 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=28, pady=18, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

f.pack()

fr.pack()

root.mainloop()
