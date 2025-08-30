contatos = []

def adicionar_contato(lista, nome):
    lista.append(nome)

def remover_contatos (lista, nome):
    lista.remove(nome)

def buscar_contatos (lista, nome):
    return lista.index(nome)

def mostrar_contatos (lista):
     for i, contatos in enumerate(lista):
        print(f'{i+1}. {contatos}')
    
while True:

    print('=== MENU ===')
    print('1 - Adicionar contato')
    print('2 - Remover contato')
    print('3 - Buscar contato')
    print('4 - Mostrar contatos')
    print('5 - Sair')
    
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        while True:
            nome = input('Digite o nome do contato e -> sair <- para voltar ao menu: ')
            if nome == 'sair':
                break
            try:
                if nome.strip() == '':
                    raise ValueError ('Você não pode inserir um contato vázio')
                adicionar_contato(contatos, nome)
                print(f'O contato {nome} foi adicionado com sucesso!')
                
            except ValueError as e:
                print(f'Erro: {e}')
                
    elif opcao == '2':
        nome = input('Digite o nome do contato que deseja remover: ')     

        try:
            remover_contatos(contatos, nome)
            print('O contato foi removido!')

        except (ValueError, IndexError):
            print('O contato não está na lista!')
    
    elif opcao == '3':
        nome = input('Digite o nome do contato que deseja buscar: ')

        try: 
            posicao = buscar_contatos(contatos, nome)
            buscar_contatos(contatos, nome)
            print(f'o contato {nome} esta posição na {posicao+1}')
        except ValueError:
            print(f'O contato não foi encontrado!')
    
    elif opcao == '4':
        if not contatos:
            print('Não existe nenhum contato na lista')
        else:
            mostrar_contatos(contatos)

    elif opcao == '5':
        print('Saindo...')
        break