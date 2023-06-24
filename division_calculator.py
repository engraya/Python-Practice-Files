from cgi import print_arguments


print('give me two numbers and i will add them instantly for you')
print("enter 'end' to quit or end the program")

while True:
    number1 = input("\n number1: ")
    if number1 == 'end':
        break
    number2 = input("\ number2: ")
    if number2 == 'end':
        break

    try:
        result = int(number1) / int(number2)
    except ZeroDivisionError:
        print('SORRY! YOU CANT DIVIDE THE NUBER BY ZERO................!!!!!')
    else:
        print(result)

 