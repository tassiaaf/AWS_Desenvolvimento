# Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

# 1: Soma
# 2: Subtração
# 3: Multiplicação
# 4: Divisão
# 0: Sair

# Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

# Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar.

# É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.
# Recursos

def calculadora():
    while True:
        print ('1: Soma\n2: subtração\n3: Multiplicação\n4: Divisão\n')

        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        op = int (input('Digite o número correspondente a operação: '))
       
        if op == 1:
            res = num1 + num2
        elif op == 2:
            res = num1 - num2
        elif op == 3:
            res = num1 * num2
        elif op == 4 and num2 != 0:
            res = num1 / num2
        else:
            res = 'Essa opção não existe'
        print (res)
        resp = input('Continuar? [S] para sim e [N] para não!')
        if resp in 'Nn':
            print('Saindo...')
            break
            
calculadora()
