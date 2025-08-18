'''1.	Faça um programa que lê o salário de um trabalhador e o 
valor da prestação de um empréstimo, depois verifica se a prestação 
é maior que 20% do salário e imprime a mensagem: 
"Empréstimo não concedido",
 caso contrário, imprime: "Empréstimo concedido".'''

#pedir para usuário
salario = float(input("Digite o seu salário: "))
prestacao = float(input("Digite o valor da prestação desejada: "))

if prestacao > 0.2 * salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")