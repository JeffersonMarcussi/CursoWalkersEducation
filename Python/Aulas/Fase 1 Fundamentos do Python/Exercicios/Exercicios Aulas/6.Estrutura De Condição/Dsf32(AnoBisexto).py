from calendar import isleap
ano = int(input('Digite um número e verifique se ele e bisexto ou não!: '))
if isleap(ano) == True:
    print('Seu ano é bisexto')
else:
    print('Seu ano não é Bisexto')



