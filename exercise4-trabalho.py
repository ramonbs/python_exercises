print('Seja bem vindo ao Controle de Estoque da Bicicletaria do Ramon Giovani Brandão da Silva')


# Função para cadastrar uma peça

def cadastrarPeca(codigo):
    # solicita ao usuário informações sobre a peça a ser cadastrada
    nome = input("Nome da peça: ")
    fabricante = input("Fabricante da peça: ")
    valor = float(input("Valor da peça: "))

    # cria um dicionário com as informações da peça e retorna
    peca = {"codigo": codigo, "nome": nome, "fabricante": fabricante, "valor": valor}
    return peca


# Função para consultar peças
def consultarPeca(pecas):
    opcao = 0
    while opcao != 4:
        # exibe opções de consulta
        print("1. Consultar Todas as Peças")
        print("2. Consultar Peças por Código")
        print("3. Consultar Peças por Fabricante")
        print("4. Retornar")

        # solicita ao usuário a opção desejada
        opcao = int(input("Escolha uma opção: "))

        # caso a opção selecionada seja 1, exibe todas as peças cadastradas
        if opcao == 1:
            print("Código\tNome\tFabricante\tValor")
            for peca in pecas:
                print(peca["codigo"], "\t", peca["nome"], "\t", peca["fabricante"], "\t", peca["valor"])

        # caso a opção selecionada seja 2, solicita ao usuário o código da peça e exibe as informações caso exista
        elif opcao == 2:
            codigo = int(input("Digite o código da peça: "))
            for peca in pecas:
                if peca["codigo"] == codigo:
                    print("Código\tNome\tFabricante\tValor")
                    print(peca["codigo"], "\t", peca["nome"], "\t", peca["fabricante"], "\t", peca["valor"])
                    break
            else:
                print("Peça não encontrada!")

        # caso a opção selecionada seja 3, solicita ao usuário o fabricante da peça e exibe as informações caso exista
        elif opcao == 3:
            fabricante = input("Digite o nome do fabricante: ")
            print("Código\tNome\tFabricante\tValor")
            for peca in pecas:
                if peca["fabricante"] == fabricante:
                    print(peca["codigo"], "\t", peca["nome"], "\t", peca["fabricante"], "\t", peca["valor"])
            else:
                print("Nenhuma peça encontrada para esse fabricante!")


# Função para remover uma peça
def removerPeca(pecas):
    codigo = int(input("Digite o código da peça que deseja remover: "))
    # caso a peça seja encontrada, a remove da lista e exibe mensagem de sucesso
    for i, peca in enumerate(pecas):
        if peca["codigo"] == codigo:
            del pecas[i]
            print("Peça removida com sucesso!")
            break
    else:
        print("Peça não encontrada!")


# Lista vazia para armazenar as peças
pecas = []

# Variável para controlar o código das peças
codigo = 1

# Loop principal do programa
while True:
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Código da peça {:03d}".format(codigo))
        peca = cadastrarPeca(codigo)
        pecas.append(peca)
        codigo += 1
        print("Peça cadastrada com sucesso!")

    elif opcao == 2:
        consultarPeca(pecas)

    elif opcao == 3:
        removerPeca(pecas)

    elif opcao == 4:
        break

    else:
        print("Opção inválida!")
