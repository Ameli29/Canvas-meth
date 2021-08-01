from tkinter import *


def red_label():label['bg'] = 'red'

def green_label():label['bg'] = 'green'

def blue_label():label['bg'] = 'blue'

def change():
    label['bg'] = var.get()

root = Tk()

var = StringVar()
var.set('red')
Radiobutton(text="Red", command=change, variable=var, value='red').pack()
Radiobutton(text="Green", command=change, variable=var, value='green').pack()
Radiobutton(text="Blue", command=change, variable=var, value='blue').pack()

label = Label(width=20, height=10, bg='red')
label.pack()

root.mainloop()