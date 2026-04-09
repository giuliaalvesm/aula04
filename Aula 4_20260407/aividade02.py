#Aplicação de Desconto AND e OR

valor = float(input('Valor da Compra: '))
forma_de_pagamento = input('Forma de Pagamento: ')

if valor >= 250 and forma_de_pagamento == 'a vista':
    print('Desconto Liberado')
    desconto = valor * 0.16
    novo_valor = valor - desconto
    print(f'Total a pagar: {novo_valor}')
elif valor <250 and forma_de_pagamento == 'a vista':
    print('Desconto Negado')
    print(f'Total a pagar: {valor}')
elif valor>= 250 and forma_de_pagamento == 'parcelado':
    print('Desconto Negado')
    print(f'Total a pagar: {valor}')
elif valor>= 250 or forma_de_pagamento == 'parcelado':
    print('Desconto Negado')
    print(f'Total a pagar: {valor}')

#--------------------------
valor = float(input('Valor da Compra: '))
forma_de_pagamento = input('Forma de Pagamento: ').lower()

if valor > 250 and forma_de_pagamento == 'a vista':
    print('Desconto Liberado')
    desconto = valor * 0.16
    novo_valor = valor - desconto
    print(f'Total a pagar: {novo_valor}')
else:
    print('Desconto Negado')
    print(f'Total a pagar: {valor}')

