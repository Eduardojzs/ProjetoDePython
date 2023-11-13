"""
Exercício Controle de Empréstimos em uma Biblioteca

Objetivo: Desenvolver um programa que auxilie Maria, uma bibliotecária, 
a controlar o número de livros emprestados por um usuário durante o mês. Para 
cada dia que o usuário exceder o limite estabelecido de livros pegos, uma multa 
será aplicada.

Instruções:

    1. O sistema de biblioteca possui um limite estabelecido de 5 
    livros que cada usuário pode pegar por vez.
    
    2. Para cada livro excedente, o usuário deve pagar uma multa de R$ 2,00.
    
    3. O programa deve começar solicitando ao usuário o número de 
    dias em que pegou livros no mês.
    
    4. Em seguida, para cada um desses dias, o programa deve pedir que 
    o usuário informe o número de livros pegos.
    
    5. O sistema deve calcular e exibir o excesso de livros e o valor 
    da multa para cada dia.
    
    6. Ao final, o programa deve mostrar o total de livros excedentes e 
    o total da multa acumulada no mês.
    
    7. Se, ao final do mês, o usuário não tiver excedido o limite em nenhum dia, 
    o programa deve mostrar uma mensagem de parabenização por seguir as regras.

Observação: O programa deve considerar que o usuário informará dados válidos, ou seja, 
valores inteiros não-negativos para o número de dias e o número de livros pegos em cada dia.
"""
# Solução:

"""
1. O sistema de biblioteca possui um limite estabelecido de 5 
    livros que cada usuário pode pegar por vez.
"""

LIMITE_LIVROS = 5

#2. Para cada livro excedente, o usuário deve pagar uma multa de R$ 2,00.
MULTA_POR_LIVRO = 2.00

"""
3. O programa deve começar solicitando ao usuário o número de 
    dias em que pegou livros no mês.
"""

#Solicitando ao usuário o número de dias em que pegou livros no mês
numero_de_dias = int(input("Informe o número de dias em que você pegou livros neste mês: "))

"""
4. Em seguida, para cada um desses dias, o programa deve pedir que 
    o usuário informe o número de livros pegos.
"""

total_livros_excedentes = 0
total_multa = 0

# Etapa 4 e 5: Loop para cada dia informado pelo usuário
for dia in range(1, numero_de_dias + 1):
    
    # Solicita o número de livros pegos no dia
    numero_de_livros = int(input(f"Quantos livros você pegou no dia {dia}? "))
    
    # Calcula o excesso de livros e a multa para o dia
    
    """
    1. excesso = max(0, numero_de_livros - LIMITE_LIVROS)

    O cálculo do excesso tem o objetivo de encontrar quantos livros foram pegos 
    além do limite permitido.

        numero_de_livros - LIMITE_LIVROS subtrai o limite permitido do número de livros 
        pegos. Se o resultado for positivo, significa que houve excesso; se for negativo ou 
        zero, significa que não houve excesso.

        max(0, ...) é usado para garantir que, se o usuário pegou menos ou exatamente o 
        limite de livros, o excesso seja considerado 0. Isso ocorre porque um valor negativo 
        não faria sentido no contexto de "excesso". O uso da função max garante que o menor 
        valor que excesso pode assumir é 0.

    Por exemplo:
    Se o usuário pegou 4 livros, e o limite é 5:
    excesso = max(0, 4 - 5) = max(0, -1) = 0

    Se o usuário pegou 7 livros, e o limite é 5:
    excesso = max(0, 7 - 5) = max(0, 2) = 2
    2. multa = excesso * MULTA_POR_LIVRO

    Depois de determinar o excesso, o programa calcula o valor da multa devida.

        excesso * MULTA_POR_LIVRO multiplica o excesso pelo valor da multa por livro.

    Por exemplo, se o excesso é 2 livros e a multa por livro é R$2,00:
    multa = 2 * 2.00 = R$4.00

    Resumindo, esses cálculos determinam o número de livros pegos além do permitido e, 
    em seguida, calculam a multa correspondente com base nesse excesso.
    """
    excesso = max(0, numero_de_livros - LIMITE_LIVROS)
    multa = excesso * MULTA_POR_LIVRO
    
    # Exibe a informação para o usuário
    if excesso > 0:
        print(f"\nNo dia {dia}, você excedeu em {excesso} livros e deve pagar R${multa:.2f} de multa.")
    else:
        print(f"\nNo dia {dia}, você não excedeu o limite de livros.")
    
    # Acumula os totais
    total_livros_excedentes += excesso
    total_multa += multa
    
    
#6. Ao final, o programa deve mostrar o total de livros excedentes e 
#    o total da multa acumulada no mês.


# Mostrando o total acumulado no mês
if total_livros_excedentes > 0:
    
    print(f"\nAo longo do mês, você excedeu um total de {total_livros_excedentes} livros e deve pagar R${total_multa:.2f} de multa.")
        
        
    """
    7. Se, ao final do mês, o usuário não tiver excedido o limite em nenhum dia, 
        o programa deve mostrar uma mensagem de parabenização por seguir as regras.
    """
else:
    
    print("\nParabéns por seguir as regras da biblioteca durante todo o mês!")
    
    
