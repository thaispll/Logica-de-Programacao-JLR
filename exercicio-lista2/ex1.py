'''1.	Faça um programa que lê o salário de um trabalhador e o valor da prestação 
de um empréstimo, depois verifica se a prestação é maior que 20% do salário e 
imprime a mensagem: "Empréstimo não concedido", caso contrário, imprime: "Empréstimo 
concedido".'''

salario = float(input("Digite o seu salário: "))
prestacoes = float(input("Digite as prestações: "))

if prestacoes <= 20/100 * salario:
    print("Empréstimo concedido!")
else:
    print("Empréstimo não concedido!")

