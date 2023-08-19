# Instruções do projeto
# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão

# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.



def calculadora(num1, num2, op):
    res = 0
    if op == 1:
        res = num1 + num2
    elif op == 2:
        res = num1 - num2
    elif op == 3:
        res = num1 * num2
    elif op == 4 and num2 != 0:
        res = num1 / num2
    else:
        res = 0
    return res
    
