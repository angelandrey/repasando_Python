print(" ")
print("Angel Andrey Muñoz Centeno 3W")
print(" ")
# Asignamos un valor a la variable 'nota' que representa la calificación.
nota = 7  # Cambia este valor por el que desees

# Usamos una serie de condiciones (if, elif) para evaluar el rango de la nota.
if 0 <= nota < 5:
    # Si la nota está entre 0 y 4, se considera un suspenso.
    print("SUSPENSO")
elif 5 <= nota < 6:
    # Si la nota está entre 5 y 5.99, se considera suficiente.
    print("SUFICIENTE")
elif 6 <= nota < 7:
    # Si la nota está entre 6 y 6.99, se considera bien.
    print("BIEN")
elif 7 <= nota < 9:
    # Si la nota está entre 7 y 8.99, se considera notable.
    print("NOTABLE")
elif 9 <= nota <= 10:
    # Si la nota está entre 9 y 10, se considera sobresaliente.
    print("SOBRESALIENTE")
else:
    # Si la nota no entra en ninguno de los rangos anteriores, es inválida.
    print("NOTA NO VÁLIDA")
