# Exercício 1: Soma total

import numpy as np
numeros = np.array([
    [10, 15, 20],
    [10, 15, 20],
    [10, 15, 20]
])
soma = np.sum(numeros)
print(soma)

# Exercício 2: Identidade

import numpy as np
n = int(input("Digite o valor de n: "))
matriz = np.eye(n)

print("Matriz identidade:")
print(matriz)

# Exercício 3: Busca simples

import numpy as np
matriz = np.array([
    [10,15,20],
    [32,47,88],
    [45,98,50]
])
numero = int(input("Digite um número: "))
if numero in matriz:
    print("Está na matriz")
else:
    print("Não está na matriz")

# Exercício 4: Troca de valores

import numpy as np
matriz = np.array([
    [20, 50],
    [30, 60]
])
print("Antes:")
print(matriz)

matriz[[0, 1]] = matriz[[1, 0]]

print("\n Depois: ")
print(matriz)

# Exercício 5: Múltiplicação por escalar

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

escalar = 2

resultado = matriz * escalar

print("Matriz resultante:")
print(resultado)

# Exercício 6: Contagem de pares

import numpy as np
Matriz = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60]
])
Numeros_Pares = np.sum(Matriz % 2 == 0)

print("Quantidade de números pares:", Numeros_Pares)

# Exercício 7: Maior elemento

import numpy as np
Matriz = np.array([
    [15, 25, 6, 11],
    [3, 7, 13, 38],
    [45, 12, 87, 22]
])
Maior = np.max(Matriz)
print(f"O maior número é: ", Maior)

# Exercício 8: Média por linha

import numpy as np
Matriz = np.array([
    [15, 35, 45],
    [20, 40, 60],
    [50, 55, 75]
])
for i in range(3):
    soma = sum(Matriz[i])
    media = soma / 3
    print(f"Média da linha {i+1}: {media}")

# Exercício 9: Soma da Diagonal Principal

import numpy as np

Matriz = np.array([
    [10, 15, 20, 25],
    [10, 15, 20, 25],
    [10, 15, 20, 25],
    [10, 15, 20, 25]
])
soma = np.trace(Matriz)

print(f"Soma da diagonal principal: {soma}")

# Exercício 10: Matriz Transposta

import numpy as np
matriz = np.array([
   [1, 2, 3],
   [4, 5, 6]
])

transposta = matriz.T

print("Matriz original:")
print(matriz)

print("Matriz transposta:")
print(transposta)

# Exercício 11: Soma de colunas

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

soma_colunas = np.sum(matriz, axis=0)

print("Soma das colunas:", soma_colunas)

# Exercício 12: Verificação de Simetria

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
])

if np.array_equal(matriz, matriz.T):
    print("A matriz é simétrica")
else:
    print("A matriz NÃO é simétrica")

# Exercício 13: Diagonal Secundária

import numpy as np

matriz = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

secundaria = np.fliplr(matriz).diagonal()

print("Diagonal secundária:", secundaria)

# Exercício 14: Multiplicação de Matrizes

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

resultado = np.dot(A, B)

print(resultado)

# Exercício 15: Rotação 90°

import numpy as np

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

rotacionada = np.rot90(matriz, -1)

print(rotacionada)