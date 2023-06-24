nigeria = []
nigeria.append('yobe')
nigeria.append('kaduna')
nigeria.append('kogi')
nigeria.append('lagos')
nigeria.append('jigawa')

print(nigeria)

numbers1 = [2,2,4,5,6,7,8,9,0,6,4,5,43,54]
numbers1.extend(7,8,9,)

numbers2 = []

for element in numbers1:
    numbers2.append(element*2)
print(numbers2)

numbers3 = [element*10 for element in numbers1]
print(numbers3)

number4 = []
for values in range(1,40):
    number4.append(values*4)
print(number4)

number5 = []
for values in range(1,90):
    number5.append(values*9)
print(number5)

number6 = [values*2 for values in range(1,45)]
print(number6)


new_series = []
for u in range(6, 0, -1):
    new_series.append((u**2))
print(new_series)
