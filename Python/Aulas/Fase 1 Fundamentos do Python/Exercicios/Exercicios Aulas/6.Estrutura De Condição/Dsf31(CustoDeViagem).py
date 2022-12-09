distancia = float(input('Qual a distancia de sua viagem? Km:'))

if distancia <= 200:
    calculo1 = float(distancia*0.50)
    print(f'Sua viagem não e tão longa assim!, o custo será de R$:{calculo1}')
else:
    calculo2 = float(distancia*0.45)  
    print(f'Nossa sua viagem e bom longe!, o custo será de R$:{calculo2}')  