'''4.	Faça um programa que pergunte o salário do funcionário e imprima o 
valor do aumento de 15% sobre o salário atual.'''

salario = float(input("Digite o salário atual do funcionário: R$"))
aumento = salario * 0.15
novo_salario = salario + aumento
print(f"O novo salário será de: R$ {novo_salario:.2f}")
