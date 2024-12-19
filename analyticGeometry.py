from tkinter import *
import matplotlib
import math

class Bod:
    def __init__(self, soX, soY):
        self.soX = soX
        self.soY = soY

        self.souradnice = [self.soX, self.soY]

class Vektor:
    def __init__(self, bodA, bodB):
        self.slozky = [(bodA.souradnice[0])-(bodB.souradnice[0]), (bodA.souradnice[1])-(bodB.souradnice[1])]

class Primka:
    def __init__(self, bod, sVektor):
        self.bod = bod
        self.sVektor = sVektor

        self.nVektor = self.sVektor
        self.nVektor.slozky = self.nVektor.slozky.reverse()
        #self.nVektor.slozky[0] = (-1) * self.nVektor.slozky[0]


bod1 = Bod(4,8)
bod2 = Bod(9,3)

vektor = Vektor(bod1, bod2)


primka = Primka(bod1, vektor)
print(bod2.souradnice[0])
print(vektor.slozky)
#print(primka.bod)
#print(primka.nVektor.slozky[0])
