def algoritmo_banquero(asignado, necesidad, disponible):
    n_procesos = len(asignado)
    n_recursos = len(asignado[0])
    terminado = [False] * n_procesos
    secuencia = []

    while len(secuencia) < n_procesos:
        progreso = False
        for i in range(n_procesos):
            if not terminado[i]:
                if all(necesidad[i][r] <= disponible[r] for r in range(n_recursos)):
                    # liberar recursos
                    for r in range(n_recursos):
                        disponible[r] += asignado[i][r]
                    terminado[i] = True
                    secuencia.append(chr(ord('A') + i))
                    progreso = True
        if not progreso:
            break

    if len(secuencia) == n_procesos:
        print("Estado seguro. Secuencia:", " → ".join(secuencia))
    else:
        print("No hay estado seguro.")


# Datos del problema:
asignado = [
    [3, 0, 1, 1],
    [2, 1, 0, 0],
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

disponible = [1, 0, 2, 0]

algoritmo_banquero(asignado, necesidad, disponible)
