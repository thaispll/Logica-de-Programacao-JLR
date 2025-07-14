'''Faça um programa que leia um nome de usuário e a sua senha e não 
aceite a senha igual ao nome do usuário, mostrando uma mensagem de 
erro e voltando a pedir as informações.'''

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if senha.lower() == usuario.lower():
        print("Erro: a senha não pode ser igual ao nome do usuário.Tente novamente. \n")
    else:
        print("Cadastro realizado com sucesso!")
        break 
