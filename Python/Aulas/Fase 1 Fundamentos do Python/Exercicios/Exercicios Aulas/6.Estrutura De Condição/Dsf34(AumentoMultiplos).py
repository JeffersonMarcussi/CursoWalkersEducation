sal = float(input('Qual o salario do funcionario?R$:'))

if sal > 1250:
    cal1 = int((10*sal) / 100)
    print(f'Seu salario e maior que R$1250 seu aumento será respectivo a 10% R$:{sal+cal1}')
else:
    cal2 = int((15*sal) / 100)
    print(f'Seu salario é menor que R$1250 seu aumento será respectivo a 15% R$:{sal+cal2}')    