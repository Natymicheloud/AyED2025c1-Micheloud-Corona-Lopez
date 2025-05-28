# -*- coding: utf-8 -*-

class MonticuloBinario: 
    def __init__(self):
        self.listamonticulo = [0] #se inicializa la lista con un elemento 0 para facilitar el manejo de índices
        self.tamañoactual = 0 #se inicializa el tamaño actual del montículo en 0

    def InfiltrarArriba(self, i): #ajusta la estructura del monticulo luego de insertar un nuevo elemento
        while i//2 > 0: #i//2 nos da el padre del nodo actual, si el elemento es menor que su padre, se intercambian
            if self.listamonticulo[i] < self.listamonticulo[i//2]: #si el elemento actual es menor que su padre
                temporal = self.listamonticulo[i//2] #se guarda el padre en una variable temporal 
                self.listamonticulo[i//2] = self.listamonticulo[i] #el padre toma el valor del hijo
                self.listamonticulo[i] = temporal #el hijo toma el valor del padre
            i = i//2 #se actualiza i para seguir subiendo en el montículo

    def Insertar(self, dato): #inserta un nuevo elemento en el montículo
        self.listamonticulo.append(dato) #se agrega el nuevo dato al final de la lista
        self.tamañoactual = self.tamañoactual + 1 #se incrementa el tamaño actual del montículo
        self.InfiltrarArriba(self.tamañoactual) #se llama a la función para ajustar la estructura del montículo

    def InfiltrarAbajo(self, i): #ajusta la estructura del montículo luego de eliminar el elemento mínimo
        while (i*2) <= self.tamañoactual: #i*2 nos da el primer hijo (hijo izquierdo) del nodo actual, se verifica si tiene hijos
            hijomin = self.hijoMin(i) #se obtiene el índice del hijo menor entre el hijo izquierdo y derecho
            if self.listamonticulo[i] > self.listamonticulo[hijomin]: #si el elemento actual es mayor que su hijo menor
                temporal = self.listamonticulo[i] #se guarda el valor del nodo actual en una variable temporal
                self.listamonticulo[i] = self.listamonticulo[hijomin] #el nodo actual toma el valor de su hijo menor
                self.listamonticulo[hijomin] = temporal #el hijo menor toma el valor del nodo actual
                i = hijomin #se actualiza i para seguir bajando en el montículo
            else:
                break #si el nodo actual no es mayor que su hijo menor, se sale del bucle
     
    def hijoMin(self, i): #determina cuál de los hijos del nodo actual es el menor
        if (i*2)+1 > self.tamañoactual: 
            return i*2 #si solo hay un hijo (hijo izquierdo), se retorna su índice
        else: #si hay dos hijos (hijo izquierdo y derecho)
            if self.listamonticulo[i*2] < self.listamonticulo[(i*2)+1]: #se compara el valor de los hijos
                return i*2 #si el hijo izquierdo es menor, se retorna su índice
            else:
                return (i*2)+1 #si el hijo derecho es menor o igual, se retorna su índice
            
    def eliminarMin(self): #elimina el elemento mínimo del montículo (la raíz)
        eliminado = self.listamonticulo[1] #se guarda el valor del elemento mínimo (raíz) para retornarlo después
        self.listamonticulo[1] = self.listamonticulo[self.tamañoactual] #se reemplaza la raíz con el último elemento del montículo
        self.tamañoactual = self.tamañoactual - 1 #se decrementa el tamaño actual del montículo
        self.listamonticulo.pop() #se elimina el último elemento (ahora duplicado) de la lista
        self.InfiltrarAbajo(1) #se llama a la función para ajustar la estructura del montículo
        return eliminado #devuelve el valor del elemento mínimo eliminado
    
    def ConstruirMonticulo(self, lista): #construye un montículo a partir de una lista de elementos
        i = len(lista) // 2 #len(lista)//2 nos determina el primer nodo no hoja (primer nodo que tiene hijos)
        self.tamañoactual = len(lista) #se establece el tamaño actual del montículo al tamaño de la lista
        self.listamonticulo = [0] + lista[:] #se inicializa la lista del montículo con un 0 y los elementos de la lista proporcionada
        while i>0: #se itera desde el primer nodo no hoja hasta la raíz
            self.InfiltrarAbajo(i) #se ajusta la estructura del montículo para cada nodo
            i = i - 1 #se decrementa i para pasar al nodo anterior