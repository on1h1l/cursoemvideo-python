num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
s = num_1 + num_2
m = num_1 * num_2
d = num_1 / num_2
di = num_1 // num_2
e = num_1 ** num_2
print(f'A soma é {s}.\nO produto é {m} e a divisão é {d:.3f}.', end=' >>> ')
print(f'A divisão inteira é {di} e a potência é {e}')
