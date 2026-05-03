# Exercício 1:

pessoa = {
    "nome": "Ana",
    "idade": 20,
    "cidade": "Curitiba"
}

chave = input("Digite a chave (nome, idade, cidade): ")

if chave in pessoa:
    print("Valor:", pessoa[chave])
else:
    print("Chave não encontrada")

# Exercício 2:

produtos = {
    "arroz": 20.0,
    "feijao": 8.5,
    "leite": 5.0
}

produto = input("Qual produto deseja alterar? ")
novo_preco = float(input("Digite o novo preço: "))

if produto in produtos:
    produtos[produto] = novo_preco
    print("Dicionário atualizado:", produtos)
else:
    print("Produto não encontrado")

# Exercício 3:

dados = {}

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

dados[nome] = idade

print("Dicionário:", dados)
print("Dicionário:", dados)

# Exercício 4:

dados = dict()

for i in range(3):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor {i+1}: ")
    dados[chave] = valor

print("Dicionário:", dados)

# Resultado:
# Digite a chave 1: nome
# Digite o valor 1: Ana
# Digite a chave 2: idade
# Digite o valor 2: 18
# Digite a chave 3: cidade
# Digite o valor 3: Curitiba

# Exercício 5:

dados = {
    "nome": "Ana",
    "idade": 20,
    "cidade": "Curitiba"
}

resposta = input("Deseja apagar todos os dados? (sim/não): ")

# Exercício 6:

original = {
    "nome": "Ana",
    "idade": 20
}

copia = original.copy()

copia["idade"] = 30

print("Original:", original)
print("Cópia:", copia)

# Exercício 7:

nomes = input("Digite nomes separados por vírgula: ")

lista_nomes = nomes.split(",")

dicionario = dict.fromkeys(lista_nomes, 0)

print("Dicionário:", dicionario)

# Exercício 8:

alunos = {
    "Ana": 8.5,
    "João": 7.0,
    "Maria": 9.0
}

nome = input("Digite o nome do aluno: ")

nota = alunos.get(nome, "Aluno não encontrado")

print("Resultado:", nota)

# Exercício 9:

produtos = {
    "arroz": 20,
    "feijao": 8,
    "leite": 5
}

print("Chaves:", produtos.keys())
print("Valores:", produtos.values())
print("Itens:", produtos.items())

# Exercício 10:

dados = {
    "nome": "Ana",
    "idade": 20,
    "cidade": "Curitiba"
}

chave = input("Digite a chave para remover: ")

removido = dados.pop(chave, "Chave não encontrada")
print("Removido:", removido)

item = dados.popitem()
print("Item removido com popitem():", item)

nova_chave = input("Digite uma nova chave: ")
novo_valor = input("Digite o valor: ")

dados.update({nova_chave: novo_valor})

print("Dicionário final:", dados)

# Exercício 11:

usuarios = {
    "Ana": 20,
    "João": 25,
    "Maria": 22
}

while True:
    print("\n1-Exibir 2-Buscar 3-Adicionar 4-Atualizar")
    print("5-Remover 6-Popitem 7-Copiar")
    print("8-Fromkeys 9-Update 10-Clear 11-Dict 0-Sair")

    op = input("Opção: ")

    if op == "1":
        print("Nomes:", list(usuarios.keys()))
        print("Idades:", list(usuarios.values()))
        print("Dados:", list(usuarios.items()))

    elif op == "2":
        nome = input("Nome: ")
        print(usuarios.get(nome, "Não encontrado"))

    elif op == "3":
        usuarios[input("Nome: ")] = int(input("Idade: "))

    elif op == "4":
        nome = input("Nome: ")
        if nome in usuarios:
            usuarios[nome] = int(input("Nova idade: "))

    elif op == "5":
        print(usuarios.pop(input("Nome: "), "Não encontrado"))

    elif op == "6":
        if usuarios:
            print(usuarios.popitem())

    elif op == "7":
        copia = usuarios.copy()
        nome = input("Alterar na cópia: ")
        if nome in copia:
            copia[nome] = int(input("Nova idade: "))
        print("Original:", usuarios)
        print("Cópia:", copia)

    elif op == "8":
        nomes = input("Nomes: ").split(",")
        idade = int(input("Idade padrão: "))
        usuarios = dict.fromkeys(nomes, idade)

    elif op == "9":
        novos = {}
        for _ in range(2):
            n = input("Nome: ")
            i = int(input("Idade: "))
            novos[n] = i
        usuarios.update(novos)

    elif op == "10":
        if input("Limpar tudo? (sim/não): ").lower() == "sim":
            usuarios.clear()

    elif op == "11":
        pares = []
        for _ in range(2):
            pares.append((input("Chave: "), input("Valor: ")))
        usuarios = dict(pares)

    elif op == "0":
        break