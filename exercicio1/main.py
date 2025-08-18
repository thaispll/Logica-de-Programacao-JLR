'''Escreva uma classe para representar um Aluno. Adicione atributos relacionados às características de um 
Aluno, como nome,matricula, curso que está matriculado, nome de 3 disciplinas que está cursando e as notas
 dessas 3 disciplinas. Desenvolva um método para verificar se o aluno está aprovado(nota maior ou igual a 7) 
 em uma determinada disciplina. Escreva um programa para testar essa classe, que pede as informações do aluno 
 ao usuário e ao final informe o nome das disciplinas, mostrar as notas e mostrar se o aluno foi aprovado ou não.'''

from aluno import Aluno #from nomedoarquivo import nomedaclasse

def main():
    print("Cadastro do aluno:")
    nome = input("Nome: ")
    matricula = input("Matricula: ")
    curso = input("Curso: ")

    disciplinas = []
    notas = []
    
    print("Informe 3 disciplinas e as notas correspondentes: ")
    for i in range(3):
        disciplina = input(f"Nome da disciplina {i+1}: ")

        while True:
            try:
                nota = float(input(f"Nota da disciplina {disciplina}: "))
                if 0 <= nota <=10:
                    break
                else:
                    print("A nota deve ser entre 0 e 10.")
            except ValueError:
                print("Digite uma nota válida (número).")
    disciplinas.append(disciplinas)
    notas.append(nota)  

    aluno = Aluno(nome, matricula, curso, disciplinas, notas)

    print("\n Resultado das disciplinas: ")
    for disciplina in aluno.disciplinas:
        nota = aluno.notas[aluno.disciplinas.index(disciplina)]
        status = "Aprovado" if aluno.verifica_aprovacao(disciplina) else "Reprovado"
        print(f"Disciplina {disciplina} - Nota: {nota:.1f} - {status}")

main()
#criar classe Aluno (arquivo aluno.py) e main.py

#atribuir caracteristicas: nome, matricula, curso, 3 disciplinas e notas.

#pedir informacoes do aluno e pedir nome das disciplinas, 

#mostrar notas
# mostrar se foi aprovado ou não