# 8) Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem diferente para cada um dos casos a seguir: A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”; B) Se a média for menor que 7 e maior que 5, exiba a mensagem “Você ficou com média (media) e está de recuperação; C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”

nome = str(input("Digite seu nome: "))
nota1 = int(input("Digite o valor da 1° nota: "))
nota2 = int(input("Digite o valor da 2° nota: "))
nota3 = int(input("Digite o valor da 3° nota: "))

media = (nota1 + nota2 + nota3)/3

if media > 7:
    print("Parábens {}! Você foi aprovado." .format(nome))
elif media < 7 > 5:
    print("Você ficou com {} e está de recuperação." .format(media))
elif media < 5: 
    print("{}, você foi reprovado" .format(nome))