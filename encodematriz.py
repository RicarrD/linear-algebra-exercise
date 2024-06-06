import numpy as np

def matrizcripto():
    # Pede a palavra para criptografar
    while True:
        palavra = input("Digite uma palavra com até 20 letras (apenas letras do alfabeto e espaços): ")
        if 5 < len(palavra) < 21 and all(c.isalpha() or c.isspace() for c in palavra):
            break
        else:
            print("A palavra deve ter até 20 letras e ter no minimo uma letra. Tente novamente.")

    # Converte a palavra para letras maiúsculas
    palavra = palavra.upper()

    # Converte a palavra em uma lista de letras
    letras = list(palavra)

    # Define as dimensões da matriz de criptografia como 10x2
    dUm = 10
    dDois = 2
    dimensoes = [dUm, dDois]

    # Inicializa uma matriz usando uma variável como tamanho e define o tipo para letras e números
    matriz = np.zeros(dimensoes, dtype='object')

    k = 0
    # Preenche a matriz com as letras da palavra
    for i in range(dDois):
        for j in range(dUm):
            if k < len(letras):  # Verifica se ainda há letras na lista letras
                matriz[j, i] = letras[k]
                k += 1

    # Cria um dicionário para a tabela de substituição
    tabela_substituicao = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
        'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
        'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
        'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27, '*': 0
    }

    # Substitui cada letra na matriz pela sua correspondência numérica
    for i in range(dUm):
        for j in range(dDois):
            letra = matriz[i, j]
            if letra in tabela_substituicao:
                valor_numerico = tabela_substituicao[letra]
                matriz[i, j] = valor_numerico

    print(matriz)

    # Define a matriz de criptografia
    criptografada = np.array(
        [[42, 24, 50, 2, 50, 10, 40, 48, 30, 3],
         [38, 35, 15, 25, 19, 5, 13, 17, 23, 50],
         [43, 1, 50, 24, 2, 45, 22, 42, 3, 26],
         [30, 1, 6, 12, 48, 50, 49, 11, 2, 19],
         [9, 12, 5, 45, 44, 16, 16, 40, 50, 5],
         [47, 19, 39, 14, 39, 45, 14, 42, 42, 36],
         [6, 36, 24, 50, 8, 12, 16, 50, 22, 26],
         [40, 5, 34, 46, 2, 20, 1, 32, 11, 32],
         [42, 1, 18, 21, 47, 22, 49, 20, 46, 11],
         [47, 43, 19, 25, 43, 16, 4, 23, 24, 42]])

    # Realiza a multiplicação entre a matriz criptografada e a matriz original
    mult = np.dot(criptografada, matriz)
    return mult
