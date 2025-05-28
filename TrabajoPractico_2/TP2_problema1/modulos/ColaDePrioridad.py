from modulos.MonticuloBinario import MonticuloBinario

class ColaPrioridad(): #representa una cola de prioridad basada en un montículo binario, encapsula operaciones de elementos con prioridad
    def __init__(self):
        self.__monticulo = MonticuloBinario() #inicializa un montículo binario para manejar los pacientes, solo la clase ColaPrioridad puede acceder a él directamente ya que es privado
    
    def insertar(self, dato): #inserta un dato (en este caso, paciente) en la cola de prioridad (el dato debe ser un objeto de la clase Paciente)
        self.__monticulo.Insertar(dato) #llama al método Insertar del montículo binario para agregar el dato (paciente), manteniendo el orden de prioridad   
    
    def eliminar(self): #elimina el dato (paceinte) con menor prioridad numerica de la cola (el paciente con mayor riesgo)
        return self.__monticulo.eliminarMin() #llama al método eliminarMin del montículo binario para obtener y eliminar el dato (paciente) con menor prioridad numerica, que es el que debe ser atendido primero

    @property #permite acceder al tamaño actual de la cola de prioridad como un atributo
    def tamano(self): 
        return self.__monticulo.tamañoactual #devuelve el tamaño actual del montículo, que representa la cantidad de pacientes en la cola de prioridad
    
    @property #permite acceder a la lista de pacientes en la cola de prioridad como un atributo
    def datos(self):
        return self.__monticulo.listamonticulo[1:] #devuelve la lista de datos (pacientes) en el montículo, excluyendo el primer elemento (0), representando los pacientes en la cola de prioridad