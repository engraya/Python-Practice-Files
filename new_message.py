from fileinput import filename


filename = 'core_status.txt'

with open(filename, 'w') as file_object:
    file_object.write("I adhere to my principles anytime")
    file_object.write("I respect peole")
    file_object.write("I do call for help sometimes")



with open(filename, 'w') as file_object:
    file_object.write("I adhere to my principles anytime\. \n)
    file_object.write("I respect peole. \n")
    file_object.write("I do call for help sometimes. \n")


with open(filename, 'a') as file_object:
    file_object.write("my feelings for my country willl be forever." \n)
    file_object.write("I lovre dedication. \n")
    file_object.write("I am ready to help everyone. \n")
