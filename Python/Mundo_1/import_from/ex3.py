from random import choice
print('Digite o nome dos alunos:')
a1 = str(input('1° '))
a2 = str(input('2° '))
a3 = str(input('3° '))
a4 = str(input('4° '))
lista = [a1, a2, a3, a4]

escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
