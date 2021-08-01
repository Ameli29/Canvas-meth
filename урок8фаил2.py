from tkinter import *

root = Tk()


def move(event):
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)
    root.title(s)


c = Canvas(root, width=400, height=400, bg='white')
c.pack()

a = c.create_polygon(200, 70, 80, 190, 320, 190, )
b = c.create_polygon(110, 330, 110, 190, 290, 190, 290, 330,)

sun = c.create_oval(260, 20, 350, 110, width=2, fill = 'yellow', outline='yellow',)


for i in range(20):
    grass = c.create_arc(10+i*20, 350, 100+i*20, 450,
                         start=180, extent=-50,
                         style=ARC, outline='green',
                         width=5)

c.move(a, 0, 50)
c.move(b, 0, 50)
# c.move(grass, 0, 300)
root.bind('<Motion>', move)

root.mainloop()