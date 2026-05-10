from random import choice
names = ['', '', '', '']

for i in range(len(names)):
    names[i] = input(f'Digite o nome do {i+1}º aluno: ')

print(f'O aluno sorteado foi: {choice(names)}')
