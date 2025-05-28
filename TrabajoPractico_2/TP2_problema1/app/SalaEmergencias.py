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
    ahora = datetime.datetime.now() #obtiene la fecha y hora actual
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S') #formatea la fecha y hora en un string legible
    print('-*-'*15) #separador visual para cada ciclo
    print('\n', fecha_y_hora, '\n') #muestra la fecha y hora de entrada del paciente

    # Se crea un paciente un paciente por segundo
    # La criticidad del paciente es aleatoria
    paciente = Paciente()
    cola_de_espera.insertar(paciente) #se inserta el paciente en la cola de prioridad

    # Atención de paciente en este ciclo: en el 50% de los casos
    if random.random() < 0.5: #se genera un número aleatorio entre 0 y 1, si es menor que 0.5, se atiende al paciente
        # se atiende paciente que se encuentra al frente de la cola
        paciente_atendido = cola_de_espera.eliminar() #se elimina al paciente con mayor prioridad de la cola de espera
        print('*'*40) #separador visual para la atención del paciente
        print('Se atiende el paciente:', paciente_atendido) #imprime el paciente que se está atendiendo
        print('*'*40) #separador visual para la atención del paciente
    else: # si no se atiende al paciente en este ciclo
        # se continúa atendiendo paciente de ciclo anterior
        pass 
    
    print()

    # Se muestran los pacientes restantes en la cola de espera
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano) 
    for paciente in cola_de_espera.datos:
        print('\t', paciente)
    
    print()
    print('-*-'*15)
    
    time.sleep(1) #espera de 1 segundo antes del siguiente ciclo

