'''Crie uma função chamada remover_duplicatas que recebe 
uma lista e retorna uma nova lista sem elementos duplicados.'''
def remover_duplicatas(lista):
    nova_lista = []
    vistos = set()

    for item in lista:
        if item not in vistos:
            nova_lista.append(item)
            vistos.add(item)
    return nova_lista

lista = [1, 2, 2, 3, 4, 4, 5]
resultado = remover_duplicatas(lista)
print(resultado)