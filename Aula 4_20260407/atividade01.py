# Cálculo de Desconto
valor = float(input('Insira o valor: '))

if valor >=250:
    print('Desconto Liberado')
    desconto = valor * 0.16
    novo_valor = valor - desconto
    print(f'Total a pagar: {novo_valor}')
else:
    print('Desconto Negado')
    print(f'Total a pagar: {valor}')




