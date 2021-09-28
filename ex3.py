#  Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas pessoas são maiores de idade.

dataNasc = 0
contador = 1
total = 0

while contador <= 10:
    contador += 1
    dataNasc = int(input("Digite o ano em que você nasceu: "))
    deMaior = 2021 - dataNasc
    if deMaior >= 18:
        total += 1
print ("{} São pessoas maiores de idade" .format (total))
