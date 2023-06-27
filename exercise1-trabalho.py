print('Bem-vindo a loja do Ramon Giovani Brandão da Silva!')

# Primeir passo é realizar captação dos dados a partir das inputs,
# e armazenar valor do produto em uma variável do tipo float e a quantidade do produto em uma variável int

numeroDeProdutos = float(input('Entre com o valor do produto: '))
quantidadeDoProduto = int(input('Entre com a quantidade de produtos: '))

# Começo das verificações das condições, resolvi tratar um dos possíveis erros,
# o usuário entrar com quantidade negativa é uma condição inválida que quebraria a aplicação
if quantidadeDoProduto <= 0:
    print('Quantidade de produtos inválido! Entre com números positivos maiores que 0!')

# segunda verificação para validar a compra sem desconto
elif (quantidadeDoProduto > 0) and (quantidadeDoProduto <= 9):
    valorSemDesconto = numeroDeProdutos * quantidadeDoProduto
    valorComDesconto = numeroDeProdutos * quantidadeDoProduto
    print('O valor sem desconto foi de: R${:.2f}'.format(valorSemDesconto))
    print('O valor com desconto foi de: R${:.2f}  (desconto de 0%)'.format(valorSemDesconto))

# terceira verificação para validar primeiro desconto de 5% nos produtos com quantidade entre 10 a 99
elif (quantidadeDoProduto > 9) and (quantidadeDoProduto <= 99):
    valorSemDesconto = numeroDeProdutos * quantidadeDoProduto
    valorComDesconto = (numeroDeProdutos * quantidadeDoProduto) * 0.95
    print('O valor sem desconto foi de: R${:.2f}'.format(valorSemDesconto))
    print('O valor com desconto foi de: R${:.2f}  (desconto de 5%)'.format(valorComDesconto))

# quarta verificação para validar segundo desconto de 10% nos produtos com quantidade entre 100 a 999
elif (quantidadeDoProduto > 99) and (quantidadeDoProduto <= 999):
    valorSemDesconto = numeroDeProdutos * quantidadeDoProduto
    valorComDesconto = (numeroDeProdutos * quantidadeDoProduto) * 0.90
    print('O valor sem desconto foi de: R${:.2f}'.format(valorSemDesconto))
    print('O valor com desconto foi de: R${:.2f}  (desconto de 10%)'.format(valorComDesconto))

# última verificação que pega todos os restantes das condições que seria produtos com quantidade de
# 1000 ou mais e aplica desconto máximo de 15%.
else:
    valorSemDesconto = numeroDeProdutos * quantidadeDoProduto
    valorComDesconto = (numeroDeProdutos * quantidadeDoProduto) * 0.85
    print('O valor sem desconto foi de: R${:.2f}'.format(valorSemDesconto))
    print('O valor com desconto foi de: R${:.2f}  (desconto de 15%)'.format(valorComDesconto))
