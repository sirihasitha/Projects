from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

#update final winner : Red = 1, Blue = 2, Green = 3, Yellow = 4
winner = 1

length = 500
height = 200

window = Tk()
window.maxsize(800, 640)
window.title("Winner")
window.config(bg = "light green")
#window.iconbitmap("Images/ludo_icon.ico")

WinnerTitle = ImageTk.PhotoImage(Image.open("Images/Winner.png").resize((230, 50), Image.ANTIALIAS))
Label(window, image = WinnerTitle, bg = "light green").pack(pady = 20)

currentVol = 0.5

mixer.init()
mixer.music.load("Winner_Song.mp3")
mixer.music.set_volume(currentVol)
mixer.music.play()

players = ["Images/RedWinner.png", "Images/BlueWinner.png", "Images/GreenWinner.png", "Images/YellowWinner.png"]

if winner == 1:
    length = 515
elif winner == 2 or winner == 3:
    length = 600

def endGame():
    window.destroy()
    import opening_window

WinnerName = ImageTk.PhotoImage(Image.open(players[winner - 1]).resize((length, height), Image.ANTIALIAS))
Label(window, image = WinnerName, bg = "light green").pack(pady = 20)

endGameImage = ImageTk.PhotoImage(Image.open("Images/EndGameButton.png").resize((160, 25), Image.ANTIALIAS))
endGameButton = Button(window, image = endGameImage, bg = "#ff4040", height = 70, width = 180, command = endGame)
endGameButton.pack(pady = 50)

window.mainloop()
