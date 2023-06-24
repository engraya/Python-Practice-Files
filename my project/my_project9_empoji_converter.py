print("Enter your statement and see emoji converted")
message = input("Enter your statement and mood expression: ")
words = message.split(' ')
emojis = {
    ".happy" : "😁",
    ".sad" : "😯",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)