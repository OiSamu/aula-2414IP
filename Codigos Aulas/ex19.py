primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
nota_final = (primeira_nota + segunda_nota) / 2

if nota_final >= 7.0:
   print("Você foi muito bem!!!")
   pass
elif nota_final < 7.0 and nota_final >= 5.0:
    print("Tem que estudar mais!")
    pass
elif nota_final < 5.0:
    print("Você vai repetir de ano.")
    pass
else:
    print("Nota inválida.")