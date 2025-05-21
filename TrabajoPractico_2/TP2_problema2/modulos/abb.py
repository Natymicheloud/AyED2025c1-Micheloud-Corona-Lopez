class ABB():
    def __init__(self):
        self.__raiz = None
        self.__tamano = 0

    def __len__(self):
        return self.__tamano
    
    def __iter__(self):
        return self.raiz.__iter__()
    
class NodoABB():
    def __init__(self, clave, valor, izquierdo = None, derecho = None, padre = None):
        self.__clave = clave
        self.__carga = valor
        self.__hijoizquierdo = izquierdo
        self.__hijoderecho = derecho
        self.__padre = padre

    @property
    def TieneHijoIzquierdo(self):
        return self.__hijoizquierdo
    
    @property
    def TieneHijoDerecho(self):
        return self.__hijoderecho
    
    @property
    def EsHijoIzquierdo(self):
        return self.__padre and self.__padre.__hijoizquierdo == self
    
    @property
    def EsHijoDerecho(self):
        return self.__padre and self.__padre.__hijoderecho == self
    
    @property
    def EsRaiz(self):
        return not self.__padre
    
    @property
    def EsHoja(self):
        return not (self.__hijoizquierdo or self.__hijoderecho)
    
    @property
    def TieneAlgunHijo(self):
        return self.__hijoizquierdo or self.__hijoderecho
    
    @property
    def TieneAmbosHijos(self):
        return self.__hijoizquierdo and self.__hijoderecho
    
    @property
    def ReemplazarDatoNodo(self, clave, valor, hijoizq, hijoder):
        self.__clave = clave
        self.__carga = valor
        self.__hijoizquierdo = hijoizq
        self.__hijoderecho = hijoder
        if self.__TieneHijoIzquierdo():
            self.__hijoizquierdo.__padre = self
        if self.__TieneHijoDerecho():
            self.__hijoderecho.__padre = self