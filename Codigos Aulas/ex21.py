data_de_nascimento = int(input('Digite seu ano de nascimento: '))
alistamento = 2025 - data_de_nascimento

if alistamento >= 18:
    print(f"Você deveria ter se alistado faz {alistamento} anos.")
    pass
elif alistamento < 18:
    print(f"Faltam {alistamento} anos para você se alistar.")