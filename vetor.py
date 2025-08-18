#Acessar elementos 
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] # "a"

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4] 
#print(sub_vetor)

#Adicionar elementos
vetor.append("d") #adiciona elemento ao final do vetor
#print(vetor)

#adicionar vários elementos de uma vez
vetor.extend([4,5])

#Remover elementos
vetor.remove("b")

#Remover elemento por índice(posição)
del vetor[2]
#print(vetor)

#Remove elemento pela posição
frutas = ["Morango", "Maçã", "Banana", "Pêra" , "Kiwi", "Pitaya", "Jaca"]
frutas.pop(2)
print(frutas)

#Atualizar elementos
#atribui um novo valor para a posição específica
vetor[0] = "JLR"
#print(vetor)

#len (IMPORTANTE) = LENGTH
tamanho_vetor = len(vetor)
print(vetor)
print(tamanho_vetor)

#ordenação
matriculas = ["Yasmin G", "Yasmin S", "Wanessa","Maria Clara", "Katelyn Lamin", "Reenam", "Agatha", "Matheus"]
matriculas.sort()
print(matriculas)

#cria nova lista ordenada
novo_vetor = sorted(matriculas)
print(novo_vetor)

#Iteração : percorre os elementos
for estudante in matriculas:
    print(estudante)

#Dividir strings em palavras
frase = "Python é muito bom!"
palavras = frase.split()
print(palavras)

#Juntar palavras em string
nova_frase = " ".join(palavras)
print(nova_frase)


#Operações matemáticas em vetores numericos
vetor_numerico = [1,2,3,4]
for i in range(len(vetor_numerico)):
    vetor_numerico[i] *=2 #vetor_numerico[i] = vetor_numerico[2] *2
print(vetor_numerico)


