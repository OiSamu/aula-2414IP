idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 4:
    print("Você é um bebê.")
    pass
elif idade >= 4 and idade <= 13:
    print("Você é um adolescente.")
    pass
elif idade >= 14 and idade <= 17:
    print("Você é um adolscente. ")
    pass
elif idade >= 18 and idade <= 24:
    print("Você é maior de idade, mas ainda é jovem")
    pass
elif idade >= 25 and idade <= 50:
    print("Você é um adulto.")
    pass
elif idade >= 50 and idade <= 80:
    print("Você é um idoso.")
    pass
else:
    print("Idade inválida."),