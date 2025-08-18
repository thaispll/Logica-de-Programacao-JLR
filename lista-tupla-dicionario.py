#Lista:Coleção ordenada e mutável de elementos.Pode ser modificada
#consigo excluir, adicionar e atualizar uma lista
frutas = ["maçã", "banana", "laranja"]
print(frutas)

#Adiciona item na lista
frutas.append("uva")
print(frutas)

#Tupla: coleção ordenada, mas IMUTÁVEL (não pode ser alterada após criada)

coordenadas = (10.0, 20.0)
print(coordenadas)

#Dicionário: coleção não ordenada de pares chave-valor.
aluno = {
    "nome": "Mauro",
    "idade": 25,
    "curso": "Psicologia"
}
print(aluno)

print(aluno["nome"])

aluno["idade"] = 21
print(aluno)


