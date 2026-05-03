# Exercício 1: Crie uma função somar(a, b) que retorne a soma de dois números

def somar(a, b):
    return a + b
resultado = somar(5, 20)
print(resultado)

# Exercício 2: Crie uma função multiplicar(a, b) que retorne o resultado da multiplicação

def multiplicar(a, b):
    return a * b
resultado = multiplicar(20, 5)
print(resultado)

# Exercício 3: Escreva uma função mensagem(nome) que imprima: Olá, <nome>!

def saudacao(nome, mensagem="Olá"):
    print(f"{mensagem}, {nome}!")
saudacao("Samara")

# Exercício 4: Crie uma função maior(a, b) que retorne o maior entre dois números

def maior(a, b):
    if a > b:
        print(a)
    elif b > a:
        print(b)
maior(5, 9)

# Exercício 5: Crie uma função dividir(a, b) que retorne o quociente e o resto da divisão

def dividir(a, b):
    quociente = a // b
    resto = a % b
    return quociente, resto
resultado = dividir(50, 3)
print(resultado)

# Exercício 6: Crie uma função par_ou_impar(n) que retorne True se for par e False caso contrário

def par_ou_impar(n):
    if n % 2 == 0:
        return(True)
    else:
        return(False)
print(par_ou_impar(2))

# Exercício 7: O que será exibido?

def teste():
    print('Olá')

resultado = teste()
print(resultado)

# Será exibido: Olá None

# Exercício 8: Crie uma função apresentar(nome, idade, cidade) que imprima os dados formatados

def apresentar(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}")

apresentar("Samara", 19, "Curitiba")

# Exercício 9: Chame a função acima usando argumentos posicionais e nomeados

# Argumentos posicionais
apresentar("Samara", 19, "Curitiba")

# Argumentos nomeados
apresentar(nome="Samara", idade=19, cidade="Curitiba")

# Exercício 10: O que acontece em: apresentar('Ana', 'Curitiba', 20)?
# Os argumentos são passados na ordem, então “Curitiba” será usado como idade e 20 como cidade. 
# O programa não dá erro, mas a saída fica incorreta: Ana tem Curitiba anos e mora em 20.

# Exercício 11: Crie uma função saudacao(nome, periodo='dia')

def saudacao(nome, periodo='dia'):
    print(f"Bom {periodo}, {nome}")
saudacao(nome= "Samara")

# Exercício 12: Modifique para aceitar valor padrão e valor informado

def saudacao(nome, periodo='dia'):
    if periodo == "":
        periodo = 'dia'
    print(f"Bom {periodo}, {nome}")
saudacao(nome= "Samara")
saudacao("Samara", input("determine o periodo: "))

# Exercício 13: Explique o erro em: def exemplo(a=1, b):
# O erro ocorre porque os parâmetros com valores padrão devem ser definidos após os parâmetros 
# sem valores padrão.

# Exercício 14: Crie uma função somar_todos(*numeros)

def somar_tudo(*args):
    return sum(args)
print(somar_tudo(5,15, 20, 30))

# Exercício 15: Crie uma função mostrar_dados(**dados)

def mostrar_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

mostrar_dados(nome="Ana", idade=20, cidade="Curitiba")

# Exercício 16: Explique a diferença entre *args e **kwargs
# *args e **kwargs permitem passar um número variável de argumentos para uma função:
# *args → captura múltiplos valores posicionais em uma tupla
# **kwargs → captura múltiplos argumentos nomeados em um dicionário

# Exercício 17: O que será exibido?

x = 10
def teste():
    x = 5
    print(x)

teste()
print(x)

# Será exibido: 5 10

# Exercício 18: Corrija:
# contador = 0
#def incrementar():
#contador += 1

contador = 0

def incrementar():
    global contador
    contador += 1

# É necessário usar global para modificar a variável contador dentro da função.


# Exercício 19: Crie uma função triplo(x) e atribua a uma variável

def triplo(x):
    return x * 3
operacao = triplo
print(operacao(3))

# Exercício 20: Crie executar(funcao, valor)

def executar(funcao, valor):
    return funcao(valor)
print(executar(triplo, 3))

# Exercício 21: Reescreva quadrado(x) usando lambda

quadrado = lambda x: x ** 2
print(quadrado(3))

# Exercício 22: Use map para dobrar [1,2,3,4,5]

numeros =[1, 2, 3, 4, 5]
dobrados=list(map(lambda x: x ** 2, numeros))
print(dobrados)

# Exercício 23: Use filter para pares

numeros=[1, 2, 3, 4, 5]
pares=list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

# Exercício 24: Crie uma função fatorial recursiva

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)
print(fatorial(10))

# Exercício 25: Crie contagem recursiva de n até 0

def contagem(n):
    if n == 0:
        print("Fim!")
    else:
        print(n)
        contagem(n - 1)
contagem(5)

# Exercício 26: Explique o erro: def erro(n): return n * erro(n - 1)
# O erro ocorre porque a função chama a si mesma sem uma condição de parada, 
# resultando em recursão infinita e eventualmente causando um erro de estouro de pilha (RecursionError).

# Exercício 27: Crie função media(lista) com docstring

def media(lista):
    """
    Calcula a média dos valores de uma lista.

    Parâmetros:
    lista (list): lista de números

    Retorna:
    float: média dos valores
    """
    return sum(lista) / len(lista)

# Exercício 28: Use help() para exibir a documentação

def media(lista):
    """
    Calcula a média dos valores de uma lista.

    Parâmetros:
    lista (list): lista de números

    Retorna:
    float: média dos valores
    """
    return sum(lista) / len(lista)

help(media)

# Exercício 29: Crie calculadora(a, b, operacao)

def calculadora(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b
    else:
        return "Operação inválida"

# Exercício 30: Crie processar_dados(*args, **kwargs)

def processar_dados(*args, **kwargs):
    print("Argumentos posicionais:", args)
    print("Argumentos nomeados:", kwargs)