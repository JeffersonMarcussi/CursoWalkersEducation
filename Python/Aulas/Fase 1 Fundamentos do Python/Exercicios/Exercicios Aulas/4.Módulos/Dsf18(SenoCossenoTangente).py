import math

a = float(input('Qual o angulo?: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))

print(f' O angulo de {a} tem o seno de {s}  \n O angulo de {a} tem o cosseno de {c}  \n o angulo de {a} tem o tangente de {t}')