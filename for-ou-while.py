#for: usamos para repetir o código com um número CONHECIDO e DEFINIDO
#de vezes

for i in range(1,6): #range: repetição de 1 a 6 i= indice do vetor
    print(i)

#outra forma
alunos = ["Melquisedeque", "Rebeca", "Sara", "Abraão", "Paulo", "Noé"]

for aluno in alunos: #em: dentro
    print(aluno) #printa o elemento sozinho

print(alunos)

#while: usado para repetir o código enquanto a condição for verdadeira
#não sabemos quantas vezes irá repetir
i = 1

while i<=5:
    print(i)
    i += 1