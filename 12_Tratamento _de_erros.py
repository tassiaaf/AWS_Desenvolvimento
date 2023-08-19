# Instruções do projeto
# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

while True:
    try:
        nome = input('Digite seu nome completo: ')
        ano_nasc = int(input('Digite o ano do seu nascimento: '))
        idade = 2022 - ano_nasc

        if ano_nasc >= 1922 and ano_nasc <= 2021:
            print ('Usuário: ', nome)
            print ('Idade: ', idade)
        else:
            print ('Digite um ano entre 1922 e 2021')
            continue
    except Exception as error:
        print(error)
        continue
    break