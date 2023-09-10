lista_produtos = ['a','b','c']

while True:
    print('Sistema de controle de estoque')
    print()
    print('1-Lista de produtos\n2-Adicionar produtos\n3-Alterar produto\n4-Sair')
    opcao = int(input('Digite a opção desejada: '))
    print('--'*30)


    if opcao == 1:
        print('Lista de produtos:')
        print()
        for i in lista_produtos:
            print(i)
            
    elif opcao == 2:
        lista_produtos.append(input('Digite o nome do produto para adicionar a lista: '))
        for i in lista_produtos:
            print(i)
            

    elif opcao == 3:
        print(*lista_produtos)
        lista_produtos.remove(input('Digite um item da lista para remover: '))
       

    elif opcao == 4:
        print('Saindo...')      
        break
    
    else:
        print('Opcão desconhecida, digite uma das opções validas!')
        



