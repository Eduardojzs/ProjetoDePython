"""
Exercício Operações Matemáticas Básicas

Objetivo: Desenvolver um programa que solicite ao usuário a entrada
de dois números e, com base nesses números, realize as seguintes operações:

    1. Calcular e mostrar a soma dos dois números.
    
    2. Calcular e mostrar a subtração do primeiro número pelo segundo.
    
    3. Calcular e mostrar a multiplicação dos dois números.
    
    4. Calcular e mostrar a divisão do primeiro número pelo 
    segundo (se o segundo número não for zero).
    
    5. Verificar e informar se algum dos números (ou ambos) é zero.
    
    6. Calcular e mostrar a média dos dois números.
    
    7. Comparar os dois números e informar qual é maior ou se são iguais.
    
"""
# Solicita dois números ao usuário
num1 = float(input("Por favor, digite o primeiro número: "))
num2 = float(input("Por favor, digite o segundo número: "))

#1. Calcular e mostrar a soma dos dois números.

# Calcula e imprime a soma
soma = num1 + num2
print(f"\nA soma dos números {num1} e {num2} é: {soma}")

#----------------------------------

#2. Calcular e mostrar a subtração do primeiro número pelo segundo.

# Calcula e imprime a subtração
subtracao = num1 - num2
print(f"A subtração do número {num1} pelo {num2} é: {subtracao}")

#----------------------------------

#3. Calcular e mostrar a multiplicação dos dois números.

# Calcula e imprime a multiplicação
multiplicacao = num1 * num2
print(f"A multiplicação dos números {num1} e {num2} é: {multiplicacao}")

#----------------------------------

"""
4. Calcular e mostrar a divisão do primeiro número pelo 
    segundo (se o segundo número não for zero).
"""

# Verifica se o segundo número é zero antes de tentar dividir
if num2 != 0:
    divisao = num1 / num2
    print(f"A divisão do número {num1} pelo {num2} é: {divisao:.2f}")
else:
    print(f"Não é possível dividir {num1} por zero.")
    
#----------------------------------

#5. Verificar e informar se algum dos números (ou ambos) é zero.

if num1 == 0:
    print(f"O primeiro número informado é zero.")
if num2 == 0:
    print(f"O segundo número informado é zero.")
if num1 == 0 and num2 == 0:
    print(f"Ambos os números são iguais a zero.")

#----------------------------------

#6. Calcular e mostrar a média dos dois números.

# Calcula e imprime a média
media = soma / 2
print(f"A média entre {num1} e {num2} é: {media:.2f}")

#----------------------------------

#7. Comparar os dois números e informar qual é maior ou se são iguais.

# Informa qual número é maior ou se são iguais
if num1 > num2:
    print(f"O número {num1} é maior que {num2}.")
elif num1 < num2:
    print(f"O número {num2} é maior que {num1}.")
else:
    print(f"Os números {num1} e {num2} são iguais.")