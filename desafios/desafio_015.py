km = float(input("Digite a quantidade de km percorridos: "))
days = int(input("Digite a quantidade de dias que o carro foi alugado: "))
price = (km * 0.15) + (days * 60)
print(f"O preço a pagar é: R$ {price:.2f}")