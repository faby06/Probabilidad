
# Definir un dado de seis caras
dado = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

# Calcular la suma de las frecuencias de todos los posibles resultados
total_frecuencia = sum(dado.values())

# Crear una distribuci�n de probabilidad normalizada
distribucion_probabilidad = {resultado: frecuencia / total_frecuencia for resultado, frecuencia in dado.items()}

# Imprimir la distribuci�n de probabilidad
for resultado, probabilidad in distribucion_probabilidad.items():
    print(f"P({resultado}) = {probabilidad}")
