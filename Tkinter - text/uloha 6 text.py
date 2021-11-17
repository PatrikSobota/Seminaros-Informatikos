import tkinter as tk

def text():
    y = open(file = "textak-1.txt")
    for i in range(12):
        x = y.readline()
        print(x)
okno = tk.Tk()
btn = tk.Button(okno, activebackground = "yellow", height = 15, width = 150, bg = "green", command = text)
btn.pack()
okno.mainloop()