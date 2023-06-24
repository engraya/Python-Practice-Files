# from fileinput import filename
# import json
# import numbers

# filename = 'numbers.json'
# with open(filename) as f:
#     numbers = json.load(f)

# print(numbers)


# filename = 'fruits'
# with open(filename) as c:
#     fruits = json.load(c)

# print(fruits)


# word = input('please enter your guess here to see if you are correct!  ')
# if word in fruits:
#     print('fantastic, your guess is correct')
# else:
#     print('sorry! try again next time youe guess is not found in the list')

import json


filename = 'seasons'
with open(filename) as s:
    seasons = json.load(s)

print(seasons)