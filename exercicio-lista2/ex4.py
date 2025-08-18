'''Escreva um programa que leia um número inteiro entre 1 e 7 e imprima 
o dia da semana correspondente a esse número. Isto é: domingo se for 1, 
segunda-feira se for 2, e assim por diante.'''

def dia_semana(numero):
    match numero:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5: 
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "Dia inválido"

num = int(input("Digite um número inteiro entre 1 e 7: "))
print(dia_semana(num))       

