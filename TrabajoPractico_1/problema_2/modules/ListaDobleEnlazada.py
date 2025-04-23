class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        self.iterador = None

    def __iter__(self):
        self.iterador = self.cabeza
        return self
    
    def __next__(self):
        if self.iterador is None:
            raise StopIteration
        dato = self.iterador.dato
        self.iterador = self.iterador.siguiente
        return dato

    def esta_vacia(self):
        return self.cabeza is None
    
    def __len__(self):
        return self.tamanio
    
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        
        nuevo = Nodo(dato)
        if posicion == 0:
            nuevo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo
            self.cabeza = nuevo
            if self.tamanio == 0:
                self.cola = nuevo
            self.tamanio += 1
            return
        
        actual = self.cabeza
        for i in range(posicion - 1):
            actual = actual.siguiente
        
        nuevo.siguiente = actual.siguiente
        nuevo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo
        actual.siguiente = nuevo
        
        if nuevo.siguiente is None:
            self.cola = nuevo
        
        self.tamanio += 1

    def extraer(self, posicion = None):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        
        if posicion is None:
            posicion = self.tamanio - 1
        
        if posicion < 0:
            posicion += self.tamanio
        
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return dato
        
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        dato = actual.dato
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        if actual == self.cola:
            self.cola = actual.anterior
        
        self.tamanio -= 1
        return dato
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia
    
    def invertir(self):
        if self.esta_vacia():
            return
        actual = self.cabeza
        while actual:
            actual.anterior, actual.siguiente = actual.siguiente, actual.anterior
            actual = actual.anterior
        self.cabeza, self.cola = self.cola, self.cabeza

    def concatenar(self, lista):
        if lista.esta_vacia():
            return
        if self.esta_vacia():
            self.cabeza = lista.cabeza
            self.cola = lista.cola
        else:
            copia_lista = lista.copiar()
            self.cola.siguiente = copia_lista.cabeza
            copia_lista.cabeza.anterior = self.cola
            self.cola = copia_lista.cola
        self.tamanio += len(lista)

        if self.cabeza:
            self.cabeza.anterior = None

    def __add__(self, lista):
        nueva = self.copiar()
        copia_lista = lista.copiar()
        nueva.concatenar(copia_lista)
        return nueva

