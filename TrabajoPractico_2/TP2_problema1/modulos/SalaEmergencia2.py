"""
Sala de emergencias
"""
import paciente as pac
import MonticuloBinario as mb

cola_de_espera = list()

for n in range(20):
    paciente = pac.Paciente()
    
    cola_de_espera.append(paciente)

monticulo = mb.MonticuloBinario()
monticulo.ConstruirMonticulo(cola_de_espera)
print("Pacientes en la sala de espera:")
for paciente in cola_de_espera:
    print(paciente)

monticulo.Insertar(paciente)

for paciente in cola_de_espera:
    if monticulo.tamañoactual > 0:
        print("El paciente atendido es:", monticulo.eliminarMin())
    else:
        print("No hay pacientes en la sala de espera")

