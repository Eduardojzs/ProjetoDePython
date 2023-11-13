#1. Solicite ao usuário o valor que ele ganha por hora.

# Solicita o valor ganho por hora e a quantidade de horas trabalhadas no mês
valor_hora = float(input("Quanto você ganha por hora? "))

#2. Pergunte quantas horas foram trabalhadas no mês.
horas_trabalhadas = float(input("Quantas horas você trabalhou este mês? "))

"""
3. Calcule o salário bruto multiplicando o valor por hora 
    pelas horas trabalhadas.
"""

# Calcula o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

print(f"\nSalário Bruto: {salario_bruto}")

"""
4. Se o usuário tiver trabalhado mais de 160 horas no mês, 
    calcule o valor das horas extras. Cada hora extra deve ser 
    compensada com um adicional de 50% sobre o valor da hora comum.
"""

# Inicializa a variável de horas extras e o valor correspondente dessas horas
horas_extras = 0
valor_horas_extras = 0

# Verifica se o total de horas trabalhadas excede 160 horas
if horas_trabalhadas > 160:
    
    # Calcula a quantidade de horas que excedem 160 horas
    horas_extras = horas_trabalhadas - 160
    
    # Calcula o valor das horas extras (acrescido de 50% sobre o valor da hora comum)
    valor_horas_extras = horas_extras * valor_hora * 0.5
    
    print(f"Valor hora extra: {valor_horas_extras}")
   

"""
5. Calcule o imposto de renda sobre o salário (considerando as horas extras). 
    O imposto de renda tem uma taxa fixa de 11% sobre o salário.
"""

# Calcula o imposto de renda, considerando 11% do salário bruto mais o valor das horas extras
imposto_renda = 0.11 * (salario_bruto + valor_horas_extras)

# Calcula o salário líquido, subtraindo o imposto de renda do salário bruto somado ao valor das horas extras
salario_liquido = (salario_bruto + valor_horas_extras) - imposto_renda

print(f"Salário Líquido: {salario_liquido}")

"""
6. Mostre ao usuário uma descrição detalhada contendo:
        - Salário Bruto.
        - Valor das Horas Extras (se aplicável).
        - Valor do Imposto de Renda.
        - Salário Líquido (Salário Bruto + Horas Extras - Imposto de Renda).
"""

#Exibindo os resultados
print(f"\n\nSalário Bruto: R$ {salario_bruto:.2f}")
print(f"Valor das Horas Extras: R$ {valor_horas_extras:.2f}")
print(f"Valor do Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")