#Domingos Soares do Carmo Neto
#32032889

nome = []
salario = []
abono = []
ab = 0
v_min = 0
while True:
    sal = float(input('Digite o salário do colaborador [0 encerra]: '))
    if sal != 0:
        salario.append(sal)
    else:
        break
    nome.append(str(input('Digite o nome do colaborador: ')))
    ab = sal * 0.20
    if ab <= 100:
        ab = 100
        abono.append(ab)
        v_min += 1
    else:
        abono.append(ab)
print('Projeção de Gastos com Abono')
print('='*30)
n = 0
text = ''
min_list = min(len(nome), len(salario))
while n < min_list: 
    text += '\nNome: {}   Salário: {}'.format(nome[n], salario[n])
    n += 1
print(text)
print('')
print(f'\n {"Nome -"}  {"Salário -"}  {"Abono"}')
n = 0
text = ''
while n < min_list: 
    text +='\n {}-  R$ {}-  R$ {}'.format(nome[n], salario[n],abono[n])
    n += 1
print(text)
print('')
print(f'Foram processados {len(nome)} colaboradores.')
print(f'Total gastos com abonos: R${sum(abono)} ')
print(f'Valor mínimo pago a {v_min} colaboradores.')
print(f'Maior valor de abono pago a: {max(abono)} ')
