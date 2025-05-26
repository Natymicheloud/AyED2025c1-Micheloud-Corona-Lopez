class MonticuloBinario:
    """Implementación de un min-heap para almacenar tuplas (prioridad, dato_1, dato_2)"""
    
    def __init__(self):
        """Inicializa el montículo con lista base y contador de tamaño"""
        self.listamonticulo = [0]  # El índice 0 no se usa (facilita cálculos)
        self.tamañoactual = 0      # Contador de elementos
    
    def esta_vacio(self):
        """Devuelve True si el montículo está vacío"""
        return self.tamañoactual == 0
    
    def infiltrar_arriba(self, i):
        """Ajusta el montículo hacia arriba para mantener la propiedad de orden"""
        while i // 2 > 0:
            # Compara solo el primer elemento de la tupla (la prioridad)
            if self.listamonticulo[i][0] < self.listamonticulo[i // 2][0]:
                # Intercambia las tuplas completas
                self.listamonticulo[i], self.listamonticulo[i // 2] = \
                    self.listamonticulo[i // 2], self.listamonticulo[i]
            i = i // 2
    
    def insertar(self, tupla):
        """Inserta una nueva tupla en el montículo"""
        self.listamonticulo.append(tupla)
        self.tamañoactual += 1
        self.infiltrar_arriba(self.tamañoactual)
    
    def hijo_min(self, i):
        """Encuentra el índice del hijo con menor prioridad"""
        if (i * 2) + 1 > self.tamañoactual:
            return i * 2
        else:
            # Compara solo el primer elemento de las tuplas (la prioridad)
            if self.listamonticulo[i * 2][0] < self.listamonticulo[(i * 2) + 1][0]:
                return i * 2
            else:
                return (i * 2) + 1
    
    def infiltrar_abajo(self, i):
        """Ajusta el montículo hacia abajo para mantener la propiedad de orden"""
        while (i * 2) <= self.tamañoactual:
            hijomin = self.hijo_min(i)
            # Compara solo el primer elemento de las tuplas
            if self.listamonticulo[i][0] > self.listamonticulo[hijomin][0]:
                # Intercambia las tuplas completas
                self.listamonticulo[i], self.listamonticulo[hijomin] = \
                    self.listamonticulo[hijomin], self.listamonticulo[i]
            i = hijomin
    
    def eliminar_min(self):
        """Elimina y devuelve la tupla con menor prioridad (la raíz)"""
        if self.tamañoactual == 0:
            return None
        
        eliminado = self.listamonticulo[1]
        self.listamonticulo[1] = self.listamonticulo[self.tamañoactual]
        self.tamañoactual -= 1
        self.listamonticulo.pop()
        self.infiltrar_abajo(1)
        return eliminado
    
    def construir_monticulo(self, lista):
        """Construye un montículo a partir de una lista existente en O(n)"""
        self.tamañoactual = len(lista)
        self.listamonticulo = [0] + lista[:]
        i = len(lista) // 2
        while i > 0:
            self.infiltrar_abajo(i)
            i -= 1

class MonticuloBinario:
    """Implementación de un min-heap para almacenar tuplas (prioridad, dato_1, dato_2)"""
    
    def __init__(self):
        """Inicializa el montículo con lista base y contador de tamaño"""
        self.listamonticulo = [0]  # El índice 0 no se usa (facilita cálculos)
        self.tamañoactual = 0      # Contador de elementos
    
    def esta_vacio(self):
        """Devuelve True si el montículo está vacío"""
        return self.tamañoactual == 0
    
    def infiltrar_arriba(self, i):
        """Ajusta el montículo hacia arriba para mantener la propiedad de orden"""
        while i // 2 > 0:
            if self.listamonticulo[i][0] < self.listamonticulo[i // 2][0]:
                self.listamonticulo[i], self.listamonticulo[i // 2] = \
                    self.listamonticulo[i // 2], self.listamonticulo[i]
            i = i // 2
    
    def insertar(self, tupla):
        """Inserta una nueva tupla en el montículo"""
        self.listamonticulo.append(tupla)
        self.tamañoactual += 1
        self.infiltrar_arriba(self.tamañoactual)
    
    def hijo_min(self, i):
        """Encuentra el índice del hijo con menor prioridad"""
        if (i * 2) + 1 > self.tamañoactual:
            return i * 2
        else:
            if self.listamonticulo[i * 2][0] < self.listamonticulo[(i * 2) + 1][0]:
                return i * 2
            else:
                return (i * 2) + 1
    
    def infiltrar_abajo(self, i):
        """Ajusta el montículo hacia abajo para mantener la propiedad de orden"""
        while (i * 2) <= self.tamañoactual:
            hijomin = self.hijo_min(i)
            if self.listamonticulo[i][0] > self.listamonticulo[hijomin][0]:
                self.listamonticulo[i], self.listamonticulo[hijomin] = \
                    self.listamonticulo[hijomin], self.listamonticulo[i]
            i = hijomin
    
    def eliminar_min(self):
        """Elimina y devuelve la tupla con menor prioridad (la raíz)"""
        if self.tamañoactual == 0:
            return None
        
        eliminado = self.listamonticulo[1]
        self.listamonticulo[1] = self.listamonticulo[self.tamañoactual]
        self.tamañoactual -= 1
        self.listamonticulo.pop()
        self.infiltrar_abajo(1)
        return eliminado
    
    def construir_monticulo(self, lista):
        """Construye un montículo a partir de una lista existente en O(n)"""
        self.tamañoactual = len(lista)
        self.listamonticulo = [0] + lista[:]
        i = len(lista) // 2
        while i > 0:
            self.infiltrar_abajo(i)
            i -= 1
