from tkinter import *
import matplotlib


class Bod:
    def __init__(self, sX, sY):
        self.soX = sX
        self.soY = sY

        self.souradnice = [self.sX, self.sY]



class Vektor:
    def __init__(self, bodA, bodB):
        self.slA = bodA[0] - bodB[0]
        self.slB = bodA[1] - bodB[1]

        self.slozky = [self.slA, self.slB]



class Primka:
    def __init__(self, bod, sVektor):
        self.bod = bod
        self.sVektor = sVektor

        self.nVektorA = [-sVektor[1], sVektor[0]]
        self.nVektorB = [sVektor[1], -sVektor[0]]

        self.paramR = "X = " + 


