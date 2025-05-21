class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self, iterable = None):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0
        self.__iterador = None

        if iterable:
            for elemento in iterable:
                self.__agregar_al_final(elemento)
    
    @property
    def cabeza(self):
        return self.__cabeza
    
    @cabeza.setter
    def cabeza(self, cabeza):
        self.__cabeza = cabeza

    @property
    def cola(self):
        return self.__cola
    
    @cola.setter
    def cola(self, cola):
        self.__cola = cola
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter         
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def __iter__(self):
        self.__iterador = self.__cabeza
        return self
    
    def __next__(self):
        if self.__iterador is None:
            raise StopIteration
        dato = self.__iterador.dato
        self.__iterador = self.__iterador.siguiente
        return dato

    def esta_vacia(self):
        return self.__cabeza is None
    
    def __len__(self):
        return self.__tamanio
    
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.__cabeza = nuevo
            self.__cola = nuevo
        else:
            nuevo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo
            self.__cabeza = nuevo
        self.__tamanio += 1

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.__cabeza = nuevo
            self.__cola = nuevo
        else:
            self.__cola.siguiente = nuevo
            nuevo.anterior = self.__cola
            self.__cola = nuevo
        self.__tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.__tamanio:
            raise IndexError("Posición fuera de rango")
        
        nuevo = Nodo(dato)
        if posicion == 0:
            nuevo.siguiente = self.__cabeza
            if self.__cabeza:
                self.__cabeza.anterior = nuevo
            self.__cabeza = nuevo
            if self.__tamanio == 0:
                self.__cola = nuevo
            self.__tamanio += 1
            return
        
        actual = self.__cabeza
        for i in range(posicion - 1):
            actual = actual.siguiente
        
        nuevo.siguiente = actual.siguiente
        nuevo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo
        actual.siguiente = nuevo
        
        if nuevo.siguiente is None:
            self.__cola = nuevo
        
        self.__tamanio += 1

    def extraer(self, posicion = None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        
        if posicion is None:
            posicion = self.__tamanio - 1
        
        if posicion < 0:
            posicion += self.__tamanio
        
        if posicion < 0 or posicion >= self.__tamanio:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            dato = self.__cabeza.dato
            self.__cabeza = self.__cabeza.siguiente
            if self.__cabeza:
                self.__cabeza.anterior = None
            else:
                self.__cola = None
            self.__tamanio -= 1
            return dato
        
        actual = self.__cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        dato = actual.dato
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.__cola:
            self.__cola = actual.anterior
        
        self.__tamanio -= 1
        return dato
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        for valor in self:
            copia.agregar_al_final(valor)
        return copia
    
    def invertir(self):
        if self.__esta_vacia():
            return
        actual = self.__cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.__cabeza, self.__cola = self.__cola, self.__cabeza

    def concatenar(self, lista):
        if lista.esta_vacia():
            return
        if self.__esta_vacia():
            self.__cabeza = lista.cabeza
            self.__cola = lista.cola
        else:
            copia_lista = lista.copiar()
            self.__cola.siguiente = copia_lista.cabeza
            copia_lista.cabeza.anterior = self.__cola
            self.__cola = copia_lista.cola
        self.__tamanio += len(lista)

        if self.__cabeza:
            self.__cabeza.anterior = None

    def __add__(self, lista):
        nueva = self.copiar()
        copia_lista = lista.copiar()
        nueva.concatenar(copia_lista)
        return nueva