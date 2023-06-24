from fileinput import filename
import json

def welcome_user():
    """say hi to the new user"""
    filename = 'profile_name.json'
    try:
        with open(filename) as p:
            profile_name = json.load(p)
    except FileNotFoundError:
        profile_name = input('Enter your name!  ')
        with open(filename, p):
            json.dump(profile_name, p)
            print(f"welcome back, {profile_name}, you can now access all your data fro backup!!!")
    else:
        print(f"your data is now saved {profile_name}, Thank you for your patronage!!!")

welcome_user()




