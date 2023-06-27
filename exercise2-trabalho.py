# Tabela de produtos, resolvi criar um objeto (ou dicionário) para manipulação ficar mais fácil, no qual:
# chave é o identificador do produto e o valor é um array com nome do produto e valor.
produtos = {
    100: ["Cachorro-Quente", 9.00],
    101: ["Cachorro-Quente Duplo", 11.00],
    102: ["X-Egg", 12.00],
    103: ["X-Salada", 13.00],
    104: ["X-Bacon", 14.00],
    105: ["X-Tudo", 17.00],
    200: ["Refrigerante Lata", 5.00],
    201: ["Chá Gelado", 4.00]
}

# Variáveis de controle para continuar programa, finalizar e contabilizar o valor do pedido
total = 0.0
continuar = True

while continuar:
    # Imprime a lista de produtos e o meu identificador
    print('Bem vindo a lanchonete do Ramon Giovani Brandão da Silva!!!')

    print("Código\tDescrição\t\t\tValor(R$)")
    # loop está sendo realizod sobre o objeto produtos para printar a lista
    for codigo, produto in produtos.items():
        print(f"{codigo}\t{produto[0]:<30}{produto[1]:.2f}")

    # Solicita o código do produto
    codigo = input("Digite o código do produto desejado: ")

    # Verifica se o código é válido: sendo um number e se está contido na lista de produtos
    if codigo.isnumeric() and int(codigo) in produtos:
        codigo = int(codigo)
        total += produtos[codigo][1]  # Adiciona o valor do produto ao total
        print(f"{produtos[codigo][0]} adicionado ao pedido. Total: R$ {total:.2f}")
    else:
        print("Opção inválida. Digite um código válido.")
        continue

    # Pergunta se o cliente deseja pedir mais alguma coisa, caso sim, realiza o break deste while e
    # voltar para o anterior onde continuar continua sendo true
    while True:
        # aqui tive que fazer um tratamento pois estava ocasionando um bug se caso entrasse com
        # uma letra minúscula, utilizei o método upper para transformar para maisúculo
        opcao = input("Deseja pedir mais alguma coisa? (S/N) ").upper()
        if opcao == "S":
            break
        elif opcao == "N":
            continuar = False
            break
        else:
            print("Opção inválida. Digite 'S' para continuar ou 'N' para encerrar o pedido.")
            continue

# Imprime o valor total da conta
print(f"Total a pagar: R$ {total:.2f}")




