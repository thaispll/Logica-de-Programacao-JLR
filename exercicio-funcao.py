'''Faça um programa que tenha uma função chamada 
maior(), que receba vários parâmetros com valores
 inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.
'''
'''def maior(a,b,c):
    if a > b and a > b:
        return f"O maior número é {a}"
    elif b > a and b > c:
        return f"O maior número é {b}"
    else:
        return f"O maior número é {c}"
print(maior(10,20,200)) '''


''' Forma da Thais'''
def maior(primeiro, *restantes):
    return max(primeiro, *restantes)

#Exemplos de uso:
print(maior(10, 4,7, 22, 13,17))
print(maior(5,5,5))