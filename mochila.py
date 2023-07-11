def fractional_knapsack(W, B, Q):
    # Calculamos la relación beneficio-peso para cada objeto
    ratios = [(b / w, w, b) for w, b in zip(W, B)]

    # Ordenamos los objetos en función de la relación beneficio-peso de forma descendente
    ratios.sort(reverse=True)

    total_value = 0  # Valor total de los objetos seleccionados
    total_weight = 0  # Peso total de los objetos seleccionados

    for ratio, weight, benefit in ratios:
        if total_weight + weight <= Q:  # Si el objeto cabe completamente en la mochila
            total_value += benefit
            total_weight += weight
        else:  # Si el objeto no cabe completamente, se toma una fracción del mismo
            remaining_space = Q - total_weight
            fraction = remaining_space / weight
            total_value += fraction * benefit
            break

    return total_value
# Construcción de ejemplo
W = [5, 6, 9, 1, 8, 7, 6, 1, 3, 4, 5]  # Peso de los objetos
B = [4, 1, 3, 4, 6, 8, 7, 5, 6, 1, 6]  # Beneficio de los objetos
Q = 25  # Capacidad de la mochila

max_value = fractional_knapsack(W, B, Q)
print("Valor máximo obtenido:", max_value)
