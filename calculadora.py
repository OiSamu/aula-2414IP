while True :
    comando = input('Digite "sair" para sair: ')
    if comando.lower() == "sair":
        break
    print(f"Você digitou: {comando}")

calculadora = input('Digite sua operação: ')

if calculadora == "-":
    número1_de_menos = float(input('Primeiro número: '))
    número2_de_menos = float(input('Segundo número: '))
    resultado_de_menos = número1_de_menos - número2_de_menos
    print(f"O resultado desta operação é igual á: {resultado_de_menos}.")
    pass
elif calculadora == "+":
    número1_de_mais = float(input('Primeiro número: '))
    número2_de_mais = float(input('Segundo número: '))
    resultado_de_mais = número1_de_mais + número2_de_mais
    print(f"O resultado desta operação é igual á: {resultado_de_mais}.")
    pass
elif calculadora == "/":
    número1_de_divisão = float(input('primeiro número: '))
    número2_de_divisão = float(input('Segundo número: '))
    resultado_de_divisão = número1_de_divisão / número2_de_divisão
    print(f"O resultado desta operação é igual á: {resultado_de_divisão}.")
    pass
elif calculadora == "*":
    número1_de_vezes = float(input('Primeiro número: '))
    número2_de_vezes = float(input('Segundo número: '))
    resultado_de_vezes = número1_de_vezes * número2_de_vezes
    print(f"O resultado desta operação é igual á: {resultado_de_vezes}.")
    pass
else:
    print("Operação inválida.")