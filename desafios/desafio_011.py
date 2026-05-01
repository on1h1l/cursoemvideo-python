width = float(input('Digite a largura da parede (m): '))
height = float(input('Digite a altura da parede (m): '))
area = width * height
paint = area / 2
print(f'Sua parede tem a dimensão de {width}m x {height}m e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {paint}l de tinta')
