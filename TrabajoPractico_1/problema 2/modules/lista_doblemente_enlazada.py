# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código

from modules import ListaDobleEnlazada 

class DequeEmptyError(Exception):
    """Excepción lanzada cuando se intenta extraer de un mazo vacío."""
    pass

class Mazo:
    def __init__(self):
        self.cartas = ListaDobleEnlazada()

    def esta_vacio(self):
        """Devuelve True si el mazo está vacío."""
        return self.cartas.esta_vacia()

    def poner_carta_arriba(self, carta):
        """Agrega una carta al inicio del mazo (arriba)."""
        self.cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Agrega una carta al final del mazo (abajo)."""
        self.cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Extrae una carta del inicio del mazo.
        Si mostrar=True, se hace visible.
        Lanza DequeEmptyError si el mazo está vacío.
        """
        if self.esta_vacio():
            raise DequeEmptyError("No se puede sacar de un mazo vacío.")
        carta = self.cartas.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        """Permite usar len(mazo)."""
        return len(self.cartas)

    def __str__(self):
        """Representación legible del mazo."""
        return str([str(carta) for carta in self.cartas])

    def __repr__(self):
        return self.__str__()
