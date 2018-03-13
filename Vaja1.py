from tkinter import *
import math
class Risanje:
    def __init__(self,master):
        # ustvarimo platno
        self.platno=Canvas(master,width=500,height=500)
        self.platno.pack() #z pack umestiš na platno
        #piramida(self.platno,8,400,50,20)
        #tarca(self.platno,8,150,200,10)
        #trikotnik(self.platno,7,250,250,160)
        torta(self.platno,[30,15,20,35],250,250,100)

        menu = Menu(okno)
        menuNarisi = Menu(menu, tearoff=0)
        menuPobrisi = Menu(menu, tearoff=0)
        okno.config(menu=menu)
        menu.add_cascade(label='Narisi', menu=menuNarisi)
        menuNarisi.add_command(label = 'Piramida', command = self.piramida)

def piramida(platno, n, x, y, d):
    for i in range(n):
        platno.create_rectangle(x-(i+1)*d,y+i*d,x+(i+1)*d,y+(i-1)*d,fill="orange",outline="")


def tarca(platno,n,x,y,d):
    for i in range(n,0,-1):
        barva="white"if i%2== 0 else "black"
        platno.create_oval(x-i*d, y-i*d, x+i*d, y+i*d, fill=barva, outline="black")

def trikotnik(platno,n,x,y,d):
    if n==1:
        platno.create_polygon(x,y,x+d,y,x+d/2,y-d*math.sqrt(3)/2, fill="",outline="black")
    else:
        trikotnik(platno,n-1,x,y,d/2)
        trikotnik(platno,n-1,x+d/2,y,d/2)
        trikotnik(platno,n-1,x+d/4,y-d*math.sqrt(3)/4,d/2)


barve=["blue","red","black","orange"]
def torta(platno,podatki,x,y,r):
    zacetni=0
    for i in range(len(podatki)):
        koncni = podatki[i] / sum(podatki) * 360
        platno.create_arc(x+r,y+r,x-r,y-r,start=zacetni,extent=koncni,style=PIESLICE,fill=barve[i],outline="black")
        zacetni+=koncni
okno = Tk()
app = Risanje(okno)
okno.mainloop()

