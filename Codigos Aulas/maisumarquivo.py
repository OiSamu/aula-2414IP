quilômetros_percorridos = float(input('Quantos quilômetros você percorreu? '))
dias_de_uso = int(input('Por quantos dias você usou o carro? '))

diária = dias_de_uso = 90
quilômetros = quilômetros_percorridos = 0.20
total = diária * dias_de_uso + quilômetros_percorridos * quilômetros
print(f"O total a pagar é {total}R$.")