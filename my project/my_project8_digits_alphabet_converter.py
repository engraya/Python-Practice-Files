print("****Enter your Phone number here ot convert it into words****")
Telephone = input(" Enter your Phone Number here: ")
print("***********|||||||||||*********")
digits_mapping = {
    "0" : "Zero",
    "1" :  "one",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
output = ""
for characters in Telephone:
    output += digits_mapping.get(characters, "!") + " "
print(f"Digits Phone Number: {Telephone}")
print(f"Alphabetic Phone Number: {output}")
