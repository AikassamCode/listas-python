# Exercício 1: Votação

idade=int(input("Digite sua idade: "))
if idade>=16:
    print("Você ja pode votar!")

# Exercício 2: Positivo, Negativo ou Zero

numero=int(input("Digite um número: "))
if numero>0:
    print("O número é positivo")
elif numero<0:
    print("O número é negativo")
else:
    print("O número é 0")

# Exercício 3: Desconto do Cliente

valor=float(input("Digite o valor total da compra: "))
if valor>100:
    desconto=valor*0.10
    final=valor-desconto
    print("Valor com desconto:", final)
else:
    print("Valor normal:", valor)
    print("Nas compras acima de R$100 reais, você ganha 10% de desconto!")

# Exercício 4: Sistema de notas

nota=float(input("Digite a nota do aluno: "))
if nota>= 9.0:
    print("Parabéns!! você foi aprovado!")
elif nota >= 7.0:
    print("Aprovado")
elif nota >= 4.0:
    print("Em recuperação")
else:
    print("Reprovado")

# Exercício 5: Verificar se o número é par ou ímpar

numero=int(input("Digite um número:"))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Exercício 6: Comparando dois números

n1=float(input("Digite número 1: "))
n2=float(input("Digite número 2:"))
if n1>n2:
    print("n1 é maior que n2")
elif n1<n2:
    print("n1 é menor que n2")
else:
    print("n1 é igual a n2")

# Exercício 7: Verificação de login

usuario_correto="admin"
usuario=input("Digite um nome de usuário:")
if usuario==usuario_correto:
    print("Acesso concedido")
else:
    print("Usuário desconhecido")

# Exercício 8: Calculadora de IMC Simples

peso=float(input("Digite o seu peso: "))
altura=float(input("Digite sua altura: "))
imc= peso/ (altura**2)
if imc > 25:
    print("Acima do peso ideal")
else:
    print("Peso dentro da normalidade")

# Exercício 9: Classificação de triângulos

a=float(input("Lado A: "))
b=float(input("Lado B: "))
c=float(input("Lado C: "))
if a == b and b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")

# Exercício 10: Múltiplo de 5

numero=int(input("Digite um número: "))
if numero % 5 == 0:
    print("É múltiplo de 5")
else:
    print("Não é múltiplo de 5")

# Exercício 11: Categorias de atletas

idade=int(input("Digite sua idade: "))
if 5 >= idade <= 7:
    print("Infantil A")
elif 8 >= idade <= 10:
    print("Infantil B")
elif 11 >= idade <= 13:
    print("Juvenil 1")
elif 14 >= idade <= 17:
    print("Juvenil 2")
elif idade >18:
    print("Adulto")

# Exercício 12: Calculadora de viagem

km=float(input("Digite a distância em km a percorrer:"))
if km <=200:
    preco = km * 0.50
else:
    preco = km * 0.45
print("Preço:", preco)

# Exercício 13: Verificar se um ano é bissexto

ano=int(input("Digite um ano: "))
if ano % 4 == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")

# Exercício 14: Aumento salarial

salario=float(input("Digite o seu salario: "))
if salario > 1621:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
    print("Novo salário:", salario + aumento)

# Exercício 15: Simulador de radar

velocidade=float(input("Digite o valor da velocidade: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Multa:", multa)
else:
    print("Dentro do limite")

# Exercício 16: Conversor de temperatura

c = float(input("Digite a temperatura em Celsius: "))
opcao = (input("Converter para (F) ou (K)? "))
if opcao == 'F':
    res = (c * 9/5) + 32
    print(f"{res} °F")

elif opcao == "K":
    res = c + 273.15
    print(f"{res}K")
else:
  print("Opção inválida!")

# Exercício 17: Loja de tintas

area=float(input("Área(m²): "))
litros = area / 3
latas = litros / 18
if latas <= 1:
   print("Precisa de 1 lata")
else:
   print("Precisa de mais de uma lata")

# Exercício 18: Aprovação de Empréstimo

casa=float(input("Valor da casa: "))
salario=float(input("Salário: "))
anos=int(input("Anos: "))
prestacao = casa / (anos * 12)

if prestacao <= salario * 0.30:
   print("Empréstimo aprovado")
else:
   print("Empréstimo negado")