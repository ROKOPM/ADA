num1 = input("Por favor ingrese el primer numero a multiplicar: ") #Se introducen los numeros a pultiplicar a mano 
num2 = input("Por favot ingrese el segundo numero a multiplicar: ") 

num1 = [int(x) for x in num1]
num2 = [int(x) for x in num2]


def multiply(num1, num2):
    
    """
    Sign se refiere a la forma en que se determinara el signo de la multiplicacion
    despues toma el valor absoluto de num1 y num2 para multiplicarlos
    y despues se crea una nueva lista que sera la suma de las longitudes de num1 y 2
    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    """
    Se usan dos for anidados para realizar la multiplicacion y se recorre dos veces para cada numero
    se multiplica uno a uno desde el numero menos significativo hasta el numero mas significativo 
    y los resultados parciales se van almacenando en result
    """
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
 #Finalmente se eliminan los 0 menos significativos de los resultados y se devuelve como una lista con el signo
 #deseado
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
result = multiply(num1, num2)
print(result) #Se toma la lista y se muestra en la pantalla

