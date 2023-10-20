# Definir tres eventos A, B y C como conjuntos de datos
evento_A = {"soleado": 20, "lluvioso": 10}
evento_B = {"caliente": 15, "frIo": 15}
evento_C = {"no": 20, "sI": 10}

# Calcular las probabilidades marginales
probabilidad_A = sum(evento_A.values())
probabilidad_B = sum(evento_B.values())
probabilidad_C = sum(evento_C.values())

# Calcular las probabilidades conjuntas
probabilidad_A_B_C = (
    evento_A["soleado"] * evento_B["caliente"] * evento_C["sI"] +
    evento_A["lluvioso"] * evento_B["frIo"] * evento_C["sI"] +
    evento_A["soleado"] * evento_B["caliente"] * evento_C["no"] +
    evento_A["lluvioso"] * evento_B["frIo"] * evento_C["no"]
)

# Verificar la independencia condicional
independencia_condicional = probabilidad_A_B_C == (probabilidad_A * probabilidad_B * probabilidad_C)

if independencia_condicional:
    print("Los eventos A, B y C son independientes condicionalmente.")
else:
    print("Los eventos A, B y C no son independientes condicionalmente.")
