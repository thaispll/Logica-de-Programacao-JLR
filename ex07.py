#somar dígitos <100
numero = int(input(" Digite um número menor que 100: "))

if numero >=100:
    print("O número deve ser menor que 100")
else:
    unidade_dezena = numero // 10
    unidade_milhar = numero % 10    

    soma = unidade_dezena + unidade_milhar
    print(f"soma: {soma} ")
