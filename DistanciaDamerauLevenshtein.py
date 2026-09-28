def distancia(A: str, B: str) -> int:
    # Normalización
    A = A.upper().strip()
    B = B.upper().strip()

    n = len(A)
    m = len(B)

    # Casos borde rápidos
    if n == 0: return m
    if m == 0: return n

    # Matriz inicializada con enteros
    D = [[0] * (m + 1) for _ in range(n + 1)]

    # Casos base
    for i in range(1, n + 1):
        D[i][0] = i
    for j in range(1, m + 1):
        D[0][j] = j

    # Bucle principal
    for i in range(1, n + 1):
        char_a = A[i - 1]
        char_a_prev = A[i - 2] if i > 1 else None

        for j in range(1, m + 1):
            char_b = B[j - 1]

            costo_sust = 0 if char_a == char_b else 1

            eliminar = D[i - 1][j] + 1
            insertar = D[i][j - 1] + 1
            sustituir = D[i - 1][j - 1] + costo_sust

            mejor_costo = min(eliminar, insertar, sustituir)

            # Transposición 
            if i > 1 and j > 1:
                if char_a == B[j - 2] and char_a_prev == char_b:
                    transponer = D[i - 2][j - 2] + 1
                    mejor_costo = min(mejor_costo, transponer)

            D[i][j] = mejor_costo

    return D[n][m]