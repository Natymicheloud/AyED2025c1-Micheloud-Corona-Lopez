from modulos.paciente import Paciente

#prueba de que los pacientes se crean y se comparan por riesgo y orden de llegada correctamente
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