'''Implemente uma função que recebe uma lista de números e retorna True se todos eles forem positivos.'''

def todos_positivos(lista):
    for numero in lista:
        if numero <=0:
            return False
    return True

numeros = [1, 5, 7, 8, 10]
print(todos_positivos(numeros))

numeros2 = [1, 3, -5]
print(todos_positivos(numeros2))
