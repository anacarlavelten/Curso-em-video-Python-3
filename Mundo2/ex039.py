print('Verificar alistamento')
anonasc = int(input('Digite seu ano de nascimento? '))
idade = 2025
if idade < 18:
    print(f'Não será possível se alistar! Faltam {18 - idade} anos para o alistamento')
elif idade > 18:
    print(f'Já passou o tempo de alistamento! Se passaram {idade - 18} anos')
else:
    print('Este é o momento certo para se alistar!')