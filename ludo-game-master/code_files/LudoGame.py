
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.maxsize(800, 640)
root.title("Ludo Game")
root.config(bg = "light green")
#root.wm_iconbitmap("ludo_icon.ico")

def Logo_Button():
    root.destroy()
    import opening_window

logoImage = ImageTk.PhotoImage(Image.open("Images/Ludo_Logo.png").resize((500, 245), Image.ANTIALIAS))

logoButton = Button(image = logoImage, bg = "light green", height = 800, width = 800, activebackground = "light green", command = Logo_Button)

logoButton.pack()

root.mainloop()

