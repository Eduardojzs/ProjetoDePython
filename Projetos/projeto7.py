"""
Exercício - Análise Comparativa e Estatística de Números

Objetivo: Desenvolver um programa que obtenha do usuário dez números e realize 
análises estatísticas e matemáticas com base nos valores inseridos.

Instruções:

    1. Solicite ao usuário que informe dez números.
    2. Determine e exiba qual é o maior número.
    3. Determine e exiba qual é o menor número.
    4. Calcule e exiba a média dos dez números.
    5. Informe quantos dos números são pares.
    6. Informe quantos dos números são positivos.
    7. Calcule e exiba a variação (diferença) entre o maior e o menor número.
    8. Mostre a soma dos números que são maiores que a média.
    9. Informe quantos dos números são negativos.
    
Observações: O programa deve considerar que o usuário fornecerá apenas 
valores numéricos válidos. Em todas as operações, os resultados devem ser 
exibidos com até duas casas decimais, quando aplicável.

"""
#Solução

#1. Solicite ao usuário que informe dez números.

numeros = []  # Lista para armazenar os dez números

# Loop para solicitar os dez números ao usuário

# Itera sobre uma sequência de 1 a 10 (inclusive)
for i in range(1, 11):
    
    # Solicita ao usuário para inserir um número e o converte para float
    num = float(input(f"Informe o {i}º número: "))
    
    # Adiciona o número informado à lista "numeros"
    numeros.append(num)
    
#2. Determine e exiba qual é o maior número.

maior_numero = max(numeros)
print(f"\nO maior número informado é: {maior_numero:.2f}")

#3. Determine e exiba qual é o menor número.

menor_numero = min(numeros)
print(f"O menor número informado é: {menor_numero:.2f}")

#4. Calcule e exiba a média dos dez números.

media = sum(numeros) / len(numeros)
print(f"A média dos números informados é:  {media:.2f}")

#5. Informe quantos dos números são pares.

# Inicializa o contador de números pares
pares = 0

# Itera por cada número na lista "numeros"
for num in numeros:

    # Verifica se o número atual é par
    if num % 2 == 0:

        # Incrementa o contador de números pares
        # pares = pares + 1
        pares += 1

print(f"{pares} números informados são pares.")


#6. Informe quantos dos números são positivos.

# Inicializa uma variável para contar os números positivos
positivos = 0

# Itera sobre cada número na lista 'numeros'
for num in numeros:
    
    # Verifica se o número atual é positivo
    if num > 0:
        
        # Se positivo, incrementa o contador
        positivos += 1

print(f"{positivos} números informados são positivos.")


#7. Calcule e exiba a variação (diferença) entre o maior e o menor número.

variacao = maior_numero - menor_numero
print(f"A variação entre o maior número e o menor número é: {variacao:.2f}")


# 8. Mostre a soma dos números que são maiores que a média.

# Inicializa uma variável para somar os números acima da média
soma_acima_media = 0

# Itera sobre cada número na lista 'numeros'
for num in numeros:
    
    # Verifica se o número atual é maior que a média
    if num > media:
        
        # Se maior, adiciona o valor do número à soma total
        soma_acima_media += num

        
print(f"A soma dos números que são maiores que a média é: {soma_acima_media:.2f}")

# 9. Informe quantos dos números são negativos.

# Inicializa uma variável para contar os números negativos
negativos = 0

# Itera sobre cada número na lista 'numeros'
for num in numeros:
    
    # Verifica se o número atual é negativo
    if num < 0:
        
        # Se for negativo, incrementa o contador
        negativos += 1

        
print(f"{negativos} números informados são negativos.")


"""
Números inseridos: 34, -2, 5, 9, 14, 38, 19, 24, -3, 18

O maior número é 38.
O menor número é -3.

A diferença entre o maior número (38) e o menor número (-3) é 38 - (-3) = 41.
"""