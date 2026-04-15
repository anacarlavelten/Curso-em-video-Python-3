velocidade = float(input("Qual a velocidade do carro? "))
if velocidade > 80:
    print(f"Você foi multado!")
    print(f"O valor da multa será de: {(velocidade - 80)* 7}")
else:
    print(f"Velocidade correta, tenha uma boa viagem!")