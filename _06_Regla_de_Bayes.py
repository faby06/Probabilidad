# Definir las probabilidades a priori
# P(A): Probabilidad de tener una enfermedad (por ejemplo, 0.01)
# P(B|A): Probabilidad de dar positivo en la prueba si tienes la enfermedad (por ejemplo, 0.95)
# P(B|�A): Probabilidad de dar positivo en la prueba si no tienes la enfermedad (por ejemplo, 0.05)
probabilidad_enfermedad = 0.01
probabilidad_positivo_dado_enfermedad = 0.95
probabilidad_positivo_dado_no_enfermedad = 0.05

# Calcular la probabilidad de tener la enfermedad dado un resultado positivo en la prueba
# P(A|B) = (P(A) * P(B|A)) / (P(A) * P(B|A) + P(�A) * P(B|�A))
probabilidad_positivo_dado_enfermedad = (probabilidad_enfermedad * probabilidad_positivo_dado_enfermedad)
probabilidad_positivo_dado_no_enfermedad = (1 - probabilidad_enfermedad) * probabilidad_positivo_dado_no_enfermedad
probabilidad_tener_enfermedad = probabilidad_positivo_dado_enfermedad / (probabilidad_positivo_dado_enfermedad + probabilidad_positivo_dado_no_enfermedad)

print(f"La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es: {probabilidad_tener_enfermedad:.2f}")


