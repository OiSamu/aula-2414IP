#Neste programa, farei um cobrador de multa, que a cada kilômetro a mais, o programa cobra uma taxa de 5.00 R$ a cada kilômetro a mais
velocidade_da_via = 80.0
multa_km = - 5.00
velocidade_atual = float(input("Digite sua velocidade atual (em Kilômetros): "))
#Aqui utilizei input para pedir a quantidade de kilômetros atuais.
pré_calculo = velocidade_da_via - velocidade_atual
multa = multa_km * pré_calculo
print(f"Você pagará uma multa de {multa}R$.")
