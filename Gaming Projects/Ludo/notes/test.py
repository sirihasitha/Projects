from tkinter import *

root = Tk()

can_widget = Canvas(root, bg = "blue", width = 500, height = 500)
can_widget.pack()

#moving the icon
circle = can_widget.create_oval(100,100,120,120,fill="red")
circle = can_widget.create_text(110,110, fill = "1")




def left(event):
    x = -200//6
    y=0
    can_widget.move(circle,x,y)

def right(event):
    x = 200//6
    y = 0
    can_widget.move(circle,x,y)

def up(event):
    x = 0
    y = -200//6
    can_widget.move(circle,x,y)

def down(event):
    x = 0
    y = 200//6
    can_widget.move(circle,x,y)
root.bind("<Left>",left)
root.bind("<Right>",right)
root.bind("<Up>",up)
root.bind("<Down>",down)

root.mainloop()
