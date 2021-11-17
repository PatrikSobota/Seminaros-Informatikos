import tkinter as tkk

root = tkk.Tk()
C = tkk.Canvas(bg="white", height=350, width=500)


C.create_rectangle(0,0,150,150,
    outline="red", fill="red", width=2)

C.create_rectangle(0,350,150, 200,
    outline="red", fill="red",)

C.create_rectangle(200,200,500, 500,
    outline="red", fill="red",)

C.create_rectangle(200,0,500, 150,
    outline="red", fill="red",)

C.pack()
root.mainloop()
