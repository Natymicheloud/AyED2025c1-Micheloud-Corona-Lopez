"""
Sala de emergencias
"""

from modulos.paciente import Paciente 
from modulos.ColaDePrioridad import ColaPrioridad    

#prueba de que la sala de emergencias funciona correctamente
cola = ColaPrioridad() #inicializa la cola de prioridad

for n in range(20): #se generan 20 pacientes
    paciente = Paciente() 
    cola.insertar(paciente) #inserta el paciente en la cola de prioridad

print("Pacientes en la sala de espera:")
for paciente in cola.datos: #lista de pacientes en la cola
    print(paciente) #imprime cada paciente

while cola.tamano > 0: #mientras haya pacientes en la cola
    print("El paciente atendido es:", cola.eliminar()) #elimina y retorna el paciente con mayor prioridad

print("No hay pacientes en la sala de espera") #mensaje final cuando la cola está vacía