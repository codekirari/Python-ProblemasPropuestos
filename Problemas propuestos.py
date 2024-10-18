# import random



# -------------- Problemas propuestos --------------
# ----------------------------
# 
# 
# 1.	Calcular el promedio de 50 valores almacenados en un vector. Determinar, además cuantos son mayores que el promedio, imprimir el promedio, el número de datos mayores que el promedio y una lista de valores mayores que el promedio.

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#         11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#         21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#         31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#         41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# # Calcular el promedio
# promedio = sum(valores) / len(valores)

# # Determinar los valores mayores que el promedio
# mayores_que_promedio = [valor for valor in valores if valor > promedio]

# # Imprimir los resultados
# print(f"Promedio: {promedio}")
# print(f"Número de valores mayores que el promedio: {len(mayores_que_promedio)}")
# print(f"Valores mayores que el promedio: {mayores_que_promedio}")

# ****************************************************************

# 2.	Llenar dos vectores A y B de 45 elementos cada uno, sumar el elemento uno del vector A con el elemento uno del vector B y así sucesivamente hasta 45, almacenar el resultado en un vector C, e imprimir el vector resultante.


# Llenar los vectores A y B con 45 elementos aleatorios cada uno
# A = [i for i in range(1, 46)]  # Llenamos A con los números del 1 al 45
# B = [i for i in range(46, 91)]  # Llenamos B con los números del 46 al 90

# # Paso 2: Crear el vector C sumando los elementos de A y B
# C = []
# for i in range(45): 
#     suma = A[i] + B[i]  
#     C.append(suma)  

# # Paso 3: Imprimir el vector C resultante
# print("Vector C resultante:", C)

# ****************************************************************

# 3. Llenar un vector de 20 elementos, imprimir la posición y el valor del elemento mayor almacenado en el vector. Suponga que todos los elementos del vector son diferentes.

# # Llenar el vector con 20 elementos
# vector = [i for i in range(1, 21)]  # Llenamos el vector con los números del 1 al 20

# # Encontrar el valor máximo y su posición
# max_valor = max(vector)
# posicion_max = vector.index(max_valor)

# # Imprimir la posición y el valor del elemento mayor
# print(f"Posición del elemento mayor: {posicion_max}")
# print(f"Valor del elemento mayor: {max_valor}")

# ****************************************************************
# 4. Almacenar 500 números en un vector, elevar al cuadrado cada valor almacenado en el vector, almacenar el resultado en otro vector. Imprimir el vector original y el vector resultante.

# Llenar el vector con 500 números
# vector_original = [i for i in range(1, 501)]

# # Elevar al cuadrado cada valor almacenado en el vector
# vector_cuadrado = [x**2 for x in vector_original]

# # Imprimir el vector original y el vector resultante
# print("Vector original:", vector_original)
# print("Vector resultante (cuadrados):", vector_cuadrado)

# ****************************************************************

# 5. Almacenar 300 números en un vector, imprimir cuantos son ceros, cuantos son negativos, cuantos positivos. Imprimir además la suma de los negativos y la suma de los positivos.


import random

# 1. Crear un vector con 300 números (aleatorios entre -100 y 100)
vector = [random.randint(-100, 100) for _ in range(300)]

# 2. Usar listas separadas para almacenar ceros, negativos y positivos
vector_ceros = [num for num in vector if num == 0]
vector_negativos = [num for num in vector if num < 0]
vector_positivos = [num for num in vector if num > 0]

# 3. Calcular la suma de los negativos y de los positivos
suma_negativos = sum(vector_negativos)
suma_positivos = sum(vector_positivos)

# 4. Imprimir los resultados
print(f"Número de ceros: {len(vector_ceros)}")
print(f"Número de negativos: {len(vector_negativos)}")
print(f"Número de positivos: {len(vector_positivos)}")
print(f"Suma de los números negativos: {suma_negativos}")
print(f"Suma de los números positivos: {suma_positivos}")


# ****************************************************************




# 6. Almacenar 150 números en un vector, almacenarlos en otro vector en orden inverso al vector original e imprimir el vector resultante.

# Llenar el vector con 150 números
vector_original = [i for i in range(1, 151)]

# Almacenar los números en otro vector en orden inverso
vector_inverso = vector_original[::-1]

# Imprimir el vector resultante
print("Vector original:", vector_original)
print("Vector inverso:", vector_inverso)


# ****************************************************************



# 7. Se tienen almacenados en la memoria dos vectores M y N de cien elementos cada uno. Hacer un algoritmo que escriba la palabra “Iguales” si ambos vectores son iguales y “Diferentes” si no lo son.

# Llenar los vectores M y N con 100 elementos
M = [i for i in range(1, 101)]  # Llenamos M con los números del 1 al 100
N = [i for i in range(1, 101)]  # Llenamos N con los números del 1 al 100

# Comparar los vectores
if M == N:
    print("Iguales")
else:
    print("Diferentes")


# Serán iguales cuando en la misma posición de ambos vectores se tenga el mismo valor para todos los elementos.

# ****************************************************************

# 8. Se tiene el vector A con 100 elementos almacenados. Diseñe un algoritmo que escriba “SI” si el vector esta ordenado ascendentemente o “NO” si el vector no está ordenado

# Llenar el vector A con 100 elementos
A = [i for i in range(1, 101)]  # Llenamos A con los números del 1 al 100

# Verificar si el vector está ordenado ascendentemente
if A == sorted(A):
    print("SI")
else:
    print("NO")

# ****************************************************************

# 9. Diseñe un algoritmo que lea un número cualquiera y lo busque en el vector X, el cual tiene almacenados 80 elementos. Escribir la posición donde se encuentra almacenado el número en el vector o el mensaje “NO” si no lo encuentra. Búsqueda secuencial.

# Llenar el vector X con 80 elementos
X = [i for i in range(1, 81)]  # Llenamos X con los números del 1 al 80

# Leer un número cualquiera
numero = int(input("Ingrese un número a buscar en el vector X: "))

# Búsqueda secuencial
encontrado = False
for i in range(len(X)):
    if X[i] == numero:
        print(f"El número {numero} se encuentra en la posición {i}")
        encontrado = True
        break

if not encontrado:
    print("NO")


# ****************************************************************


# 10. Diseñe un algoritmo que lea dos vectores A y B de 20 elementos cada uno y multiplique el primer elemento de A con el último elemento de B y luego el segundo elemento de A por el diecinueveavo elemento de B y así sucesivamente hasta llegar al veinteavo elemento de A por el primer elemento de B. El resultado de la multiplicación almacenarlo en un vector C.

# Llenar los vectores A y B con 20 elementos
A = [i for i in range(1, 21)]  # Llenamos A con los números del 1 al 20
B = [i for i in range(21, 41)]  # Llenamos B con los números del 21 al 40

# Crear el vector C con el resultado de las multiplicaciones
C = [A[i] * B[19 - i] for i in range(20)]

# Imprimir el vector resultante C
print("Vector A:", A)
print("Vector B:", B)
print("Vector C (resultado de las multiplicaciones):", C)


# ****************************************************************
