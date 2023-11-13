# Solicita ao usuário que insira um número e converte a entrada em float
num = float(input("Por favor, digite um número: "))


#1. Mostrar o número informado.

# Exibe o número que o usuário inseriu
print(f"\nO número informado foi {num}.")


#2. Informar se o número é par ou ímpar.

# A seguir, o código verifica se o número é par ou ímpar:
# Se o resto da divisão do número por 2 é zero, é porque ele é par
# if - Se
# else - Senão
if num % 2 == 0:
    
    # Imprime que o número é par
    print(f"O número {num} é par.")
    
else:
    
    # Caso contrário, imprime que o número é ímpar
    print(f"O número {num} é ímpar.")
    
    
#3. Informar se o número é positivo, negativo ou zero.

# O código agora verificará se o número é positivo, negativo ou zero:
# Se o número for maior que zero, ele é positivo
# if - Se
# elif - Senão Se
# else - Senão
if num > 0:
    
    # Imprime que o número é positivo
    print(f"O número {num} é positivo.")
    
    
    #4. Se o número for positivo, calcular e mostrar sua raiz quadrada.
    
    # Calcula a raiz quadrada do número elevando-o à potência 0.5
    raiz = num ** 0.5
    
    # Imprime a raiz quadrada do número
    print(f"A raiz quadrada de {num:.0} é {raiz:.0f}.")
    
# Se o número for menor que zero, ele é negativo
elif num < 0:
    
    # Imprime que o número é negativo
    print(f"O número {num} é negativo.")
    
else:
    # Se o número não for nem positivo nem negativo, ele é zero
    print(f"O número informado é zero.")

    
    