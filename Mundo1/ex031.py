distancia = float(input("Qual a distância da viagem(KM)? "))
if distancia <= 200:
    print(f"O valor da passagem será de {distancia * 0.5} reais")
else:
    print(f"O valor da passagem será de {distancia * 0.45} reais")
