'''8.	Crie um programa que leia três números e imprima o maior entre eles.'''

#num1 = float(input("Digite o número 1:"))
#num2 = float(input("Digite o número 2:"))
#num3 = float(input("Digite o número 3:"))

#print(max(num1,num2,num3))
numeros=[]

for i in range(1,3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = max(numeros)
print(f"O maior número digitado é: {maior}")


