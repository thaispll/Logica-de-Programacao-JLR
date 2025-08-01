''' Escreva uma função chamada classificar_nota
 que recebe uma nota e retorna "Aprovado", 
 "Reprovado" ou "Em Recuperação" com base na nota.
'''

def classificar_nota(nota):
    if nota >= 7:
        print("Aprovado")

    elif nota >=5:
        print("Em recuperação")

    else:
        print("Reprovado")

nota = float(input("Digite a nota: "))
classificar_nota(nota)