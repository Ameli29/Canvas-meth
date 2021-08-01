from tkinter import *


def changeFont(font):
    label['font'] = font


root = Tk()
label = Label(text="Hello Wold")
label.pack()

b1 = Button(command=lambda f="Verdana": changeFont(f))
b1.pack()

b2 = Button(command=lambda f="Times": changeFont(f))
b2.pack()

root.mainloop()