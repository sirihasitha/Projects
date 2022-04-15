from tkinter import *
from PIL import Image, ImageTk
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

mainWindow = Tk()
mainWindow.minsize(800, 640)
mainWindow.title("Ludo Game")
mainWindow.config(bg = "light green")
#mainWindow.iconbitmap("Images/ludo_icon.ico")

Label(bg = "light green").pack(pady = 30)

LudoLogoImage = ImageTk.PhotoImage(Image.open("Images/Ludo_Logo.png").resize((250, 120), Image.ANTIALIAS))
LudoLogo = Label(image = LudoLogoImage, bg = "light green").pack(pady = 20)

currentVol = 0.5

mixer.init()
mixer.music.load("6-Happy-Commercial-Piano.mp3")
mixer.music.set_volume(currentVol)
mixer.music.play(-1)

def playGame():
    mainWindow.withdraw()
    import ludo_backup

def changeVol(vol):
    currentVol = float(vol) / 100
    mixer.music.set_volume(currentVol)

def menu():
    menuWindow = Toplevel()
    menuWindow.maxsize(400, 350)
    menuWindow.title("Options Menu")
    menuWindow.config(bg = "light green")
    #menuWindow.iconbitmap("Images/ludo_icon.ico")
    
    Label(menuWindow, image = menuTitle, bg = "light green").pack(pady = 20)
    Label(menuWindow, image = soundImage, bg = "light green").pack(padx = 10, pady = 8, anchor = W)

    soundSlider = Scale(menuWindow, from_ = 0, to = 100, orient = HORIZONTAL, bg = "light green", length = 300, sliderlength = 25, command = changeVol)
    soundSlider.pack(padx = 10, anchor = W)

    backButton = Button(menuWindow, image = backImage, bg = "#ff4040", height = 55, width = 110, command = menuWindow.destroy)
    backButton.pack(pady = 50)


playImage = ImageTk.PhotoImage(Image.open("Images/PlayButton.png").resize((78, 25), Image.ANTIALIAS))
menuImage = ImageTk.PhotoImage(Image.open("Images/MenuButton.png").resize((78, 23), Image.ANTIALIAS))
menuTitle = ImageTk.PhotoImage(Image.open("Images/MenuButton.png").resize((150, 45), Image.ANTIALIAS))
quitImage = ImageTk.PhotoImage(Image.open("Images/QuitButton.png").resize((70, 27), Image.ANTIALIAS))
soundImage = ImageTk.PhotoImage(Image.open("Images/Sound.png").resize((110, 26), Image.ANTIALIAS))
backImage = ImageTk.PhotoImage(Image.open("Images/BackButton.png").resize((80, 26), Image.ANTIALIAS))

playButton = Button(image = playImage, bg = "#ff8f17", height = 55, width = 110, command = playGame)
menuButton = Button(image = menuImage, bg = "#4287f5", height = 55, width = 110, command = menu)
quitButton = Button(image = quitImage, bg = "#ff4040", height = 55, width = 110, command = mainWindow.quit)

playButton.pack(pady = 8)
menuButton.pack(pady = 8)
quitButton.pack(pady = 8)

mainWindow.mainloop()
