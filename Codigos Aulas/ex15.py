dias_trabalhados = float(input('Por quantos dias você trabalhou neste mês? '))
horas_mensais = dias_trabalhados * 8.00
hora_por_dia = horas_mensais * 25
salário = horas_mensais + hora_por_dia
print(f"Seu salário este mês será de {salário}.")