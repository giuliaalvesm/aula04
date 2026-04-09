# Exemplo IFs Encadeados
nota = float(input('Insira a nota: '))
if nota >= 10:
    print('A')
elif nota >= 7:
    print('B')
elif nota >= 5:
    print('C')
elif nota >= 3:
    print('D')
else:
    print('F')

# Exemplo IFs Não Encadeados
nota = float(input('Insira a nota: '))
if nota >= 10:
    print('A')
if nota >= 7:
    print('B')
if nota >= 5:
    print('C')
if nota >= 3:
    print('D')
else:
    print('F')

#Exemplo IFs aninhados
nota = float(input('Insira a nota: '))
frequencia = float(input('Informe a frequência: '))

if nota >= 7 and frequencia >= 75:
    print('Aprovado')
else:
    print('Reprovado')

#Exemplo IFs aninhados 2
nota = float(input('Insira a nota: '))
frequencia = float(input('Informe a frequência: '))
if nota >= 7:
    #Aprovado por nota, mas precisa checar a frequência
    if frequencia >= 75:
        print('Aluno aprovado por Nota e Frequência')
    else:
        print('Aluno reprovado por Frequência baixa')
else:
    print('Aluno reprovado por nota baixa')
