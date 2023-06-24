from importlib.resources import contents

filename = 'my_annecdotes.txt'

try:
    with open(filename) as bb:
        contents = bb.read()
except FileNotFoundError:
    print(f"sorry! we couldnt find the {filename}  file")
else:
    highligths = contents.split()
    capacity = len(highligths)
    print(f"the {filename} contains approximately {capacity}......")


# title = "my name is ahmad"
# title.split()
# print(title.split())
