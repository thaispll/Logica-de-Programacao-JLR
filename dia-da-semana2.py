'''Faça uma função dia_da_semana(numero) que recebe um número de 1 a 7
e retorna o nome do dia da semana correspondente, sendo 1 para 
"Segunda-feira", 2 para "Terça-feira", 3 para "Quarta-feira", 4 para
"Quinta-feira", 5 para "Sexta-feira", 6 para "Sábado" e 7 para "Domingo"
'''

def dia_da_semana(numero):
    match numero:
        case 1:
            return "Segunda-feira"
        case 2:
            return "Terça-feira"
        case 3:
            return "Quarta-feira"
        case 4:
            return "Quinta-feira"
        case 5:
            return "Sexta-feira"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:
            return "Dia inválido!"

#FORA DA FUNÇÃO!
entrada = int(input("Digite um número de 1 a 7 para o dia da semana: "))

#chamar a função com o valor de entrada
resultado = dia_da_semana(entrada)
print(resultado)