"""
Sala de emergencias
"""
import paciente as pac
import MonticuloBinario as mb

monticulo = mb.MonticuloBinario()

for n in range(20):
    paciente = pac.Paciente()
    monticulo.Insertar(paciente)

print("Pacientes en la sala de espera:")
for paciente in monticulo.listamonticulo[1:]:
    print(paciente)

while monticulo.tamañoactual > 0:
    print("El paciente atendido es:", monticulo.eliminarMin())
else:
    print("No hay pacientes en la sala de espera")