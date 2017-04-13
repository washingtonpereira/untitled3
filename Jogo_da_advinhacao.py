#coding: utf8
import random
print("jogo de advinhação")


numero = random.randint(1,50)
jogada = 0
tentativas =0 
  


while jogada != numero:
    jogada = input("para jogar digite um numero de 1 a 50 :")
    tentativas +=1
    if jogada < numero:
      print("Errou ! numero menor que o correto")
    elif jogada > numero:
      print("Errou ! numero maior que o correto")
    if jogada == numero:  
      print("Acertou Miseravi", numero)
      print("voce tentativas", tentativas)



