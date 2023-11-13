"""
Exercício Análise de Desempenho do Aluno

Objetivo: Desenvolver um programa que avalie o desempenho de um aluno ao
longo dos bimestres. Para isso, o programa deve solicitar as quatro
notas bimestrais do aluno e, com base nelas, realizar as seguintes ações:

    1. Calcular e exibir a média das notas.
    2. Determinar e mostrar a maior e a menor nota entre as inseridas.
    3. Com base na média, informar ao usuário se o aluno está aprovado, 
    em recuperação ou reprovado. Considere os seguintes critérios:
        - Aprovado: média >= 7
        - Em recuperação: 5 <= média < 7
        - Reprovado: média < 5
        
    4. Calcular e mostrar a quantidade de notas que estão acima da média calculada.
"""

#Solução

# Solicita as 4 notas bimestrais ao usuário
nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))

#1. Calcular e exibir a média das notas.

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"\nA média das notas é: {media:.2f}")

#------------------------------------------------

#2. Determinar e mostrar a maior e a menor nota entre as inseridas.

# Encontra e exibe a maior e menor nota
maior_nota = max(nota1, nota2, nota3, nota4)
menor_nota = min(nota1, nota2, nota3, nota4)

print(f"A maior nota foi: {maior_nota}")
print(f"A menor nota foi: {menor_nota}")

#------------------------------------------------

"""
3. Com base na média, informar ao usuário se o aluno está aprovado, 
    em recuperação ou reprovado. Considere os seguintes critérios:
        - Aprovado: média >= 7
        - Em recuperação: 5 >= média < 7
        - Reprovado: média < 5
"""

print(f"\nMédia: {media}")

# Com base na média, determina a situação acadêmica do aluno
if media >= 7:
    
    # Se a média for maior ou igual a 7, o aluno está aprovado
    print("Aluno aprovado!")
    
elif media >= 5:
    
    # Se a média for maior ou igual a 5 e menor que 7, o aluno está em recuperação
    print("Aluno em recuperação.")
    
else:
    
    # Se a média for menor que 5, o aluno está reprovado
    print("Aluno reprovado.")
    

#------------------------------------------------

#4. Calcular e mostrar a quantidade de notas que estão acima da média calculada.

# Inicializa um contador para armazenar a quantidade de notas acima da média
contador = 0

# Itera sobre cada uma das quatro notas
for nota in [nota1, nota2, nota3, nota4]:
    
    # Verifica se a nota atual é maior que a média
    if nota > media:
        
        # Incrementa o contador se a nota estiver acima da média
        contador += 1

        print(f"Nota: {nota}")

print(f"Quantidade de notas acima da média: {contador}")