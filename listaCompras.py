lista_compras = []

def adicionar_item(lista, item):
    lista.append(item)

def mostrar_lista(lista):
    print(lista)

while True:
    item = input('Digite um item para adicionar á lista e depois escreva -> sair <- para finalizar: ')
    if item == "sair":
        break

    try:
        float(item)
        print("O item nao pode ser um numero. Tente de novo!")
        continue

    except ValueError:
        adicionar_item(lista_compras, item)

mostrar_lista(lista_compras)