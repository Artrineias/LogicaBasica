word = ('Python','Program','Learn','Course','Free','Study','Practice','Work','Market','Programmer','Future')
m = len(word)
for w in word:
    if w == word[0]:
        print(f'In the word {w.upper()} we have',end= " ")
    else:
        print(f'\nIn the word {w.upper()} we have',end= " ")
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter,end=" ")
print('')