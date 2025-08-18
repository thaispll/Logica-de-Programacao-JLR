'''2.	Faça um programa que receba a altura e o sexo de uma pessoa e
 calcule e mostre seu peso ideal, utilizando as seguintes fórmulas 
 (onde h corresponde à altura):
 - Homens: (72,7 × h) − 58
 - Mulheres: (62,1 × h) − 44,7
'''

altura = float(input("Digite a sua altura"))
genero = input("Digite F para Feminino ou M para Masculino").upper()

if genero == "F":
    feminino = (62.1 * altura) - 44.7
    print(f"Peso ideal: {feminino:.2f}")

elif genero == "M":
    masculino =(72.7 * altura) - 58
    print(f"Peso ideal: {masculino:.2f}")
else:
    print("Número inválido!")
