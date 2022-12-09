import random 
number = int(random.randint(0, 5))

print('Olá seja bem vindo ao jogo da advinhação! \n vou escolher um número inteiro entre 0 e 5 e você terá que advinha vamos lá!')

numescolha = int(input('Escolha um número!: '))

if numescolha == number:
    print(f'Você venceu o número que escolhi foi o {number} \n PARABENS!')
else:
    print(f'Você perdeu o número que escolhi foi o {number} \n DERROTA!')