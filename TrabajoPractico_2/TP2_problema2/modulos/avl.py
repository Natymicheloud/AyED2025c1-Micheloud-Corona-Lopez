class NodoAVL():
    def __init__(self, fecha, temperatura):
        self._fecha = fecha #clave del nodo
        self._temperatura = temperatura #valor del nodo, asociado a la clave
        self._hijoizquierdo = None
        self._hijoderecho = None
        self._altura = 1 #altura del nodo, para balanceo
        self._equilibrio = 0 #diferencia de altura entre subarboles

class AVL():
    def __init__(self):
        self._raiz = None 

    def _insertar(self, nodo, fecha, temperatura): #método privado que aplica la inserción recursiva y el balanceo del árbol
        if nodo is None:
            return NodoAVL(fecha, temperatura) #si el nodo es una hoja, se crea uno nuevo con los datos
        
        elif fecha < nodo._fecha:
            nodo._hijoizquierdo = self._insertar(nodo._hijoizquierdo, fecha, temperatura) #si la fecha es menor, se inserta a la izquierda
        
        else:
            nodo._hijoderecho = self._insertar(nodo._hijoderecho, fecha, temperatura) #si la fecha es mayor, se inserta a la derecha

        return self._balancear(nodo) #despues de insertar, se balancea el árbol
    
    def insertar(self, fecha, temperatura): #interfaz pública para insertar datos en el AVL sin exponer la lógica interna
        self._raiz = self._insertar(self._raiz, fecha, temperatura)

    def _buscar(self, nodo, fecha): #método privado que aplica la búsqueda recursiva
        if nodo is None:
            return None #si el nodo es None, no se encontró la fecha
        
        if fecha == nodo._fecha:
            return nodo._temperatura #si la fecha coincide, se devuelve la temperatura
        
        elif fecha < nodo._fecha:
            return self._buscar(nodo._hijoizquierdo, fecha) #si la fecha es menor al nodo actual, se busca en el subárbol izquierdo
        
        else:
            return self._buscar(nodo._hijoderecho, fecha) #si la fecha es mayor al nodo actual, se busca en el subárbol derecho
        
    def buscar(self, fecha): #interfaz pública para buscar datos en el AVL sin exponer la lógica interna
        return self._buscar(self._raiz, fecha) #busca temperatura por fecha
    
    def _balancear(self, nodo): #método privado que aplica el balanceo del árbol
        if nodo is None:
            return nodo #si el nodo es None, no se hace nada
        
        nodo._altura = 1 + max(self._altura(nodo._hijoizquierdo), self._altura(nodo._hijoderecho)) #se actualiza la altura del nodo, siendo 1 + la máxima altura de sus hijos
        nodo._equilibrio = self._altura(nodo._hijoizquierdo) - self._altura(nodo._hijoderecho) #se calcula el factor de equilibrio del nodo, siendo la diferencia de alturas entre sus hijos izquierdo y derecho

        if nodo._equilibrio > 1: #si el factor de equilibrio es mayor a 1, el árbol está desbalanceado hacia la izquierda
            if nodo._hijoizquierdo and nodo._hijoizquierdo._equilibrio < 0: #si el hijo izquierdo tiene un factor de equilibrio negativo, se hace una rotación izquierda en el hijo izquierdo y una rotación derecha en el nodo actual (dos rotaciones)
                nodo._hijoizquierdo = self._rotarIzquierda(nodo._hijoizquierdo)
            nodo = self._rotarDerecha(nodo)
        
        elif nodo._equilibrio < -1: #si el factor de equilibrio es menor a -1, el árbol está desbalanceado hacia la derecha
            if nodo._hijoderecho and nodo._hijoderecho._equilibrio > 0: #si el hijo derecho tiene un factor de equilibrio positivo, se hace una rotación derecha en el hijo derecho y una rotación izquierda en el nodo actual (dos rotaciones)
                nodo._hijoderecho = self._rotarDerecha(nodo._hijoderecho)
            nodo = self._rotarIzquierda(nodo)
        
        #recalcula la altura y el equilibrio despues de la rotacion 
        nodo._altura = 1 + max(self._altura(nodo._hijoizquierdo), self._altura(nodo._hijoderecho)) #se actualiza la altura del nodo, siendo 1 + la máxima altura de sus hijos
        nodo._equilibrio = self._altura(nodo._hijoizquierdo) - self._altura(nodo._hijoderecho) #se calcula el factor de equilibrio del nodo, siendo la diferencia de alturas entre sus hijos izquierdo y derecho
    
        return nodo #si el árbol está balanceado, se devuelve el nodo sin cambios
    
    def _altura(self, nodo): #método privado que devuelve la altura del nodo
        return nodo._altura if nodo else 0 #devuelve la altura del nodo, o 0 si es None

    def _rotarDerecha(self, nodo): #método privado que aplica la rotación derecha
        nuevaraiz = nodo._hijoizquierdo #se guarda el hijo izquierdo del nodo actual como nueva raíz
        nodo._hijoizquierdo = nuevaraiz._hijoderecho #el hijo derecho de la nueva raíz se convierte en el hijo izquierdo del nodo actual
        nuevaraiz._hijoderecho = nodo
        
        nodo._altura = 1 + max(self._altura(nodo._hijoizquierdo), self._altura(nodo._hijoderecho)) #se actualiza la altura del nodo actual, siendo 1 + la máxima altura de sus hijos
        nodo._equilibrio = self._altura(nodo._hijoizquierdo) - self._altura(nodo._hijoderecho) #se actualiza el factor de equilibrio del nodo actual, siendo la diferencia de alturas entre sus hijos izquierdo y derecho

        nuevaraiz._altura = 1 + max(self._altura(nuevaraiz._hijoizquierdo), self._altura(nuevaraiz._hijoderecho)) #se actualiza la altura de la nueva raíz, siendo 1 + la máxima altura de sus hijos
        nuevaraiz._equilibrio = self._altura(nuevaraiz._hijoizquierdo) - self._altura(nuevaraiz._hijoderecho) #se actualiza el factor de equilibrio de la nueva raiz, siendo la diferencia de alturas entre sus hijos izquierdo y derecho

        return nuevaraiz 
    
    def _rotarIzquierda(self, nodo): #método privado que aplica la rotación izquierda
        nuevaraiz = nodo._hijoderecho #se guarda el hijo derecho del nodo actual como nueva raíz
        nodo._hijoderecho = nuevaraiz._hijoizquierdo #el hijo izquierdo de la nueva raíz se convierte en el hijo derecho del nodo actual
        nuevaraiz._hijoizquierdo = nodo
       
        nodo._altura = 1 + max(self._altura(nodo._hijoizquierdo), self._altura(nodo._hijoderecho))
        nodo._equilibrio = self._altura(nodo._hijoizquierdo) - self._altura(nodo._hijoderecho)

        nuevaraiz._altura = 1 + max(self._altura(nuevaraiz._hijoizquierdo), self._altura(nuevaraiz._hijoderecho))
        nuevaraiz._equilibrio = self._altura(nuevaraiz._hijoizquierdo) - self._altura(nuevaraiz._hijoderecho)
        
        return nuevaraiz