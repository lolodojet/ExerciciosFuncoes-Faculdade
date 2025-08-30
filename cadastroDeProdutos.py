produtos = []

def adicionar_produtos(lista, nome, preco):
    produto = {'id': len(lista) + 1, 'nome': nome, 'preco': preco}
    lista.append(produto)

def mostrar_produtos(lista):
    for produto in lista:
        print(f"ID: {produto['id']} - Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}")

def alterar_produtos(lista, id, novo_nome, novo_preco):
    for produto in lista:
        if produto['id'] == id:
            produto['nome'] = novo_nome   
            produto['preco'] = novo_preco
            return
    raise ValueError('Produto com esse ID não existe.')

while True:
    print("=== MENU ===")
    print("1. Adicionar produto")
    print("2. Mostrar produtos")
    print("3. Alterar produto")
    print("4. Sair")

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        while True:
            nome = input('Digite o nome do produto e depois -> sair <- para voltar ao menu: ')
            if nome.lower() == 'sair':
                break
            try:
                if nome.strip() == '':
                    raise ValueError('O nome do produto não pode ser vazio!')
                
                preco = float(input('Digite o preço do produto: '))

                adicionar_produtos(produtos, nome, preco)
                print(f'O produto {nome} foi adicionado com sucesso!')

            except ValueError as e:
                print(f'Erro: {e}')
    
    elif opcao == '2':
        if not produtos:
            print('Nenhum produto na lista')
        else:
            mostrar_produtos(produtos)
    
    elif opcao == '3':
        try: 
            id = int(input('Digite o ID do produto que você quer alterar: '))
            novo_nome = input('Digite o nome do produto: ')  

            if novo_nome.strip() == '':
                raise ValueError('Nome não pode ser vazio')
            
            novo_preco = float(input('Digite o novo preço do produto: '))
            alterar_produtos(produtos, id, novo_nome, novo_preco)
            print(f'O produto ID {id} foi alterado com sucesso!')

        except ValueError as e:
            print(f'Erro: {e}')
    
    elif opcao == '4':
        print('Saindo...')
        break