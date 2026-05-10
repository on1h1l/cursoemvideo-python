from math import sin, cos, tan, radians

angle = float(input('Digite o ângulo: '))

print(f'O seno de {angle} é: {sin(radians(angle)):.2f}')
print(f'O cosseno de {angle} é: {cos(radians(angle)):.2f}')
print(f'A tangente de {angle} é: {tan(radians(angle)):.2f}')
