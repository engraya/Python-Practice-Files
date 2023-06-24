
print('give me three numbers and i will multiply them instantly for you')
print("enter 'end' to quit or end the program")

while True:
    number1 = input("\n number1: ")
    if number1 == 'end':
        break
    number2 = input("\ number2: ")
    if number2 == 'end':
        break
    number3 = input("\n number3: ")
    if number3 == 'end':
        break
    result = int(number1) * int(number2) * int(number3)
    print(f" Here is the sum of your two numbers:........{result}.....")
    print(result)

