'''Crie uma função que receba uma lista de números e retorne uma nova lista 
com os números ordenados em ordem crescente.'''

def ordenar_lista(lista):
    return sorted(lista)

numeros = [5, 10, 7, 6, 8, 9]
ordenados = ordenar_lista(numeros)

print(f"Lista original: {numeros} ")
print(f"Lista ordenada: {ordenados} ")
