from math import hypot

oppos_leg = float(input('Digite o comprimento do cateto oposto: '))
adj_leg = float(input('Digite o comprimento do cateto adjacente: '))
hypotenuse = hypot(oppos_leg, adj_leg)
'''hipotenusa = (cateto_oposto**2 + cateto_adjacente**2)**0.5'''

print(f'O comprimento da hipotenusa é {hypotenuse:.2f}')
