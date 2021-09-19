# Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago.

prod1 = int(input("Digite o valor do primeiro produto: "))
prod2 = int(input("Digite o valor do segundo produto: "))
desc1 = (prod1*8)/100
desc2 = (prod2*11)/100
val1 = prod1 - desc1
val2 = prod2 - desc2
valfinal = val1 + val2 

print("O valor final a pagar é: {}" .format(valfinal))

