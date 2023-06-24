with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())


file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())


file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(f"{pi_string[:52]}..........")
print(len(pi_string))

independence_day = input('Enter your independece day in the form of mmddyy to see if the date can be found in the pi file: ')
if independence_day in pi_string:
    print('Your independence day can be found in pi file')
else:
    print('Sorry! your independence cannot be found in thhe pi file')



