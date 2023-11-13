vogais = ['a', 'e', 'i', 'o', 'u']

while True:  # Loop infinito até que o usuário decida sair
    
    # 1. Solicite ao usuário que digite uma letra ou uma palavra.
    entrada_usuario = input("Digite uma letra ou palavra: ")
    
    
    """
    2. Se o usuário digitar apenas um caractere:
    
        a. Verifique se é uma vogal ou consoante.
        b. Se for uma vogal, exiba: "Você digitou uma vogal."
        c. Se for uma consoante, exiba: "Você digitou uma consoante."
        d. Se o caractere não for uma letra, exiba: "Caractere inválido."
    """
    # Verifica se a entrada do usuário possui apenas um caractere
    if len(entrada_usuario) == 1:

        # Converte o caractere inserido para minúsculo para simplificar a verificação subsequente
        char = entrada_usuario.lower()
        
        if char in vogais:
            print("Você digitou uma vogal")
            
        # Verifica se o caractere é alfabético (isto é, se é uma letra) e não é uma vogal
        elif char.isalpha():  
            print("Você digitou uma consoante.")
            
        # Se o caractere não for uma vogal nem uma consoante, é tratado como inválido
        else:
            print("Caractere inválido.")
      
        """
        3. Se o usuário digitar mais de um caractere (uma palavra):

            a. Calcule e exiba o número de vogais na palavra.
            b. Calcule e exiba o número de consoantes na palavra.
            c. Exiba a palavra em ordem inversa.
            d. Informe se a palavra é um palíndromo (se lê da mesma forma de frente para trás 
            e de trás 
            para frente, como "arara").
        """
    elif len(entrada_usuario) > 1:
        
        # Converte a entrada do usuário para minúsculo para simplificar a verificação subsequente
        palavra = entrada_usuario.lower()
        
        # Calcula e exibe o número de vogais na palavra. 
        # Utiliza uma compreensão de lista para contar os caracteres que são vogais.
        # num_vogais = sum(1 for char in palavra if char in vogais)
        
        # Inicializa o contador de vogais
        num_vogais = 0

        # Itera sobre cada caractere na palavra
        for char in palavra:
            
            # Verifica se o caractere atual é uma vogal
            if char in vogais:
                num_vogais += 1

        print(f"A palavra {palavra} contém {num_vogais} vogais.")
        
        
        # Calcula e exibe o número de consoantes na palavra. 
        # Utiliza uma compreensão de lista para contar os caracteres que são letras alfabéticas e não são vogais.
        # num_consoantes = sum(1 for char in palavra if char.isalpha() and char not in vogais)
        
        # Inicializa o contador de consoantes
        num_consoantes = 0

        # Itera sobre cada caractere na palavra
        for char in palavra:
            
            # Verifica se o caractere é alfabético e não é uma vogal
            if char.isalpha() and char not in vogais:
                num_consoantes += 1

        print(f"A palavra {palavra} contém {num_consoantes} consoantes.")
        
        
        # Exibe a palavra em ordem inversa usando fatiamento de string.
        print(f"A palavra em ordem inversa é: {palavra[::-1]}")
        
        # Verifica se a palavra é um palíndromo, comparando-a com sua versão invertida.
        # Se forem iguais, é um palíndromo; caso contrário, não é.
        if palavra == palavra[::-1]:
            print(f"A palavra {entrada_usuario} é um palíndromo.")
        else:
            print(f"A palavra {entrada_usuario} não é um palíndromo.")
        
    # 4. Peça ao usuário se deseja verificar outra letra ou palavra ou sair do programa.
    
    continuar = input("Deseja verificar outra letra ou palavra? (sim/não) ")
    
    # Verifica se a entrada "continuar" foi fornecida como "não" (independente de ser maiúscula ou minúscula)
    #lower - Converte os caracteres em caixa baixa (minúsculas).
    if continuar.lower() == 'não':
        
        print("Obrigado por usar o programa!")  # Imprime uma mensagem de agradecimento ao usuário
        break  # Sai do loop atual, terminando a execução deste bloco de código
    