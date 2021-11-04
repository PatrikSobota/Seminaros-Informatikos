import tkinter as tk


def moveimage(x):
    if x.keysym == "Down":
        window.move(img, 0, 30)
        window.itemconfig(img, image = pacman1)
        window.update()
        window.after(150)
        window.itemconfig(img, image = pacman2)
        window.update()

    elif x.keysym == "Up":
        window.move(img, 0, -30)
        window.itemconfig(img, image=pacman1)
        window.update()
        window.after(150)
        window.itemconfig(img, image = pacman2)
        window.update()

    elif x.keysym == "Left":
        window.move(img,-30,0)
        window.itemconfig(img, image=pacman1)
        window.update()
        window.after(150)
        window.itemconfig(img, image=pacman2)
        window.update()

    elif x.keysym =="Right":
        window.move(img,30,0)
        window.itemconfig(img, image=pacman1)
        window.update()
        window.after(150)
        window.itemconfig(img, image=pacman2)
        window.update()

pole = tk.Tk()
window = tk.Canvas(pole, width = 1000, height = 500)
window.pack()
pacman1 = tk.PhotoImage(file = "pacman1.png")
pacman2 = tk.PhotoImage(file = "pacman2.png")
img = window.create_image(100,100, image= pacman1)

window.bind_all("<KeyPress-Right>", moveimage)
window.bind_all("<KeyPress-Left>", moveimage)
window.bind_all("<KeyPress-Up>", moveimage)
window.bind_all("<KeyPress-Down>", moveimage)

window.mainloop()
