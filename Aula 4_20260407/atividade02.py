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
