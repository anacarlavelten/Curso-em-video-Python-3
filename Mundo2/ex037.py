print("Conversão de bases\n")
num = int(input("Escolha um número para conversão: "))
print("Escolha agora uma opção para conversão")
print("Opção 1: binário")
print("Opção 2: octal")
print("Opção 3: hexadecimal")
escolha = int(input("Sua escolha: "))
if escolha < 0 or escolha > 3:
    print("Opção inválida")
else:
    match escolha:
        case 1:
            binario = bin(num)[2:]
            print(f"O número {num} em binário é {binario}")
        case 2:
            octal = oct(num)[2:]
            print(f"O número {num} em octal é {octal}")

        case 3:
            hexa = hex(num)[2:]
            print(f"O número {num} em hexadecimal é {hexa}")