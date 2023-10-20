# Definir un conjunto de datos de ejemplo
datos = ["A", "B", "A", "C", "A", "B", "C", "A", "A", "B"]

# Definir el evento de inter�s
evento_interes = "A"

# Calcular la probabilidad a priori del evento de inter�s
# P(A) = (N�mero de veces que A ocurre) / (N�mero total de eventos)
probabilidad_a_priori = datos.count(evento_interes) / len(datos)

print(f"La probabilidad a priori de '{evento_interes}' es: {probabilidad_a_priori}")

