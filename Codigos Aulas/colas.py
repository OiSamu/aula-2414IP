
#Exemplo 1: Contador simples
contador = 0
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1 #Incremeta o Contador.

    
senha = "1234"
tentativa = ""
while tentativa != senha:
    tentativa = input('Digite a senha: ')
    print("Acesso concedido!")