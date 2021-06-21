nome = input('Digite a nome do aluno:')

a1 = int(input('primeira nota:'))
a2 = int(input('segunda nota:'))

print('O aluno {} teve nota media de {:.1f}'.format(nome, (a1+a2)/2))
