# Descrição
Este script Python realiza a decodificação de uma mensagem criptografada usando uma matriz de criptografia predefinida. A mensagem criptografada é multiplicada pela matriz inversa da matriz de criptografia para recuperar a mensagem original.

# Realização
Este é um trabalho da seguinte disciplina
ÁLGEBRA LINEAR - UNICARIOCA - Professor Manuel Martins Filho

# Pré-requisitos
Para executar este script, você precisará de:

Python 3.x
NumPy (biblioteca de computação numérica)

# Modo de Uso
Clone ou baixe este repositório para o seu ambiente local.
Certifique-se de que o arquivo encodematriz.py está no mesmo diretório que o arquivo decodematriz.py.
Execute o script usando o comando:
  python decodematriz.py

# Funcionamento do Script

O script solicita ao usuário que insira uma palavra com até 20 letras (apenas letras do alfabeto e espaços).
A palavra fornecida é convertida em maiúsculas e dividida em uma matriz.
A matriz de criptografia é pré-definida no código.
A mensagem criptografada é multiplicada pela matriz inversa da matriz de criptografia para obter a mensagem original.
Os valores resultantes são arredondados e convertidos em inteiros.
Os números inteiros são convertidos de volta em letras, conforme a tabela de substituição.
A palavra original é exibida na saída.

# Observações
Caso haja algum problema com a entrada ou processamento da palavra fornecida, o script informará e solicitará uma nova entrada.
