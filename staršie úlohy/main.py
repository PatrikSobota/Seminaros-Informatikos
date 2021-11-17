import tkinter
import time

okno = tkinter.Tk()

platno = tkinter.Canvas (okno, width = 800, height = 400)
platno.pack()

mojtrojuholnik = platno.create_polygon (10,10,10,60,50,35)



for x in range (1,100):
    platno.move(1, 5, 0)
    #animovat utvar
    okno.update ()
    time.sleep(0.05)