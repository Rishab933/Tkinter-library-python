from tkinter import *


def upload():
    s.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    s.set("Ready Now")


root = Tk()
root.geometry("350x350")
root.title("Status Bar")

s = StringVar()
s.set("Ready")
sbar = Label(root, textvariable=s, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()

root.mainloop()
can_widget = Canvas(root, width=800, height=800, bg="#1A2C38", borderwidth=0, highlightthickness=0)
can_widget.pack(padx=20, pady=15)
can_widget.create_rectangle(0, 0, 200, 476, outline="")
b = can_widget.create_rectangle(0, 476, 759, 518, fill="#0F212E", outline="")
c = can_widget.create_rectangle(200, 0, 759, 472, fill="#0F212E", outline="")