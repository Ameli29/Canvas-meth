from tkinter import*


def exit_win(event): root.destroy()


def to_label(event):
    t = ent.get()
    lbl.configure(text=t)


def select_all(event):
    def select_all2(widget):
        widget.selection_range(0, END)
        widget.icursor(END)  # курсор в конец

    root.after(10, select_all2, event.widget)


root = Tk()


root.mainloop()