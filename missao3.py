nota = int(input('Qual foi a sua nota? '))

if nota >= 90 and nota <= 100:
    print('Parabens, Voce tirou A!!!')
elif nota >= 80 and nota <= 89:
    print('Muito bem, voce tirou B.')
elif nota >= 70 and nota <= 79:
    print('Bom trabalho, voce tirou C.')
elif nota >= 60 and nota <= 69:
    print('Fique atento, você tirou D')
elif nota >= 0 and nota < 60:
    print('Estude um pouco mais, você tirou F.')
else:
    print('Nota inválida, digite somente notas de 0 a 100')
