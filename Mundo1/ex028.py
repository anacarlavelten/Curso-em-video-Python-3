from random import randint
computador = randint(0, 5)
print('=-'*20)
print("Jogo da adivinhação")
print ("Adivinhe o número que eu estou pensando entre 0 e 5: ")
print('=-'*20)
num = int(input("Em qual número eu pensei? "))
if num == computador:
    print(f"Parabéns! você acertou, eu pensei no número {num}")
else: 
    print(f"Você errou! o número que eu pensei foi o {computador}")