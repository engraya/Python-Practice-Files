from fileinput import filename
import json

profile_name = input('Enter your username here please!  ')

filename = 'profile_name.json'

with open(filename, 'w') as p:
    json.dump(profile_name, p)
    print(f" Dear {profile_name}, we will save all your information when you need any backup!")
