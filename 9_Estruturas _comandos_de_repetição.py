#Instruções do projeto
#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

for i in range(20,0,-1):
    if i == 13:
        print()
    else:
        print (i)

cont = 1
while cont <= 20:
    if cont == 13:
        print()
    else:
        print(cont)
    cont = cont + 1

c = 1
while True:
    if c == 21:
        break
    if c == 13:
        print()
    else:
        print(c)
    c += 1

print(*[x for x in range(20,0,-1)if x != 13 ])