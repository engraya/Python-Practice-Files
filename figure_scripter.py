from fileinput import filename
import json

numbers = [2, 3, 4, 6, 7, 89, 6, 456, 57, 58, 676, 87, 66, 789, 78, 99]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


fruits = ['apple', 'banana', 'mango', 'kiwi', 'pineapple', 'strawberry', 'berry', 'apricot']


filename = 'fruits'
with open(filename, 'w') as c:
    json.dump(fruits, c)


seasons = ['winter', 'summer', 'autumn']

filename = 'seasons'
with open(filename, 'w') as s:
    json.dump(seasons, s)
