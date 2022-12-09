n1 = int(input('Digite um número: '))
n2 = int(input('Agora digite outro: '))
n3 = int(input('Digite o último: '))

if n1<n3 and n1<n2:
    print(f'O menor número é o {n1}')
if n2<n1 and n2<n3:
    print(f'O menor número é o {n2}')
if n3<n2 and n3<n1:
    print(f'O maior número é o {n3}')

if n1>n3 and n1>n2:
    print(f'O menor número é o {n1}')
if n2>n1 and n2>n3:
    print(f'O menor número é o {n2}')
if n3>n2 and n3>n1:
    print(f'O menor número é o {n3}')