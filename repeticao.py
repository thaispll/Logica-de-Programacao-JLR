'''i = 1

while i <5:
    print(i)
    i += 1 # i = i +1 
'''
i = 0

while i < 4:
    print("Olá")
    i += 1

''' While: usa quando quer repetir o código ENQUANTO
a condição for VERDADEIRA. Quando usar: quando não se
conhece o número previamente
For: quando se sabe o número de repetições ou quando
iterar sobre uma sequência'''
'''
alunos = ["Fulana", "Beltrano", "Ciclano"]

for aluno in alunos: # para elemento in vetor 
    print(f"Aluno: {aluno}")
#Para cada aluno, dentro de ALUNOS faça:

frutas = ["Morango", "Abacate","Laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
'''

#Tabuada

numero = int(input("Digite o número para ver a tabuada: "))
print(f"Tabuada do {numero}:")

for i in range(1,11): #range:sequência de números inteiros. range(início,parada)
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
