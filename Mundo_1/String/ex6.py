nomei = str(input('Digite o seu nome: ')).strip()
nome = nomei.split(' ')

print('O seu primeiro nome é {}'.format(nome[0]))
print('O seu ultimo nome é {}'.format(nome[len(nome)-1]))
