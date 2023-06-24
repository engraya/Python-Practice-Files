solutions = [2,2,4,5,6,7,8,9,0,6,4,5,43,54]
print(solutions)


# append only carries on argument
solutions.append(0)
solutions.append(900)
solutions.append('HELLO')
solutions.append('marakesh')


#a list can be added to an existing list through append command
solutions.append([5,6,78,9,0,0,7,6,7,4,45,6466556577,9,0,87])
solutions.append('popularity')
solutions.append('google')
print(solutions)
solutions.pop()
print(solutions)
print(solutions[5])
solutions[3] = 'MOTHER SOLUTIONS:'
print(solutions)


#exchanging the index position of values in a list
#method no.1 
temp = solutions[0]
solutions[0] = solutions[3]
solutions[3] = solutions[0]
print(solutions)
# method no.2
solutions[4], solutions[11] = solutions[11], solutions[4]
print(solutions)
