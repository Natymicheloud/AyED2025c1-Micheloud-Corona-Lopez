from modules import ListaDobleEnlazada 

class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def esta_vacio(self):
        return self.cartas.esta_vacia()

    def poner_carta_arriba(self, carta):
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacio():
            raise DequeEmptyError("No se puede sacar de un mazo vacío.")
        carta = self.cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        return len(self.cartas)

    def __str__(self):
        return str([str(carta) for carta in self.cartas])

    def __repr__(self):
        return self.__str__()