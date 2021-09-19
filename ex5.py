# Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou, por exemplo, o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120

fatorial =1
contador=1

numero = int(input("Digite um número: "))

while contador <= numero:
    fatorial *= contador
    contador += 1

print(" O fatorial de {} é {}".format (numero, fatorial))
