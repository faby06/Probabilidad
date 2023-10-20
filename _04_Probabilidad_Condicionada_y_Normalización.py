# Definir un conjunto de datos de ejemplo
datos = {
    "A": 30,
    "B": 20,
    "C": 50
}

# Definir el evento de condici�n
condicion = "A"

# Calcular la probabilidad condicionada de un evento dado el evento de condici�n
# P(B|A) = P(A y B) / P(A)
# En este ejemplo, calculamos P(B|A)
probabilidad_condicionada = datos.get("B", 0) / datos.get(condicion, 1)

print(f"La probabilidad condicionada P(B|A) es: {probabilidad_condicionada}")

# Normalizar las probabilidades para asegurarse de que sumen 1
total_probabilidad = sum(datos.values())
probabilidades_normalizadas = {evento: frecuencia / total_probabilidad for evento, frecuencia in datos.items()}

print("Probabilidades normalizadas:")
for evento, probabilidad in probabilidades_normalizadas.items():
    print(f"P({evento}) = {probabilidad}")

