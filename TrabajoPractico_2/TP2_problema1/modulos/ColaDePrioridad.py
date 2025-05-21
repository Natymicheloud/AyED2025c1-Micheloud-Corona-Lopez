from modulos.MonticuloBinario import MonticuloBinario

class ColaPrioridad():
    def __init__(self):
        self.__monticulo = MonticuloBinario()
    
    def insertar(self, paciente):
        self.__monticulo.Insertar(paciente)       
    
    def eliminar(self):
        return self.__monticulo.eliminarMin()

    @property    
    def tamano(self):
        return self.__monticulo.tamañoactual
    
    @property
    def pacientes(self):
        return self.__monticulo.listamonticulo[1:]