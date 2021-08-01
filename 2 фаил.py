from tkinter import *

def plus(e):
    text1 = ent1.get()
    text2 = ent2.get()
    otvet = int(text1) + int(text2)
    lab.config(text=otvet)

def ymnogit(e):
    text1 = ent1.get()
    text2 = ent2.get()
    otvet = int(text1) * int(text2)
    lab.config(text=otvet)


def delit(e):
    text1 = ent1.get()
    text2 = ent2.get()
    otvet = int(text1) / int(text2)
    lab.config(text=otvet)


def minus(e):
    text1 = ent1.get()
    text2 = ent2.get()
    otvet = int(text1) - int(text2)
    lab.config(text=otvet)


root = Tk()

ent1 = Entry (width=20)
ent2 = Entry (width=20)
but1 = Button(text='+', width=16)
but2 = Button(text='-', width=16)
but3 = Button(text='*', width=16)
but4 = Button(text='/', width=16)

lab = Label(width=20, )

but1.bind('<Button-1>', plus)
but2.bind('<Button-1>', minus)
but3.bind('<Button-1>', ymnogit)
but4.bind('<Button-1>', delit)


ent1.pack()
ent2.pack()
but1.pack()
but2.pack()
but3.pack()
but4.pack()



lab.pack()
root.mainloop()

