#Pedir 4 notas

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

#calcular média ponderada
media = (nota1 *1 +nota2 *2 + nota3 *3 + nota4 *4)/10

#imprimir média
print(f"A média das notas é:{media} ")