
import random

# Simulaci�n de lanzamiento de moneda justa
def lanzamiento_moneda():
    return random.choice(['cara', 'cruz'])

# N�mero de lanzamientos
num_lanzamientos = 1000

# Contadores de caras y cruces
cara_count = 0
cruz_count = 0

for _ in range(num_lanzamientos):
    resultado = lanzamiento_moneda()
    if resultado == 'cara':
        cara_count += 1
    else:
        cruz_count += 1

# Probabilidad de obtener caras
probabilidad_cara = cara_count / num_lanzamientos
print("Probabilidad de obtener caras:", probabilidad_cara)
