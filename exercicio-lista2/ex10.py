'''10.	O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, conforme a tabela abaixo.
 Leia o custo de fábrica e escreva o custo ao consumidor.'''
custo = float(input("Digite o custo de fábrica: "))

if custo <= 12000:
    custo_consumidor = custo + custo * 5/100
    print(f"Custo ao consumidor: R$ {custo_consumidor}")

elif custo > 12000 and custo <=25000:
    custo_consumidor = custo + custo * 10/100 + custo *15/100
    print(f"Custo ao consumidor: R$ {custo_consumidor}")

else:
    custo_consumidor = custo + custo * 15/100 + custo *20/100
    print(f"Custo ao consumidor: R$ {custo_consumidor}")
