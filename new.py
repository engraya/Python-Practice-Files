# with open('technology.txt') as result:
#     all = result.read()
#     print(all)

import keyword


new_list = []
for all in keyword.kwlist:
    new_list.append(all)
print(new_list)


for all_values in new_list:
    print(all_values)

# from ast import keyword


# brand = "lenovo"
# print(type(brand))

# print(keyword)
