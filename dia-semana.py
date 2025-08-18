def dia_da_semana(dia):
    match dia:
        case "sábado" | "domingo":
            return "Fim de semana"
        case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
            return "Dia útil"
        case _:
            return "Dia inválido!"

print(dia_da_semana("sábado"))
print(dia_da_semana("Kelly"))