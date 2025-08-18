#validação do nome

while True:
    nome = input("Digite o seu nome: ")

    if len(nome) >=3:
        break
    else:
        print("Erro: o nome deve conter pelo menos 3 caracteres")

#validação da idade
while True:
    idade = int(input("Digite a sua idade(entre 0 e 150): "))

    if 0 <= idade <= 150:
        break
    else:
        print("Erro: a idade deve ser entre 0 e 150.")

while True: 
    salario = float(input("Digite o seu salário: "))

    if salario > 0:
        break
    else:
        print("Erro: o salário deve ser maior que zero")

while True:
    genero = input("Digite seu gênero ('F' para Feminino, 'M para Masculino, 'O' para outros:)").upper()
    if genero in ['F', 'M', 'O']:
        break
    else:
        print("Erro: Gênero Inválido. Digite 'F', 'M' ou 'O'.")

#validação do estado civil
while True:
    estado_civil = input("Digite o seu estado civil ('s' - solteiro(a), 'c' - casado(a), 'v' - viúvo(a), 'd' - divorciado(a)):").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Erro: Estado civil inválido!")

#Exibir as informações
print("\n Informações validadas com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")

if genero == "F":
    print("Gênero: Feminino")
elif genero == "M":
    print("Gênero: Masculino")
else:
    print("Gênero: Outros")

if estado_civil == "s":
    print("Estado Civil: Solteiro(a)")
elif estado_civil == "c":
    print("Estado Civil: Casado(a)")
elif estado_civil == "v":
    print("Estado Civil: Viúvo(a)")
else:
    print("Estado Civil: Divorciado(a)")

