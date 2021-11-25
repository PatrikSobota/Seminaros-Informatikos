import tkinter
import threading
import random
import time
######################################################


def nacitaj_mapu():
    # vytvorime cestu k suboru, ktory budeme pouzivat
    premenna = open('textak-1.txt')
    # z prveho riadku v subore nacitame sirku

    sirka = int(premenna.readline())
    # z druheho riadku v subore nacitame vysku

    vyska = 10
    # vytvorime premennu mapa, ktora je zoznam - list
    mapa = []

    # pre kazdy riadok mapy precitaj kazdy riadok a vytvor z nich zoznam (rozsah je po vysku)
    for y in range(0, 11):

        line = premenna.readline()
        mapa.append(list(line))

# uzavri subor
    premenna.close()

# tieto hodnoty nam vrati z funkcie
    return sirka, vyska, mapa
######################################################

def vytvor_platno(okno, sirka, vyska, mapa, cell_size, stena):

    platno = tkinter.Canvas(okno,
                            width= sirka*cell_size,
                                          height = vyska *cell_size)
    platno.config(bg='orange')
    platno.pack()

    # ak je polozka v poli rovna #, tak vytvor obrazok pre stenu (rozsah je po vysku, resp sirku)
    for y in range(0, vyska):
        for x in range(0, sirka):
            if mapa[y][x] == '#':
                platno.create_image(x * cell_size + stena/ 2,
                                                             y * cell_size + stena / 2,
                                                                                      image = 'wall.gif')
            # vrati nakreslene platno
            return platno

        ######################################################
        # mapa - steny a prechody (1. index - vyska, 2. index sirka)
        mapa = []

        # rozmery mapy
        sirka = 20
        vyska = 0

        # rozmer policka (px)
        cell_size = 80
        ######################################################
        okno = tkinter.Tk()
        okno.title('Patrikova hra')

        # nacitaj zo suboru mapu a vratene hodnoty uloz do premennych.
        # vsetky nazvy premennych sesdia s lokalnymi premennymi, ale nie su to totozne
        # premenne.

        sirka, vyska, mapa = nacitaj_mapu('textak-1.txt')

        # obrazok si musime odlozit v premennej, ktora prezije platno a preto je globalna
        stena = tkinter.PhotoImage(file='wall.gif')

        # volame funkciu vytvor_platno tak, ze ju priradime do premennej. v zatvorke musia byt nazvy vsetkych premennych, ktore potrebuje na inicializaciu
        platno = (okno, sirka, vyska, mapa, cell_size, stena)

        okno.mainloop()
        terminate = True
