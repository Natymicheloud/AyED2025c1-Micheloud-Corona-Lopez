from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

# contador de llegada de pacientes
contador_llegada=0

class Paciente:
    def __init__(self):
        global contador_llegada
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__llegada = contador_llegada
        contador_llegada += 1


    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    
    # def __lt__(self, other):
    #     if self.__riesgo > other.__riesgo:
    #         turno= other.__riesgo

    #     if self.__riesgo < other.__riesgo:
    #         turno= self.__riesgo

    #     else:
    #         if self.__riesgo == other.__riesgo:
    #             if self.__llegada > other.__llegada:
    #                 turno = other.__llegada
    #             else:
    #                 turno= self.__llegada

    #     return turno


    def __lt__(self, other):
        if self.__riesgo != other.__riesgo:
            return self.__riesgo < other.__riesgo
        return self.__llegada < other.__llegada

Paciente1= Paciente()
Paciente2= Paciente()
if Paciente1 > Paciente2:
    print("1")
else:
    print(Paciente1)
