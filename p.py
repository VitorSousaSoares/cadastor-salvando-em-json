import json


def adicionar():

    dado = {}

    cadNome = input("Digite o nome ")

    cadIdade = input("Digite a idade ")

    dado["Nome"] = cadNome

    dado["Idade"] = cadIdade

    return dado


print("---------- Menu app Cadastro ---------")
print("O que voçê dezeja fazer:")
print("1 - Adicionar")
print("2 - Editar")
print("3 - Excluiur")
print("4 - Buscar")
print("5 - A dicionar iformações")
print("6 - Ezibir tudo")
print("--------------------------------------")

op = input("Digite uma opção: ")

if op == "1":
    dado = adicionar()

    with open('J.json') as f:
        cadastro = json.load(f)

    for i in cadastro:
        ultimoCadastro = i

    id = 1 + int(ultimoCadastro)

    cadastro[id] = dado

    add = json.dumps(cadastro, indent=1)

    with open('J.json', "w") as f:
        f.write(add)
        f.close()

elif op == "2":
    with open('J.json') as f:
        cadastro = json.load(f)

    opId = input("Digite o id para alterar: ")

    print(cadastro[opId])

    print("Oque dezeja alterar:")
    print("1 - Nome")
    print("2 - Idade")

    opAlterar = input("? ")

    novoValor = input("Digite o novo valor: ")

    if opAlterar == "1":
        cadastro[opId]["Nome"] = novoValor
    else:
        cadastro[opId]["Idade"] = novoValor

    edit = json.dumps(cadastro, indent=1)

    with open('J.json', "w") as f:
        f.write(edit)
        f.close()

elif op == "3":
    with open('J.json') as f:
        cadastro = json.load(f)

    idDelete = input("Digite o id para deleyar: ")

    del cadastro[idDelete]

    delet = json.dumps(cadastro, indent=1)

    with open('J.json', "w") as f:
        f.write(delet)
        f.close()

elif op == "4":
    with open('J.json') as f:
        cadastro = json.load(f)

    busca = input("Digite o id para vizualizar: ")

    print(cadastro[busca])

elif op == "5":
    with open('J.json') as f:
        cadastro = json.load(f)

    opId = input("Digite o id para adiciona: ")
    print(cadastro[opId])

    NovoItem = input("Digite o titulo do item: ")

    ValorItem = input("Digite o Item: ")

    cadastro[opId][NovoItem] = ValorItem

    Novo = json.dumps(cadastro, indent=1)

    with open('J.json', "w") as f:
        f.write(Novo)
        f.close()


else:
    with open('J.json') as f:
        cadastro = json.load(f)

    print(cadastro)
