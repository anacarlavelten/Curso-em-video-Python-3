ano = int(input("Digite um ano: "))
div1 = 100
div2 = 4
if ano % div1 and ano % div2:
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")