from tkinter import *


def take():
    lab['text'] = "Выдано"

root = Tk()

Label(text="пункт выдачи",font="Arial 25").pack()
Button(text="взять",font="Arial 20",command=take).pack()

lab = Label(width=10, height=2, bd=25, font="Arial 25")
lab.pack()

root.mainloop()