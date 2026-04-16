print(f"Aprovação de crédito\n")
casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe o salário do comprador: "))
anos = int(input("Informe em quantos anos deseja pagar a casa: "))
prestacao = casa/(anos * 12)
if prestacao > (salario * 0.3):
    print(f"Crédito negado!")
    print(f"A prestação exede os 30% do salário do comprador")
else:
    print("Crédito aprovado, parabéns!")