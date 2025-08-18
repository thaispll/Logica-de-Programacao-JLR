#Perguntar quanto ganha por hora
ganhos = float(input("Quanto você ganha por hora trabalhada?"))
# Perguntar quantas horas trabalhadas
horas = float(input("Quantas horas você trabalhou no mês?"))

# Cálculo do total do salário
calculo = ganhos * horas

#imprimir total
print(f"Você receberá o valor de R${calculo}")
