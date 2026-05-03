# Exercício 1: Cadastro de números inteiros

a = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    a.append(numero)

# Exercício 2: Exibição de elementos da lista

print("Elementos da lista: ")

for valor in a:
    print(valor)

# Exercício 3: Maior e menor valor

a = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    a.append(numero)

maior = max(a)
menor = min(a)

print("\nMaior valor:", maior)
print("Menor valor:", menor)

# Exercício 4: nálise de notas de alunos

notas = []

quantidade = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade):
    nota = int(input(f"Digite a nota do aluno {i+1} (0 a 100): "))
    notas.append(nota)

abaixo_media = 0
na_media_ou_acima = 0

for nota in notas:
    if nota < 60:
        abaixo_media += 1
    else:
        na_media_ou_acima += 1

print("\nResultados:")
print("Alunos abaixo da média:", abaixo_media)
print("Alunos na média ou acima:", na_media_ou_acima)

# Exercício 5: Análise de números inteiros

numeros = []

for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    numeros.append(n)

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
somatorio = sum(numeros)
media = somatorio / len(numeros)

print(f"\nMaior número par: {max(pares)}" if pares else "\nNão há números pares na lista.")
print(f"Menor número ímpar: {min(impares)}" if impares else "Não há números ímpares na lista.")
print(f"Somatório: {somatorio}")
print(f"Média: {media:.2f}")