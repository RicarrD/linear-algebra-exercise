# Ricardo dos Santos da Silva 2023100944
# Jean Souza de Santana Nascimento Macção 2023100819
from statistics import mode
# Declaração de variaveis
numerosInteiros = []
x = []
y = []

# Pede números para o usuário
for i in range(10):
    while True:
        escolha = input(f"Digite o {i+1}º número ou 'parar' caso não queira mais números. ")
        if escolha.lower() == 'parar':
            break
        try:
            num = int(escolha)
            numerosInteiros.append(num)
            break
        except ValueError:
            print("Por favor, insira um número inteiro.")
    if escolha.lower() == 'parar':
        break

for num in numerosInteiros:
    if num % 2 == 0:
        x.append(num)
    else:
        y.append(num)

# Soma dos elementos sobre o total de elementos
mediax = sum(x) / len(x) if x else 0
mediay = sum(y) / len(y) if y else 0

# Moda dos conjuntos
def calcula_moda(lista):
    frequencias = {}
    for num in lista:
        frequencias[num] = frequencias.get(num, 0) + 1
    max_freq = max(frequencias.values())
    modas = [num for num, freq in frequencias.items() if freq == max_freq]
    return modas

modaX = calcula_moda(x) if x else None
modaY = calcula_moda(y) if y else None

# Ordena os números para calcular a mediana
xOrdenado = sorted(x)
yOrdenado = sorted(y)

# Mediana dos conjuntos
def calcula_mediana(lista):
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]

medianaX = calcula_mediana(xOrdenado) if xOrdenado else None
medianaY = calcula_mediana(yOrdenado) if yOrdenado else None

# Soma dos desvios ao quadrado sobre o total de elementos
varianciax = sum((num - mediax) ** 2 for num in x) / len(x) if x else 0
varianciay = sum((num - mediay) ** 2 for num in y) / len(y) if y else 0

# Calculo da Variância
coefVarianciaX = (varianciax ** 0.5) / mediax * 100 if mediax != 0 else 0
coefVarianciaY = (varianciay ** 0.5) / mediay * 100 if mediay != 0 else 0

print('A array x(pares) tem {} números e é composta pelos numeros {}'.format(len(x), x))
print('A array y(ímpares) tem {} números e é composta pelos numeros {}'.format(len(y), y))
print('A soma do array x(pares) é {}'.format(sum(x)))
print('A soma do array y(ímpares) é {}'.format(sum(y)))
print("A média dos conjuntos númericos é: x(pares) = {:.2f} e y(ímpares) = {:.2f}".format(mediax, mediay))
print("A moda dos conjuntos é: x(pares) = {}, y(ímpares) = {}".format(modaX, modaY))
print("A mediana dos conjuntos é: x(pares) = {:.2f}, y(ímpares) = {:.2f}".format(medianaX, medianaY))
print("A variância dos conjuntos númericos é: x(pares) = {:.2f} e y(ímpares) = {:.2f}".format(varianciax, varianciay))
print("O coeficiente de variação dos conjuntos numéricos é:x(pares) = {:.2f} e "
      "y(ímpares) = {:.2f}".format(coefVarianciaX, coefVarianciaY))