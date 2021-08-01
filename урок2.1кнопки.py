from tkinter import *

def chande():
    b1['text'] = "Изменено"
    b1['bg'] = 'purple'
    b1['activebackground'] = '#555555'
    b1['fg'] = '#ffffff'
    b1['activeforeground'] = '#ffffff'

root = Tk()
b1 = Button(text="Изменить",
            width=15, height=3)
b1.config(command=chande)
b1.pack()
root.mainloop()