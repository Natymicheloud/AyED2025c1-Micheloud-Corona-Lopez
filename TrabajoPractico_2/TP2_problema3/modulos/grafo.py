class Vertice: #representa un nodo en el grafo
    def __init__(self, clave): 
        self.__clave = clave #clave del vertice
        self.__adyacentes = {} #diccionario que almacena los vecinos (claves) y sus ponderaciones (valores). se utiliza un diccionario porque es mas eficiente para almacenar vecinos (ya que almacena solo los que existen) y permite acceder más rápido a los vecinos y sus ponderaciones (O(1)) dado que cada aldea tiene un conjunto de vecinos y cada vecino tiene una ponderación asociada.

    def agregar_vecino(self, clave_vecino, ponderacion):
        self.__adyacentes[clave_vecino] = ponderacion #agrega un vecino al vertice con su ponderacion

    def __str__(self): #convierte el vertice a una cadena de texto
        return str(self.__clave) + "adyacentes:" + str(list(self.__adyacentes.keys())) #nombre del vertice y sus vecinos
    
    def obtener_adyacentes(self): #devuelve los vecinos del vertice
        return self.__adyacentes.keys() #keys devuelve las claves del diccionario de adyacentes
    
    def obtener_clave(self): #devuelve la clave del vertice
        return self.__clave
    
    def obtener_ponderacion(self, vecino): #devuelve la ponderacion de un vecino
        return self.__adyacentes[vecino]
    
class Grafo: #representa un grafo no dirigido y ponderado
    def __init__(self):
        self.__vertices = {} #diccionario que almacena los vertices del grafo, donde la clave es el nombre del vertice y el valor es el objeto Vertice
        self.__numero_vertices = 0 #contador de vertices en el grafo

    def agregar_vertice(self, clave):
        clave = clave.strip() #elimina espacios en blanco al inicio y al final de la clave
        self.__numero_vertices += 1 #incrementa el contador de vertices
        nuevo_vertice = Vertice(clave) #crea un nuevo vertice con la clave proporcionada
        self.__vertices[clave] = nuevo_vertice #agrega el nuevo vertice al diccionario de vertices con la clave como nombre del vertice
        return nuevo_vertice #devuelve el objeto Vertice creado
    
    def obtener_vertice(self, clave): #devuelve el vertice correspondiente a la clave proporcionada
        if clave in self.__vertices: 
            return self.__vertices[clave] #si la clave existe, devuelve el objeto Vertice
        else:
            return None #si la clave no existe, devuelve None
        
    def __contains__(self, clave): #verifica si el grafo contiene un vertice con la clave proporcionada
        return clave in self.__vertices 
    
    def agregar_arista(self, origen, destino, ponderacion): #agrega conexiones entre vertices (aristas) con una ponderacion
        if origen not in self.__vertices: #si el vertice de origen no existe, lo agrega antes de conectarlo
            self.agregar_vertice(origen)
        if destino not in self.__vertices: #si el vertice de destino no existe, lo agrega antes de conectarlo
            self.agregar_vertice(destino)
        
        self.__vertices[origen].agregar_vecino(destino, ponderacion) #agrega la conexion entre origen y destino con la ponderacion especificada
        self.__vertices[destino].agregar_vecino(origen, ponderacion) #agrega la conexion inversa, ya que el grafo es no dirigido

    def obtener_vertices(self): #devuelve una lista de las claves (nombres) de los vertices en el grafo
        return self.__vertices
    
    def __iter__(self): #permite iterar sobre los vertices del grafo
        return iter(self.__vertices.values()) #devuelve los objetos Vertice en el grafo