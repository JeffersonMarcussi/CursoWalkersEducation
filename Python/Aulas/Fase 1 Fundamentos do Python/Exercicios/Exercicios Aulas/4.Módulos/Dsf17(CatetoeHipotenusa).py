import math

co = float(input('Qual o comprimento do cateto oposto?: '))
ca = float(input('Qual o comprimento do cateto adjacente?: '))
sm = float((pow(co, 2 ))+(pow(ca, 2)))

print(f'O valor da Hipotenusa dessas medidas é: {math.sqrt(sm)}')