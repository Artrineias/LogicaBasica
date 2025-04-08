
frase = str(input('Digite uma frase qualquer: ')).upper().strip()

print('A quantidade de letras A é {}.'.format(frase.count('A',0)))
print('A letra A aparece primeiro na posição {}.'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na posição {}.'.format(frase.rfind('A')+1))
