#Exemplo 3: Loop infinito com interrupção
while True:
    comando = input('Digite "sair" para parar: ')
    if comando.lower() == "sair":
        break
    print(f"Você digitou: {comando}")