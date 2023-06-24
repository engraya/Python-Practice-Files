with open('files.txt') as my_files:
    all_in = my_files.read()
print(all_in)

filename = 'files.txt'

with open(filename) as main_object:
    for line in main_object:
        print(line)
print(line)


with open(filename) as main_object:
    lines = main_object.readlines()
    for line in lines:
        print(line)


random_string = ''
for line in lines:
    random_string += line
print(random_string)
print(len(random_string))
2
favourite_date = input('Enter yoyr favourite date here to see if it appers on the match  ')
if favourite_date in random_string:
    print('statement True!')
else:
    print('sorry. wrong statement!')

