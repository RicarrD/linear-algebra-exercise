import numpy as np
from encodematriz import matrizcripto

C = np.array(
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

MC = matrizcripto()

print('\nA matriz da entrada origem é \n{}\n'.format(MC))


inversa = np.linalg.inv(C)
resultado = np.dot(inversa, MC).astype(float)
# Evitar problemas de precisão e arredondar para inteiros
resultado = np.rint(resultado).astype(int)
print('A matriz da mensagem original é \n{}\n'.format(resultado))

k = 0
letras = []
dUm = 10
dDois = 2

# Preenche a matriz com as letras da palavra
for j in range(dDois):
    for i in range(dUm):
        letras.append(resultado[i, j])
        k += 1

tabela_substituicao = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
    8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
    15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
    22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', 27: ' ', 0: '*'
}

k = 0

for k in range(len(letras)):
    valor = letras[k]
    if valor in tabela_substituicao:
        valor_numerico = tabela_substituicao[valor]
        letras[k] = valor_numerico

palavra = ''.join(letras)

print('A palavra original é "{}".'.format(palavra.lower().replace('*', '')))
