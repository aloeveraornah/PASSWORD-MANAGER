from cryptography.fernet import Fernet

#the multi line comments below are used to create and open another file that holds the encryption for the master password
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()
'''

def load_key(): 
    file = open("key.key", "rb") #this line opens the file "key.key" which holds the input encrypted master password
    key = file.read()
    file.close()
    return key

master = input("What is the master password? ")
key = load_key() + (master.encode())
fer = Fernet(key)
 
def view(): 
    with open("passwords.txt", "r") as f: #this line opens the file "passowords.txt" and the input encrypted information of the user is printed here
        for line in f.readlines():
            data = line.rstrip()
            user, passcode, number = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passcode.encode()).decode(), "| Phone number: ", 
            fer.decrypt(number.encode()).decode())
            #the two lines above decrypts the encrypted information (from function add()) of the user and prints them out
 
def add(): #this prompts users to enter their name, password, and phone number
    name = input("Account name: ")
    password = input("Password: ")
    phone_number = input("Phone number: ")
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "|"+ fer.encrypt(phone_number.encode()).decode() + "\n")
        #the line above encrypts what the user inputs so that it cannot be revealed in the other folders

while True: #this line assures that the user must either add/view infor or quit in the game
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
