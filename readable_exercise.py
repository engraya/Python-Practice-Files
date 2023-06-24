with open('exercise_file.txt') as all:
    statements = all.read()
print(statements)

filename = 'exercise_file.txt'
with open(filename) as all:
    for structures in all:
        print(structures)


new_statement = structures.capitalize()

print(new_statement)


word = input('enter the word: ')
if word in new_statement:
    print('yes, correct')
else:
    print('no, wrong')


