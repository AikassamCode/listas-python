# Exercício 1: Crie uma lista com os números de 1 a 5 e imprima-a na tela

numeros = [1, 2, 3, 4, 5]
print(numeros)

# Exercício 2: Dada a lista cores = ['vermelho', 'azul', 'verde', 'amarelo']
# acesse e imprima a segunda cor da lista.

cores = ['vermelho', 'azul', 'verde', 'amarelo']
print(cores[1])

# Exercício 3: Adicione o número 10 ao final da lista numeros = [1, 2, 3]

numeros = [1, 2, 3]
numeros.append(10)
print(numeros)

# Exercício 4: Remova a palavra "banana" da lista frutas = ['maçã', 'banana', 'laranja']

frutas = ['maçã', 'banana', 'laranja']
frutas.remove('banana')
print(frutas)

# Exercício 5: Encontre e imprima o tamanho (quantidade de elementos) da lista itens = [10,20,30,40,50]

itens = [10, 20, 30, 40, 50]
print(len(itens))

# Exercício 6: Verifique se o número 7 está presente na lista valores = [1, 3, 5, 7, 9] 
# e imprima o resultado booleano

valores = [1, 3, 5, 7, 9]
print(7 in valores)

# Exercício 7: Concatene as listas lista1 = [1, 2] e lista2 = [3, 4] em uma terceira lista

lista1 = [1, 2]
lista2 = [3, 4]
lista3 = lista1 + lista2
print(lista3)

# Exercício 8: Inverta a ordem dos elementos da lista letras = ['a', 'b', 'c', 'd']

letras = ['a', 'b', 'c', 'd']
letras.reverse()
print(letras)

# Exercício 9: Conte quantas vezes o número 2 aparece na lista numeros = [1, 2, 2, 3, 2, 4]

numeros = [1, 2, 2, 3, 2, 4]
print(numeros.count(2))

# Exercício 10: Calcule e imprima a soma de todos os elementos da lista precos = [10.5, 20.0, 15.5]

precos = [10.5, 20.0, 15.5]
print(sum(precos))

# Exercício 11: Escreva um programa que remova as duplicatas de uma lista 
# garantindo que a ordem original dos primeiros elementos encontrados seja mantida

def remover_duplicatas(lista):
    vistos = []
    for item in lista:
        if item not in vistos:
            vistos.append(item)
    return vistos

print(remover_duplicatas([1, 2, 2, 3, 1, 4]))

# Exercício 12: Encontre o maior e o menor número em uma lista de inteiros 
# sem usar as funções nativas max() e min()

def maior_menor(lista):
    maior = menor = lista[0]
    for n in lista:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    return maior, menor

print(maior_menor([3, 1, 4, 1, 5, 9, 2, 6]))

# Exercício 13: Use list comprehension (compreensão de listas) para criar uma lista 
# contendo os quadrados dos números de 1 a 10

quadrados = [x**2 for x in range(1, 11)]
print(quadrados)

# Exercício 14: Dada uma lista mista de números, crie uma nova lista 
# contendo apenas os números ímpares da lista original

mistos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = [x for x in mistos if x % 2 != 0]
print(impares)

# Exercício 15: Escreva um programa que rotacione os elementos de uma lista para a direita em n posições 
# (Exemplo: a lista [1, 2, 3, 4, 5] com n=2 vira [4, 5, 1, 2, 3])

def rotacionar(lista, n):
    n = n % len(lista)
    return lista[-n:] + lista[:-n]

print(rotacionar([1, 2, 3, 4, 5], 2))

# Exercício 16: Dadas duas listas, encontre a interseção entre elas 
# (os elementos que estão presentes em ambas) sem usar a conversão para conjuntos (set)

def intersecao(lista1, lista2):
    return [x for x in lista1 if x in lista2]

print(intersecao([1, 2, 3, 4], [2, 4, 6]))

# Exercício 17: "Achate" (flatten) uma lista de listas (uma matriz bidimensional) 
# em uma única lista unidimensional (Exemplo: [[1, 2], [3, 4]] vira [1, 2, 3, 4])

def achatar(matriz):
    return [item for sublista in matriz for item in sublista]

print(achatar([[1, 2], [3, 4], [5, 6]]))

# Exercício 18:  Implemente o algoritmo de ordenação Merge Sort (Ordenação por Mistura)
#para ordenar uma lista desordenada de números em ordem crescente

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esq = merge_sort(lista[:meio])
    dir = merge_sort(lista[meio:])
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
    return resultado + esq[i:] + dir[j:]

print(merge_sort([5, 2, 8, 1, 9, 3]))

# Exercício 19: Dada uma lista de números inteiros (positivos e negativos)
# encontre a sublista contígua com a maior soma e retorne o valor dessa soma (Algoritmo de Kadane)

def kadane(lista):
    maior_soma = soma_atual = lista[0]
    for n in lista[1:]:
        soma_atual = max(n, soma_atual + n)
        maior_soma = max(maior_soma, soma_atual)
    return maior_soma

print(kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# Exercício 20: Escreva uma função recursiva que receba uma lista de números distintos 
# e retorne todas as permutações possíveis de seus elementos

def permutacoes(lista):
    if len(lista) <= 1:
        return [lista]
    resultado = []
    for i, elem in enumerate(lista):
        resto = lista[:i] + lista[i+1:]
        for p in permutacoes(resto):
            resultado.append([elem] + p)
    return resultado

print(permutacoes([1, 2, 3]))