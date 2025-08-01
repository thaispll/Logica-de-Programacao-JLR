'''Crie uma função que receba como parâmetro uma lista,
com valores de qualquer tipo. A função deve imprimir 
todos os elementos da lista numerando-os'''
def imprimir_lista(lista):
    i = 0 
    for valor in lista:
        i += 1
        print(f"{i})", valor)

imprimir_lista(['Maçã', 27, True, 3.14])



