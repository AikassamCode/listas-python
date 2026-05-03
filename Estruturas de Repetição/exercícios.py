# Exercício 1: Some os números de 1 a 10
soma = 0
for i in range(1, 11):
    soma += i
print("Soma de 1 a 10:", soma)

# Exercício 2: Mostre apenas números pares de 1 a 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercício 3: Leia 5 números e calcule a média
soma = 0
for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    soma += n
print(f"Média: {soma/5:.2f}")

# Exercício 4: Conte quantos números negativos foram digitados
negativos = 0
for i in range(5):
    n = int(input(f"Digite o {i+1}º número: "))
    if n < 0:
        negativos += 1
print(f"Quantidade de negativos: {negativos}")

# Exercício 5: Leia números até digitar 0 e calcule soma
soma = 0
while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    soma += n
print(f"Soma: {soma}")

# Exercício 6: Leia 10 números e conte quantos são maiores que 5
maiores = 0
for i in range(10):
    n = int(input(f"Digite o {i+1}º número: "))
    if n > 5:
        maiores += 1
print(f"Números maiores que 5: {maiores}")

# Exercício 7: Leia números até negativo e conte pares
pares = 0
while True:
    n = int(input("Digite um número (negativo para parar): "))
    if n < 0:
        break
    if n % 2 == 0:
        pares += 1
print(f"Quantidade de pares: {pares}")

# Exercício 8: Calcule o fatorial de um número
n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"{n}! = {fatorial}")

# Exercício 9: Mostre a tabuada de um número
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Exercício 10: Leia 5 notas e informe quantas são >= 7
aprovadas = 0
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    if nota >= 7:
        aprovadas += 1
print(f"Notas >= 7: {aprovadas}")