"""
Sala de emergencias
"""
from modulos.paciente import Paciente 
from modulos.ColaDePrioridad import ColaPrioridad    

cola = ColaPrioridad()

for n in range(20):
    paciente = Paciente()
    cola.insertar(paciente)

print("Pacientes en la sala de espera:")
for paciente in cola.pacientes:
    print(paciente)

while cola.tamano > 0:
    print("El paciente atendido es:", cola.eliminar())

print("No hay pacientes en la sala de espera")