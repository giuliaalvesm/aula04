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

# Operadores AND e OR
usuario = input('Nome: ')
senha = input('Senha: ')

if usuario == 'admin' and senha == '1234':
    print('Login realizado com sucesso')
else:
    print('Login ou senha incorretos')

#------------------------------

usuario = input('Nome: ')
senha: input('Senha: ')

if usuario == 'admin' or senha == '1234':
    print('Login realizado com sucesso')
else:
    print('Login incorreto')



