'''5.	Escreva um programa que leia um número inteiro entre 1 e 12 e imprima o mês correspondente 
a esse número. Isto é: janeiro se for 1, fevereiro se for 2, e assim por diante.'''

def mes(numero):
    match numero:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5: 
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9:
            return "Setembro"
        case 10:
            return "Outubro"
        case 11:
            return "Novembro"
        case 12:
            return "Dezembro"
        case _:
            return "Dia inválido"

num = int(input("Digite um número inteiro entre 1 e 12: "))
print(mes(num))   