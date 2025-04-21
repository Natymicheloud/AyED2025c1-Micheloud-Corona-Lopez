class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._previo = None
        self._siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamano = 0

    def esta_vacia(self):
        return self._cabeza is None
    
    def __len__(self):
        return self._tamano
    
    def agregar_al_inicio(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            nuevo._siguiente = self._cabeza
            self._cabeza._previo = nuevo
            self._cabeza = nuevo
        self._tamano += 1

    def agregar_al_final(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo
            self._cola = nuevo
        else:
            self._cola._siguiente = nuevo
            nuevo._previo = self._cola
            self._cola = nuevo
        self._tamano += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self._tamano:
            raise IndexError("Posición fuera de rango")
        
        nuevo = Nodo(dato)
        if posicion == 0:
            nuevo._siguiente = self._cabeza
            if self._cabeza:
                self._cabeza._previo = nuevo
            self._cabeza = nuevo
            if self._tamano == 0:
                self._cola = nuevo
            self._tamano += 1
            return
        
        actual = self._cabeza
        for i in range(posicion - 1):
            actual = actual._siguiente
        
        nuevo._siguiente = actual._siguiente
        nuevo._previo = actual
        if actual._siguiente:
            actual._siguiente._previo = nuevo
        actual._siguiente = nuevo
        
        if nuevo._siguiente is None:
            self._cola = nuevo
        
        self._tamano += 1

    def extraer(self, posicion):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        
        if posicion < 0 or posicion >= self._tamano:
            raise IndexError("Posición fuera de rango")

        if posicion == 0:
            dato = self._cabeza._dato
            self._cabeza = self._cabeza._siguiente
            if self._cabeza:
                self._cabeza._previo = None
            else:
                self._cola = None
            self._tamano -= 1
            return dato
        
        actual = self._cabeza
        for _ in range(posicion):
            actual = actual._siguiente
        
        dato = actual._dato
        if actual._previo:
            actual._previo._siguiente = actual._siguiente
        if actual._siguiente:
            actual._siguiente._previo = actual._previo
        if actual == self._cola:
            self._cola = actual._previo
        
        self._tamano -= 1
        return dato
    
    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self._cabeza
        while actual:
            copia.agregar_al_final(actual._dato)
            actual = actual._siguiente
        return copia
    
    def invertir(self):
        if self.esta_vacia():
            return
        actual = self._cabeza
        while actual:
            actual._previo, actual._siguiente = actual._siguiente, actual._previo
            actual = actual._previo
        self._cabeza, self._cola = self._cola, self._cabeza

    def concatenar(self, lista):
        if lista.esta_vacia():
            return
        if self.esta_vacia():
            self._cabeza = lista._cabeza
            self._cola = lista._cola
        else:
            self._cola._siguiente = lista._cabeza
            lista._cabeza._previo = self._cola
            self._cola = lista._cola
        self._tamano += len(lista)

    def __add__(self, lista):
        nueva = self.copiar()
        copia_lista = lista.copiar()
        nueva.concatenar(copia_lista)
        return nueva

