'''Crie uma função chamada ordenar_lista que recebe uma lista de 
números e retorna a lista ordenada em ordem crescente.'''

def ordenar_lista(lista):
    if not lista:
        return []
    
    #ORDENAR A LISTA
    lista_ordenada = sorted(lista)
    #lista_decrescente = sorted(lista, reverse=True)
    
    print(f"Lista ordenada: {lista_ordenada} ")

lista1 = [10, 2, 5, 9, 1,0]
ordenar_lista(lista1)
    

