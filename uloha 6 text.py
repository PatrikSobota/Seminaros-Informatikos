import tkinter as tk

def text():
    y = open(file = "textak.txt")
    for i in range(12):
        x = y.readline()
        print(x)

okno = tk.Tk()



btn = tk.Button(okno, activebackground = "yellow", height = 15, width = 150, bg = "green", command = text)
btn.pack()

okno.mainloop()
