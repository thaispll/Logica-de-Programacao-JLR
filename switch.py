'''Exemplo de match case'''

def switch_case(valor):
    match valor:
        case 1: 
            return "um"
        case 2:
            return "dois"
        case _:
            return "desconhecido"