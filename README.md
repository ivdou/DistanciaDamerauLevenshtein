# DistanciaDamerauLevenshtein (OSA)
Implementación en Python de la *Distancia restringida* Damerau-Levenshtein entre 2 cadenas de texto. 

La distancia Damerau-Levenshtein estándar (no ponderada) se define mediante programación dinámica, asignando un costo unitario de 1 a cada una de las siguientes operaciones de edición:

- Inserción
- Eliminación
- Sustitución
- Transposición de caracteres consecutivos

Sean:

$$A = a_1 a_2 \dots a_n$$

$$B = b_1 b_2 \dots b_m$$

y sea $D(i, j)$ la cantidad mínima de operaciones para transformar los primeros $i$ caracteres de $A$ en los primeros $j$ caracteres de $B$.

### Inicialización

Los casos base representan la transformación desde o hacia una cadena vacía:

$$D(0, 0) = 0$$

$$D(i, 0) = i$$

$$D(0, j) = j$$

### Fórmula recursiva

Para $i \ge 1$ y $j \ge 1$:

$$
D(i, j) = \min \begin{cases}
D(i-1, j) + 1 & \text{Eliminación} \\
D(i, j-1) + 1 & \text{Inserción} \\
D(i-1, j-1) + C_{\text{sub}}(a_i, b_j) & \text{Sustitución} \\
D(i-2, j-2) + 1 & \text{si } a_i = b_{j-1} \land a_{i-1} = b_j
\end{cases}
$$

Donde el costo de sustitución $C_{\text{sub}}(a_i, b_j)$ se define como:

$$
C_{\text{sub}}(a_i, b_j) = \begin{cases}
0 & \text{si } a_i = b_j \\
1 & \text{si } a_i \neq b_j
\end{cases}
$$

La alternativa de transposición solo se evalúa cuando $i > 1$, $j > 1$ y los dos caracteres consecutivos adyacentes están intercambiados ($a_i = b_{j-1}$ y $a_{i-1} = b_j$).

### Resultado final

La distancia mínima total para transformar la cadena $A$ completa en $B$ es:

$$\text{DL}(A, B) = D(n, m)$$
