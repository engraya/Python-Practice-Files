from cryptography.fernet import Fernet



# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    file = open("key.key", "rb").read()
    key = file.read()
    file.close()
    return key


master_password = input("Wat is the master Password? ")

key = load_key() + master_password.encode()
fer = Fernet(key)

# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)




def view():
    with open('passwords.txt', 'r') as password_file:
        for line in password_file.readlines():
            print(line)
        
def add():
    name = input("Account Name: ")
    password = input("Account Password: ")

    with open('passwords.txt', 'a') as password_file:
        password_file.write(name + '|' + str(fer.encrypt(password.encode())) + "\n")

while True: 
    mode = input(" Would you like to view or add password? ")
    if mode == 'q':
        break

    if mode == 'view':
        view()

    if mode == 'add':
        add()

    else:
        print("Invalid mode")
        continue