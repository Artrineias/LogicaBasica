print('Para fazer a verificação da media digite as notas do aluno.')
nota_1 = float(input('1°nota: '))
nota_2 = float(input('2°nota: '))
media = (nota_1 + nota_2)/2
if media < 5:
    print('O aluno foi reprovado.')
elif media >= 5 and media <= 6.9:
    print('O aluno vai pra recuperação.')
else:
    print('O aluno foi aprovado.')
