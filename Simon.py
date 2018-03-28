#---IMPORT---#
import Tkinter 
from tkMessageBox import askyesno
import time, random, sys 

#---MAIN---#

canvasWidth = 702
canvasHeight = 702
root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, width = canvasWidth, height = canvasHeight)
canvas.pack()

red = canvas.create_rectangle(2, 2, 354, 354, fill="dark red")
blue = canvas.create_rectangle(2, 358, 354, 704, fill="dark blue")
yellow = canvas.create_rectangle(358, 2, 704, 354, fill="#cccc00")
green = canvas.create_rectangle(358, 358, 704, 704, fill="dark green")

colourList = []
colours = ["red", "blue", "yellow", "green"]
clickedList = []

#---FUNCTIONS---#

def flash():
    global colourList, colours
    colourList.append(str(random(colours)))

def unnamed(*args):
    global clickedList, colourList
    print 'redis clicked'
    clickedList.append("red")
    if clickedList(len(clickedList)) != colourList(len(clickedList)):
        game_over_message()

def main_loop():
    #flash()
    root.after(20, main_loop)

###########

canvas.tag_bind(red, "<Button-1>", unnamed)

main_loop()
root.mainloop()
