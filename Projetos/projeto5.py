"""
Exercício Análise de Números Inteiros e Reais

Objetivo: Desenvolver um programa que obtenha do usuário dois 
números inteiros e um número real, e em seguida realize e apresente 
uma série de cálculos e análises relacionadas a esses números.

Instruções:

    1. Solicite ao usuário dois números inteiros.
    2. Solicite ao usuário um número real.
    3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo.
    4. Calcule e exiba a soma do triplo do primeiro número com o terceiro número.
    5. Calcule e exiba o terceiro número elevado ao cubo.
    6. Determine e informe se o primeiro número é par ou ímpar.
    7. Determine e informe se o terceiro número é positivo, negativo ou zero.
    8. Calcule e mostre a média aritmética entre os três números.
"""

#Solução:

#1: Solicitar ao usuário dois números inteiros.

# Solicitando os dois números inteiros ao usuário.
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

#------------------------------------------------------------------------------

#2. Solicite ao usuário um número real.
num3 = float(input("Digite um número real: "))

#------------------------------------------------------------------------------

#3. Calcule e exiba o produto do dobro do primeiro número com metade do segundo.

"""
Nesse contexto, "produto" refere-se ao resultado da multiplicação 
entre dois ou mais números.

Vamos quebrar a expressão produto = (2 * num1) * (num2 / 2):

    2 * num1: Está dobrando o valor de num1. Por exemplo, se num1 for 5, 
    esta expressão resultará em 10.

    num2 / 2: Está dividindo o valor de num2 pela metade. Por exemplo, 
    se num2 for 8, esta expressão resultará em 4.

    A expressão final (2 * num1) * (num2 / 2) está multiplicando o dobro 
    de num1 pela metade de num2.

Então, se num1 for 5 e num2 for 8:

    O dobro de num1 é 10.
    A metade de num2 é 4.
    O produto desses dois resultados (ou seja, 10 multiplicado por 4) é 40.
"""
produto = (2 * num1) * (num2 / 2)
print(f"\nO produto do dobro do primeiro com metade do segundo é: {produto}")

#------------------------------------------------------------------------------

#4. Calcule e exiba a soma do triplo do primeiro número com o terceiro número.

soma = (3 * num1) + num3
print(f"A soma do triplo do primeiro número com o terceiro é: {soma}")

#------------------------------------------------------------------------------

#5. Calcule e exiba o terceiro número elevado ao cubo.

cubo = num3 ** 3

print(f"O terceito número elevado ao cubo é: {cubo:.2f}")

#------------------------------------------------------------------------------

#6. Determine e informe se o primeiro número é par ou ímpar.

# Verifica se o primeiro número é divisível por 2 (ou seja, par)
if num1 % 2 == 0:
    
    # Se for divisível por 2 (resto da divisão é 0), imprime que o número é par
    print(f"O primeiro número, {num1}, é par.")
    
else:
    
    # Se não for divisível por 2 (resto da divisão não é 0), imprime que o número é ímpar
    print(f"O primeiro número, {num1}, é ímpar.")


#------------------------------------------------------------------------------
    
#7. Determine e informe se o terceiro número é positivo, negativo ou zero.

# Verifica se o terceiro número é maior que 0
if num3 > 0:
    
    # Se for maior que 0, imprime que o número é positivo
    print(f"O terceiro número, {num3}, é positivo.")
    
# Verifica se o terceiro número é menor que 0
elif num3 < 0:
    
    # Se for menor que 0, imprime que o número é negativo
    print(f"O terceiro número, {num3}, é negativo.")
    
else:
    
    # Se não for maior nem menor que 0, então é exatamente 0
    print(f"O terceiro número é zero.")
    
#------------------------------------------------------------------------------


#8. Calcule e mostre a média aritmética entre os três números.

# Calcula a média aritmética somando os três números e dividindo por 3
media = (num1 + num2 + num3) / 3

# Imprime a média calculada formatada com duas casas decimais
print(f"A média entre os três números é: {media:.2f}")