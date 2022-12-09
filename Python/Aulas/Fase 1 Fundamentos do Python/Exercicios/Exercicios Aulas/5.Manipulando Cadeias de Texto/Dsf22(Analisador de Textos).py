nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
replaced = nome.replace(" ", "")

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minusculas: {nome.lower()}')
print(f'Quantas letras ao todo?: {len(replaced)}')
print(f'O primeiro {dividido[0]} nome tem: {len(dividido[0])} letras')
