dia = float(input('Quantos dias você ficou com o carro?: '))
km = float(input('Quantos Kilometros você rodou?:'))

d = float(60*dia)
k = float(0.15*km)

print(f'O total a pagar por {dia} dias, é {km}km é R${d+k}')