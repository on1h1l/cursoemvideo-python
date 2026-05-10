from random import shuffle
names = ['', '', '', '']

for i in range(len(names)):
    names[i] = input(f'Digite o nome do {i+1}º aluno: ')
shuffle(names)

print(f'A ordem de apresentação será: {names}')
