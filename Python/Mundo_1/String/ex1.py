nome = str(input('Digite um nome completo: ')).strip()
nomesepa = nome.split()

print('O nome em maiusculo {}'.format(nome.upper()))
print('O nome em minusculo {}'.format(nome.lower()))
print('O seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome é {} e tem {} letras'.format(
    nomesepa[0], len(nomesepa[0])))
