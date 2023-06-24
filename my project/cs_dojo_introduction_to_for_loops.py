loop_values = ['arizona', 'missisipi', 'virginia', 'dakota', 'alabama', 'michigan', 'texas', 'georgia', 'arkansas']
print(loop_values[0])
print(loop_values[6])
print('i want to visit' +' '+  loop_values[7])

for states in loop_values:
    print(states)
    print(states)

values_k = [2,2,4,5,6,7,8,9,0,6,4,5,43,54]
for value in values_k:
    print(value)


values_k = [2,2,4,5,6,7,8,9,0,6,4,5,43,54]
sum = 0
for value in values_k:
    sum = sum + value
print(sum)

numbers_in_range = list(range(1,30))
print(numbers_in_range)

for k in range(1,99):
    print(k)

total4 = 0
for m in range(1, 500):
    total4 = total4 + m
print(total4)


total8 = 0
for r in range(1,25):
    total8 += r
print(total8)

total_reader = 0
range_u = list(range(1, 5000))
print(range_u)

for p in range_u:
    if p % 2 == 0: 
        total_reader += p
print(total_reader)

for p in range_u:
    if p % 10 == 0:
        total_reader = total_reader + p
print(total_reader)


numbers_less_than_100 = list(range(1,100))
total_3  = 0 
for w in numbers_less_than_100:
    if w % 3 == 0:
        total_3 += w
print(total_3)

numbers_less_than_100 = list(range(1,100))
total_5 = 0
for f in numbers_less_than_100:
    if f % 5 == 0:
        total_5 = total_5 + f
print(total_5)



states = ['arizona', 'missisipi', 'virginia', 'dakota', 'alabama', 'michigan', 'texas', 'georgia', 'arkansas']
for q in states:
    print(q)



for l in range(len(states)):
    for m in range( l + 1):
        print(states[l])



print(list(range(1,100)))
total = 0 
for r in range(1,100):
    if r % 3 == 0:
        total += r
    elif r % 5 == 0:
        total += r

print(total)


print(list(range(1,100)))
total = 0 
for r in range(1,100):
    if r % 3 == 0 or r % 5 == 0:
        total += r

print(total)

    



list_0 = [7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7]
total_p = 0

d = len(list_0) - 1
while list_0[d] < 0:
    total_p = total_p + list_0[d]
    d = d -1
print(total_p)
