from datetime import datetime
from modulos.avl import AVL

class TemperaturasDB:
    def __init__(self):
        self._arbol = AVL()

    def guardar_temperatura(self, temperatura, fecha): #inserta una temperatura en el árbol, en la fecha dada como clave
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        self._arbol.insertar(fecha, temperatura)

    def devolver_temperatura(self, fecha): #devuelve la temperatura de una fecha dada
        fecha = datetime.strptime(fecha, '%d/%m/%Y')
        return self._arbol.buscar(fecha)
    
    def max_temp_rango(self, fecha1, fecha2): #devuelve la temperatura máxima en un rango de fechas
        fecha1 = datetime.strptime(fecha1, '%d/%m/%Y')
        fecha2 = datetime.strptime(fecha2, '%d/%m/%Y')

        return self._maximo(self._arbol._raiz, fecha1, fecha2)
    
    def _maximo(self, nodo, fecha1, fecha2): #busca la temperatura máxima en un rango de fechas
        if nodo is None:
            return float('-inf') #si el nodo es None, devuelve -infinito para que no afecte la comparación
        
        if nodo._fecha < fecha1:
            return self._maximo(nodo._hijoderecho, fecha1, fecha2) #si la fecha del nodo es menor a fecha1, se busca en el subárbol derecho
        
        elif nodo._fecha > fecha2: 
            return self._maximo(nodo._hijoizquierdo, fecha1, fecha2) #si la fecha del nodo es mayor a fecha2, se busca en el subárbol izquierdo
        
        #se busca el maximo en los subárboles izquierdo y derecho
        maximo_izquierdo = self._maximo(nodo._hijoizquierdo, fecha1, fecha2)
        maximo_derecho = self._maximo(nodo._hijoderecho, fecha1, fecha2)

        return max(maximo_izquierdo, maximo_derecho, nodo._temperatura) #devuelve el máximo entre los tres valores: el máximo izquierdo, el máximo derecho y la temperatura del nodo actual
    
    def min_temp_rango(self, fecha1, fecha2):
        fecha1 = datetime.strptime(fecha1, '%d/%m/%Y')
        fecha2 = datetime.strptime(fecha2, '%d/%m/%Y')

        return self._minimo(self._arbol._raiz, fecha1, fecha2)
    
    def _minimo(self, nodo, fecha1, fecha2):
        if nodo is None:
            return float('inf')
        
        if nodo._fecha < fecha1:
            return self._minimo(nodo._hijoderecho, fecha1, fecha2)
        
        elif nodo._fecha > fecha2:
            return self._minimo(nodo._hijoizquierdo, fecha1, fecha2)
        
        minimo_izquierdo = self._minimo(nodo._hijoizquierdo, fecha1, fecha2)
        minimo_derecho = self._minimo(nodo._hijoderecho, fecha1, fecha2)

        return min(minimo_izquierdo, minimo_derecho, nodo._temperatura)
    
    def temp_extremos_rango(self, fecha1, fecha2): #devuelve la temperatura mínima y máxima en un rango de fechas
        #utiliza las funciones anteriores
        minimo = self.min_temp_rango(fecha1, fecha2)
        maximo = self.max_temp_rango(fecha1, fecha2)

        return minimo, maximo
    
    def borrar_temperatura(self, fecha): #elimina una temperatura en la fecha dada
        fecha = datetime.strptime(fecha, '%d/%m/%Y')

        self._arbol._raiz = self._eliminar(self._arbol._raiz, fecha)

    def _eliminar(self, nodo, fecha):
        if nodo is None:
            return None #si el nodo es None, no se elimina nada

        if fecha < nodo._fecha:
            nodo._hijoizquierdo = self._eliminar(nodo._hijoizquierdo, fecha) #si la fecha es menor, se busca en el subárbol izquierdo

        elif fecha > nodo._fecha:
            nodo._hijoderecho = self._eliminar(nodo._hijoderecho, fecha) #si la fecha es mayor, se busca en el subárbol derecho

        else: #tres casos: nodo hoja, nodo con un hijo, nodo con dos hijos
            # caso 1: nodo hoja (sin hijos)
            if nodo._hijoizquierdo is None and nodo._hijoderecho is None:
                return None

            # caso 2: nodo con un hijo (izquierdo o derecho)
            elif nodo._hijoizquierdo is None:
                return nodo._hijoderecho

            elif nodo._hijoderecho is None:
                return nodo._hijoizquierdo

            # caso 3: nodo con dos hijos
            else:
                sucesor = self._minimo_eliminar(nodo._hijoderecho) #busca el sucesor (el nodo con la fecha mínima en el subárbol derecho)
                nodo._fecha = sucesor._fecha #reemplaza la fecha del nodo a eliminar con la fecha del sucesor
                nodo._temperatura = sucesor._temperatura #reemplaza la temperatura del nodo a eliminar con la temperatura del sucesor
                nodo._hijoderecho = self._eliminar(nodo._hijoderecho, sucesor._fecha) #elimina el sucesor del subárbol derecho
            
        return self._arbol._balancear(nodo) if nodo else nodo #balancea el árbol 

    def _minimo_eliminar(self, nodo): #busca el nodo con la fecha mínima en el subárbol
        while nodo._hijoizquierdo is not None: 
            nodo = nodo._hijoizquierdo 
        return nodo 

    def devolver_temperaturas(self, fecha1, fecha2): #devuelve una lista de temperaturas en un rango de fechas
        fecha1 = datetime.strptime(fecha1, '%d/%m/%Y')
        fecha2 = datetime.strptime(fecha2, '%d/%m/%Y')
        temperaturas = []

        self._recorrer_en_rango(self._arbol._raiz, fecha1, fecha2, temperaturas)

        return temperaturas
        
    def _recorrer_en_rango(self, nodo, fecha1, fecha2, temperaturas): #busca todas las temperaturas en un rango de fechas
        if nodo is None: 
            return #si el nodo es None, no se hace nada y se termina el recorrido
            
        if nodo._fecha >= fecha1: 
            self._recorrer_en_rango(nodo._hijoizquierdo, fecha1, fecha2, temperaturas) #si la fecha del nodo actual es mayor o igual a fecha1, se busca en el subárbol izquierdo

        if fecha1 <= nodo._fecha <= fecha2:
            temperaturas.append((f"{nodo._fecha.strftime('%d/%m/%Y')}: {nodo._temperatura}°C")) #si la fecha del nodo actual está dentro del rango, se agrega a la lista de temperaturas

        if nodo._fecha <= fecha2:
            self._recorrer_en_rango(nodo._hijoderecho, fecha1, fecha2, temperaturas) #si la fecha del nodo actual es menor o igual a fecha2, se busca en el subárbol derecho

    def cantidad_muestras(self): #devuelve la cantidad de muestras (nodos) en el árbol
        return self._contar_nodos(self._arbol._raiz)
            
    def _contar_nodos(self, nodo): 
        if nodo is None:
            return 0 #si el nodo es None, no se cuenta nada y se devuelve 0
        else:
            return 1 + self._contar_nodos(nodo._hijoizquierdo) + self._contar_nodos(nodo._hijoderecho) #cuenta el nodo actual (1) y suma la cantidad de nodos en los subárboles izquierdo y derecho, recorriendo todo el árbol recursivamente