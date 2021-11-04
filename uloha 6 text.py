import tkinter as tk

def text():
    y = open(file = "txt.txt")
    for i in range(12):
        x = y.readline()
        print(x)

okno = tk.Tk()



btn = tk.Button(okno, activebackground = "blue", height = 15, width = 150, bg = "cyan", command = text)
btn.pack()

okno.mainloop()