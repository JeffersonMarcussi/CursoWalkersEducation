velocidade = int(input('A quantos Km/h você está?: '))


if velocidade > 80:
    print('Você passou do seu limite de velocidade e será multado!')
    multa = int((velocidade-80)*7)
    print(f'Sua multa é de R$:{multa}')
else:
    print('Você está na velocidade correta!')   