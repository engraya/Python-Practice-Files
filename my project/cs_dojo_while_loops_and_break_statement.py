
# numbers_less_than_100 = list(range(1,100))
# total = 0
# for v in numbers_less_than_100:
#     total = total + v
# print(total)



# full_sum = 0
# a = 1
# while a < 100:
#     full_sum += a
#     a += 1
# print(full_sum)


# # addition of ements in a list that contain positive and negative numbers using while loop
# list_0 = [9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,]
# sum_all = 0 
# q = 0
# while list_0[q] > 0:
#     sum_all = sum_all + list_0[q]
#     q = q + 1
# print(sum_all)



# # addition of ements in a list that contain positive and negative numbers using while  loop
# list_0 = [9,8,7,6,5,4,3,2,1]
# sum_all = 0 
# q = 0
# while q < len(list_0) and list_0[q] > 0:
#     sum_all = sum_all + list_0[q]
#     q = q + 1
# print(sum_all)


# # addition of ements in a list that contain positive and negative numbers using for loop 
# list_0 = [9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,]
# total = 0 
# for elements in list_0:
#     if elements <= 0:
#         break
#     total = total + elements
# print(total)



# list_0 = [9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,]
# total_77 = 0
# k = 0
# while True:
#     total_77 += list_0[k]
#     k += 1
#     if list_0[k] <= 0:
#         break
# print(total_77)




list_0 = [9,8,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7,-8,-9,]
total = 0 
for elements in list_0:
    if elements >= 0:
        break
    total = total + elements
print(total)
