from random import randint, choices #choices perimite elegir un elemento de una lista basado en una distribucion de probabilidades

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] #critico es el menos probable

class Paciente: 
    contador_llegada = 0 #cuenta cuantos pacientes han llegado, se usa para asignar un orden de llegada de cada paciente
    def __init__(self):
        n = len(nombres) #número de nombres y apellidos disponibles
        self.__nombre = nombres[randint(0, n-1)] #selecciona un nombre aleatorio de la lista
        self.__apellido = apellidos[randint(0, n-1)] #selecciona un apellido aleatorio de la lista
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0] #selecciona un nivel de riesgo basado en las probabilidades definidas
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1] # asigna una descripción de riesgo basada en el nivel de riesgo seleccionado
        self.__llegada = Paciente.contador_llegada #asigna el orden de llegada del paciente
        Paciente.contador_llegada += 1 #incrementa el contador de llegada para el próximo paciente

    def get_nombre(self): #devuelve el nombre del paciente
        return self.__nombre
    
    def get_apellido(self): #devuelve el apellido del paciente
        return self.__apellido 
    
    def get_riesgo(self): #devuelve el nivel de riesgo del paciente
        return self.__riesgo
    
    def get_descripcion_riesgo(self): #devuelve la descripción del riesgo del paciente
        return self.__descripcion

    def __lt__(self, other): #compara dos pacientes para determinar cuál tiene mayor prioridad numerica (menor riesgo)
        #lt es less than
        if self.__riesgo != other.__riesgo: #compara los niveles de riesgo
            return self.__riesgo < other.__riesgo #si son diferentes, el paciente con menor riesgo tiene mayor prioridad numerica
        return self.__llegada < other.__llegada #si los riesgos son iguales, se prioriza al que llegó primero
    
    def __str__(self): #representa el paciente como una cadena de texto
        cad = self.__nombre + ' ' 
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion + '-' + str(self.__llegada)
        return cad #devuelve la cadena con la informacion del paciente
