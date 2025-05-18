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
    contador_llegada = 0
    def __init__(self):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__llegada = Paciente.contador_llegada
        Paciente.contador_llegada += 1

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_riesgo(self):
        return self.__riesgo
    
    def get_descripcion_riesgo(self):
        return self.__descripcion

    def __lt__(self, other):
        if self.__riesgo != other.__riesgo:
            return self.__riesgo < other.__riesgo
        return self.__llegada < other.__llegada
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion + '-' + str(self.__llegada)
        return cad

if __name__ == '__main__':
    paciente1 = Paciente()
    paciente2 = Paciente()
    paciente3 = Paciente()

    print("Paciente 1:", paciente1)
    print("Paciente 2:", paciente2)
    print("Paciente 3:", paciente3)

    if paciente1 < paciente2 and paciente1 < paciente3:
        print(f"{paciente1.get_nombre()} tiene mayor prioridad que {paciente2.get_nombre()} y {paciente3.get_nombre()}")
    elif paciente2 < paciente1 and paciente2 < paciente3:
        print(f"{paciente2.get_nombre()} tiene mayor prioridad que {paciente1.get_nombre()} y {paciente3.get_nombre()}")
    elif paciente3 < paciente1 and paciente3 < paciente2:
        print(f"{paciente3.get_nombre()} tiene mayor prioridad que {paciente1.get_nombre()} y {paciente2.get_nombre()}")