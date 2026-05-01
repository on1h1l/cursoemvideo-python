price = float(input('Digite o preço do produto: R$'))
discount = price * 0.05
new_price = price - discount
print(f'O produto que custava R${price:.2f}, com desconto de 5% vai custar R$ {new_price:.2f}')
