from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master = input("What is the master password? ")
key = load_key() + (master.encode())
fer = Fernet(key)

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passcode, number = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passcode.encode()).decode(), "| Phone number: ", 
            fer.decrypt(number.encode()).decode())
 
def add(): 
    name = input("Account name: ")
    password = input("Password: ")
    phone_number = input("Phone number: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "|"+ fer.encrypt(phone_number.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (add, view)? Or type 'q' to quit: ")
    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "q":
        break
    else:   
        print("Invalid response, please try again")
        continue
