# Define os objetos para os valores de dimensões, peso e a rota
DIM_VALORES = {
    (0, 1000): 10,
    (1000, 10000): 20,
    (10000, 30000): 30,
    (30000, 100000): 50
}

PESO_MULT = {
    (0, 0.1): 1,
    (0.1, 1): 1.5,
    (1, 10): 2,
    (10, 30): 3
}

ROTA_MULT = {
    'RS': 1,
    'SR': 1,
    'BS': 1.2,
    'SB': 1.2,
    'BR': 1.5,
    'RB': 1.5
}

print('Seja muito bem vindo a Companhia de Logistica Ramon Giovani Brandão da Silva S.A!')

# Define as funções de perguntas para as dimensões, peso e rota
def dimensoesObjeto():
    while True:
        # esta estrutura do try foi usada para captar o erro de tipo,
        # caso o usuário entre com um valor que não seja numérico
        try:
            altura = float(input("Digite a altura do objeto em cm: "))
            comprimento = float(input("Digite o comprimento do objeto em cm: "))
            largura = float(input("Digite a largura do objeto em cm: "))
            volume = altura * comprimento * largura
            for limites, valor in DIM_VALORES.items():
                if limites[0] <= volume < limites[1]:
                    return valor
            print("Valor de dimensões inválido, proporções são muito grandes!")
        #  capturando o erro e printando mensagem tratada
        except ValueError:
            print("Valor inválido, entre com um valor numérico.")


def pesoObjeto():
    while True:
        try:
            peso = float(input("Digite o peso do objeto em kg: "))
            for limites, valor in PESO_MULT.items():
                if limites[0] <= peso < limites[1]:
                    return valor
            print("Valor de peso inválido, não aceitamos cargas tão pesadas!")
        except ValueError:
            print("Valor inválido, entre com um valor numérico.")


def rotaObjeto():
    while True:
        rota = input("Digite a rota do objeto (ex: RS, SR, BS, SB, BR, RB): ").upper()
        if rota in ROTA_MULT:
            return ROTA_MULT[rota]
        print("Rota inválida, ela não existe!")


# Programa principal, chamada das funções
dimensoes = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()

total = dimensoes * peso * rota
print(f"Total a ser pago: R$ {total:.2f}")
