ano_de_nascimento = int(input("Em que ano você nasceu? "))
calculo = 2025 - ano_de_nascimento

if calculo >= 18:
    print("Você pode votar.")
    pass
elif calculo < 18:
    print("Você não pode votar.")
    pass
else:
    print("Você não existe.")
    pass