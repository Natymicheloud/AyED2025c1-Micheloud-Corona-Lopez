# -*- coding: utf-8 -*-

class MonticuloBinario:
    def __init__(self):
        self.listamonticulo = [0]
        self.tamañoactual = 0

    def InfiltrarArriba(self, i):
        while i//2 > 0:
            if self.listamonticulo[i] < self.listamonticulo[i//2]:
                temporal = self.listamonticulo[i//2]
                self.listamonticulo[i//2] = self.listamonticulo[i]
                self.listamonticulo[i] = temporal
            i = i//2

    def Insertar(self, dato):
        self.listamonticulo.append(dato)
        self.tamañoactual = self.tamañoactual + 1
        self.InfiltrarArriba(self.tamañoactual)

    def InfiltrarAbajo(self, i):
        while (i*2) <= self.tamañoactual:
            hijomin = self.hijoMin(i)
            if self.listamonticulo[i] > self.listamonticulo[hijomin]:
                temporal = self.listamonticulo[i]
                self.listamonticulo[i] = self.listamonticulo[hijomin]
                self.listamonticulo[hijomin] = temporal
        i = hijomin
     
    def hijoMin(self, i):
        if (i*2)+1 > self.tamañoactual:
            return i*2
        else:
            if self.listamonticulo[i*2] < self.listamonticulo[(i*2)+1]:
                return i*2
            else:
                return (i*2)+1
            
    def eliminarMin(self):
        eliminado = self.listamonticulo[1]
        self.listamonticulo[1] = self.listamonticulo[self.tamañoactual]
        self.tamañoactual = self.tamañoactual - 1
        self.listamonticulo.pop()
        self.InfiltrarAbajo(1)
        return eliminado
    
    def ConstruirMonticulo(self, lista):
        i = len(lista) // 2
        self.tamañoactual = len(lista)
        self.listamonticulo = [0] + lista[:]
        while i>0:
            self.InfiltrarAbajo(i)
            i = i - 1