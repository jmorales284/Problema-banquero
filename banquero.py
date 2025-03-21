# Función para verificar el estado seguro
def es_seguro(disponible, asignado, necesidad):
    n = len(asignado)
    m = len(disponible)
    trabajo = disponible.copy()
    acabado = [False] * n
    secuencia = []

    print("\nComenzando comprobación de estado seguro...")
    print(f"Recursos disponibles inicialmente: {trabajo}\n")

    while True:
        encontrado = False
        for i in range(n):
            if not acabado[i] and all(necesidad[i][j] <= trabajo[j] for j in range(m)):
                print(f"Proceso {i} puede ejecutarse (necesidad: {necesidad[i]}, asignado: {asignado[i]}).")
                trabajo = [trabajo[j] + asignado[i][j] for j in range(m)]
                acabado[i] = True
                secuencia.append(i)
                print(f"Recursos disponibles tras proceso {i}: {trabajo}\n")
                encontrado = True
        if not encontrado:
            break

    if all(acabado):
        print("El sistema está en un estado SEGURO.")
        print("Secuencia segura de procesos:", secuencia)
        return True
    else:
        print("El sistema NO está en un estado seguro.")
        return False

# Función de petición de recursos
def peticion_recursos(i, peticion, disponible, asignado, necesidad):
    m = len(disponible)

    print(f"\nEl proceso {i} solicita: {peticion}")

    if any(peticion[j] > necesidad[i][j] for j in range(m)):
        print("Error: El proceso solicita más recursos de los que necesita.")
        return False

    if any(peticion[j] > disponible[j] for j in range(m)):
        print(f"El proceso {i} debe esperar: no hay recursos suficientes.")
        return False

    disponible_temp = [disponible[j] - peticion[j] for j in range(m)]
    asignado_temp = [fila.copy() for fila in asignado]
    necesidad_temp = [fila.copy() for fila in necesidad]

    for j in range(m):
        asignado_temp[i][j] += peticion[j]
        necesidad_temp[i][j] -= peticion[j]

    print("Probando si la asignación temporal es segura...")

    if es_seguro(disponible_temp, asignado_temp, necesidad_temp):
        print(f"Recursos asignados con éxito al proceso {i}.")
        return disponible_temp, asignado_temp, necesidad_temp
    else:
        print("Asignación no segura, los recursos NO se otorgan.")
        return False

# Datos de prueba
disponible = [1, 0, 2, 0]

asignado = [
    [3, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
]

necesidad = [
    [1, 1, 0, 0],
    [0, 1, 1, 2],
    [3, 1, 0, 0],
    [0, 0, 1, 0],
    [2, 1, 1, 0]
]

# Comprobar el estado seguro inicial
es_seguro(disponible, asignado, necesidad)

