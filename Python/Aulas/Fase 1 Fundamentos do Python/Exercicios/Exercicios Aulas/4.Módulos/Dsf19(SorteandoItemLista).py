import random

al1 = str(input('Fale o nome do aluno 1: '))
al2 = str(input('Fale o nome do aluno 2: '))
al3 = str(input('Fale o nome do aluno 3: '))
al4 = str(input('Fale o nome do aluno 4: '))
lista = [al2, al2, al3, al4]

r = random.choice(lista)

print(f'O aluno sorteado foi {r}!')