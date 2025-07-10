'''Desenvolva um programa em Python que utilize WHILE para permitir
 o cadastro de um número indeterminado de funcionários. O programa deve
 encerrar o cadastro quando o usuário digitar 0  e,ao final, exibir a 
 lista completa dos funcionários registrados'''

funcionarios = []

while True:
    nome = input("Digite o nome do funcionário (ou 0 para encerrar): ")
    
    if nome == "0":
        break #parada
    

    #impedir que o usuário envie um campo vazio de funcionários

    if nome.strip() == "":
        print("O nome do funcionário não pode estar vazio. Tente novamente") #strip():remove espaços em branco
        continue
    
    funcionarios.append(nome)

print("\nLista de funcionários cadastrados: ")
for i, funcionario in enumerate(funcionarios, 1): #enumerate: itera sobre a sequência
#iterar = repetir
#enumerate(objeto a ser percorrido, valor inicial do índice)
    print(f"{i}. {funcionario}")