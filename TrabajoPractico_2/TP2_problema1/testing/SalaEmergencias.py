# -*- coding: utf-8 -*-
"""
Sala de emergencias
"""

import time
import datetime
from modulos.paciente import Paciente   
import random
from modulos.ColaDePrioridad import ColaPrioridad

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaPrioridad()

# Ciclo que gestiona la simulación
for i in range(n):
    # Fecha y hora de entrada de un paciente
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    cola_de_espera.insertar(paciente)

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5:
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminar()
        print('*'*40)
        print('Se atiende el paciente:', paciente_atendido)
        print('*'*40)
    else:
        # se continúa atendiendo paciente de ciclo anterior
        pass
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano)
    for paciente in cola_de_espera.pacientes:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)

