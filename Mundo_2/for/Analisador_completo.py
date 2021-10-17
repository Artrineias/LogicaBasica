import os
mulher_n = 0
homem_v_i = 0
soma = 0
os.system('clear')or None
for x in range (1,6,1):
    print("-"*6+"{}°PESSOA".format(x)+6*"-")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input('Sexo[M/F]: ').upper()
    os.system('clear')or None
    if 20>=idade and sexo== 'F':
        mulher_n=mulher_n + 1
    if sexo=='M' and homem_v_i==0:
        homem_v = nome 
        homem_v_i = idade
    soma += idade
    media = soma/x
print('A media de idade do grupo é {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(homem_v_i,homem_v))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_n))