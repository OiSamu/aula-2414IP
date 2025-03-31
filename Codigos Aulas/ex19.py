primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))
nota_final = (primeira_nota + segunda_nota) / 2

if nota_final >= 7.0:
    print("Você foi muito bem!!!")
    pass
elif nota_final <= 7.0:
    print("Tem que estudar mais!")
    pass
else:
    print("Você vai repitir de ano.")
    pass