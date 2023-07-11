import heapq
from collections import defaultdict

# Clase para representar un nodo del árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    # Método especial para comparar nodos por su frecuencia
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Función para generar el árbol de Huffman
def generar_arbol_huffman(frecuencias):
    cola_prioridad = []
    for caracter, frecuencia in frecuencias.items():
        nodo = NodoHuffman(caracter, frecuencia)
        heapq.heappush(cola_prioridad, nodo)

    while len(cola_prioridad) > 1:
        nodo_izq = heapq.heappop(cola_prioridad)
        nodo_der = heapq.heappop(cola_prioridad)
        nodo_padre = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
        nodo_padre.izquierda = nodo_izq
        nodo_padre.derecha = nodo_der
        heapq.heappush(cola_prioridad, nodo_padre)

    return cola_prioridad[0]

# Función para generar los códigos de Huffman recursivamente
def generar_codigos_huffman(nodo, codigo_actual, codigos_huffman):
    if nodo.caracter:
        codigos_huffman[nodo.caracter] = codigo_actual
    else:
        generar_codigos_huffman(nodo.izquierda, codigo_actual + "0", codigos_huffman)
        generar_codigos_huffman(nodo.derecha, codigo_actual + "1", codigos_huffman)

# Función para decodificar la cadena comprimida
def decodificar_cadena(cadena_comprimida, codigos_huffman):
    cadena_decodificada = ""
    codigo_actual = ""
    for bit in cadena_comprimida:
        codigo_actual += bit
        for caracter, codigo in codigos_huffman.items():
            if codigo_actual == codigo:
                cadena_decodificada += caracter
                codigo_actual = ""
                break
    return cadena_decodificada

# Obtener frecuencias de caracteres
texto = input("Ingrese un texto: ")
frecuencias = defaultdict(int)
for caracter in texto:
    frecuencias[caracter] += 1

# Generar árbol de Huffman
arbol_huffman = generar_arbol_huffman(frecuencias)

# Generar códigos de Huffman
codigos_huffman = {}
generar_codigos_huffman(arbol_huffman, "", codigos_huffman)

# Imprimir códigos de Huffman
print("Códigos de Huffman:")
for caracter, codigo in codigos_huffman.items():
    print(caracter, ":", codigo)

# Calcular el costo total del árbol de Huffman
costo_total = 0
for caracter, frecuencia in frecuencias.items():
    costo_total += frecuencia * len(codigos_huffman[caracter])

print("Costo total del árbol de Huffman:", costo_total)

# Comprimir el texto utilizando los códigos de Huffman
cadena_comprimida = ""
for caracter in texto:
    cadena_comprimida += codigos_huffman[caracter]

print("Cadena comprimida:", cadena_comprimida)

# Decodificar la cadena comprimida
cadena_decodificada = decodificar_cadena(cadena_comprimida, codigos_huffman)
print("Cadena decodificada:", cadena_decodificada)
