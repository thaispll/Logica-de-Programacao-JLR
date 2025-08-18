'''9.	Escreva um programa que leia o código do produto escolhido no cardápio de uma lanchonete e a quantidade.
 O programa deve calcular o valor a ser pago por aquele lanche. Considere que, a cada execução, somente 
 será calculado um pedido.'''

codigos = [100, 101, 102, 103, 104, 105, 106]
descricoes = ["Cachorro Quente", "Bauru Simples", "Bauru com ovo", "Hamburguer", "Cheeseburger", "Suco", "Refrigerante"]
precos = [1.20, 1.30, 1.50, 1.20, 1.70,2.20,1.00]

print("Cardápio:")
for i in range(len(codigos)):
    print(f"Código: {codigos[i]} - {descricoes[i]} - R$ {precos[i]:.2f}")


codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

if codigo in codigos:
    posicao = codigos.index(codigo)
    preco_total = precos[posicao] * quantidade
    print(f"Produto: {descricoes[posicao]}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: {preco_total:.2f}")
else:
    print("Código inválido!")


