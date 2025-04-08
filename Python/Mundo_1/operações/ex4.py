name = input('Enter the name of student:')

note1 = int(input('first note:'))
note2 = int(input('second note:'))

print('The student {}  had average grade of {:.1f}'.format(name, (note1+note2)/2))
