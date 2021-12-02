import tkinter
import threading
import random
import time


def nacitaj_mapu(cesta):

    premenna = open(cesta)

    sirka = int(premenna.readline())

    vyska = int(premenna.readline())

    mapa=[]

    pac_found = True
    duch_found = False


    for y in range(0, vyska):
        line = premenna.readline()
        mapa.append(list(line))

    premenna.close()

        for y in range(0, ?????):
            # ak sme ich oboch nasli, tak vybehni z cyklu
            if ?????? and ?????:
                break;
            for x in range(0, ????????):
                # ak na sucasnom policku sa ma nachadzat postavicka...
                if mapa[y][x] == '?????':
                    # tak to prepiseme na volne policko a ulozime si poziciu a zmenime
                    # najdenie pacmana na True, aby sme vybehli z vonkajsieho cyklu von
                    mapa[y][x] = '???????? '
                    pac_x = x
                    pac_y = y
                    pac_found = ???????
                    # vkladame do sceny potvorku, zloducha
                    elif mapa[y][x] == '??????':
                    mapa[y][x] = ' '
                    duch_x = ?????
                    duch_y = ?????
                    duch_found = True

                if pac_found and duch_found:
                    break;

    return sirka, vyska, mapa, ???????, pac_y, duch_x, ????????



def vytvor_platno(okno, sirka, vyska, mapa, cell_size, stena):

    platno = tkinter.Canvas(okno,
                width= sirka * cell_size,
                height = vyska * cell_size)
    platno.config(bg='orange')
    platno.pack()

    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                platno.create_image(x * cell_size + stena / 2,
                            y * cell_size + stena / 2,
                            image='wall.gif')
    return platno


# pohyb panacika pomocou sipok
def pacmanmove(event):
    # musime mu zadat globalne premenne - definovali sme ich mimo tejto funkcie
    # , s ktorymi bude pracovat aj tato fcia
    global pac_x
    global pac_y
    global platno
    global pacman
    global cell_size
    global mapa
    global skore
    global gulicky
    global okno

    # pripravime si premenne pre poziciu pacmana po posunuti
    target_x = ???????
    ????????? = pac_y

    # podla stlacenej klavesy nastavime cielovu poziciu pacmana - 1 neznamena
    # pixel ale policko

    if event.keysym == 'Up':
        target_y -= ????
        elif event.keysym == 'Down':
        ?????? += 1
    elif event.keysym == 'Left':
        ???????? = 1
    elif event.keysym == 'Right':
        target_x += 1

    # ak je cielove policko prazdne, tak priradime nove suradnice
    # musime mysliet na to, ze berie do uvahy stred obrazku, aby
    # sme nevosli do steny
    if mapa[target_y][target_x] != '?????????':
        # zapamatame si nove suradnice pacmana
        ?????? = target_x
        pac_y = ?????????
        # posunieme obrazok
        platno.coords(pacman, \
                      target_x * cell_size + cell_size / 2, \
                      target_y * cell_size + cell_size / 2)

    global duch_x
    global duch_y


mapa = []

pac_x = 0
pac_y = 0

duch_x = 1
duch_y = 1

sirka = 20
vyska = 0

cell_size = 80


okno = tkinter.Tk()
okno.title('Patrikova hra')

sirka, vyska, mapa, pac_x, pac_y, duch_x, duch_y = nacitaj_mapu('textak.txt')


wall = tkinter.PhotoImage(file='wall.gif')


platno = (okno, sirka, vyska, mapa, cell_size, wall)

#nacitame data k obrazku a zobrazime ho na konkretnych suradniciach
pacman_data = tkinter.PhotoImage (file= 'pacman1.png')
pacman = platno.create_image (pac_x * cell_size + cell_size / 2, \
                              pac_y * cell_size + cell_size / 2, \
                              image=pacman_data)

duch_data = tkinter.PhotoImage (file= 'pacman2.png')
duch = platno.create_image (duch_x * cell_size + cell_size / 2, \
                            duch_y * cell_size + cell_size / 2, \
                            image=duch_data)
duch_smer = 3
terminate = False

platno.bind_all ('<KeyPress-Up>', pacmanmove)
platno.bind_all ('<KeyPress-Down>', pacmanmove)
platno.bind_all ('<KeyPress-Left>', pacmanmove)
platno.bind_all ('<KeyPress-Right>', pacmanmove)
platno.bind_all ('<KeyPress-Escape>', lambda key: okno.destroy())

duch_timer.start()


okno.mainloop()
terminate = True