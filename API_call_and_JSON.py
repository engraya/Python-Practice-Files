from urllib import request
import requests
import json
import pyttsx3


####### METHOD 1
url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(r)
print(r.getcode())
main_data = r.read()
json_main_data = json.loads(main_data)
print(json_main_data)

class Joke:

     def __init__(self, setup, punchline):
         self.setup = setup
         self.punchline = punchline

     def __str__(self) -> str:
         return f"setup: {self.setup}\n" \
                f"punchline : {self.punchline}\n"
jokes = []

for j in json_main_data:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f" A total of {len(jokes)} are gotten successfully______")
for joke in jokes:
    print(joke)




##### METHOD 2
url = "https://official-joke-api.appspot.com/random_ten"

response = requests.get(url)
print(response.status_code)


json_main_data = json.loads(response.text)
print(json_main_data)

class Joke:

     def __init__(self, setup, punchline):
         self.setup = setup
         self.punchline = punchline

     def __str__(self) -> str:
         return f"setup: {self.setup}\n" \
                f"punchline : {self.punchline}\n"
jokes = []

for j in json_main_data:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f" A total of {len(jokes)} are gotten successfully______")
for joke in jokes:
    print(joke)