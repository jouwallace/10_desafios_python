
def dobrar_valor():
    numero_inserido = int(input('Digite um numero: '))
    calculo = numero_inserido * 2
    return calculo, numero_inserido


resultado, numero_inserido = dobrar_valor()
print(f'O dobro de {numero_inserido} é: {resultado}')
