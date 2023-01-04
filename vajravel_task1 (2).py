#Registration and login system, file handling - task 1
import re
email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pwd_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')

#username validation
def mail_validation(email):
    if re.fullmatch(email_regex, email):
        return True
    else:
        return False

#password validation    
def pwd_validation(pwd):
    if re.fullmatch(pwd_regex, pwd):
        return True
    else:        
        return False

#register the username using emailID
def register():
        email = input ("Enter your emailID: ")
        db = open ("vajravel_task1_up.py", "r")
        info = db.read()
        if email in info:
            print ("Username already exists, please try again...")
        if mail_validation:
                pwd = input ("Create a password: ")
                if pwd_validation:
                    print ("Congrats! Username successfully registered")
                else:
                    print ("Invalid password, please try again...")
        db = open ("vajravel_task1_up.py", "w")
        info = (email+ " " + pwd)
        db.write(info)
        db.close()
        
#login using the existing username
def login():
    email = input("Enter your emailID: ")
    pwd = input("Please enter your password: ")
    db = open ("vajravel_task1_up.py", "r")
    info = db.read()
    info = info.split()
    db.close()
    if email in info:
                index = info.index(email) + 1
                usr_password = info[index]
                if usr_password == pwd:
                    print ("Success!! Access Granted")
                else:
                    print ("Invalid password, please try again...")
    else:
        print ("Entered emailID is not found, please register to continue...")

#retrive forgotten password
def forget_password( ):
    email = input("Enter your emailID: ")
    db = open ("vajravel_task1_up.py", "r")
    info = db.read()
    info = info.split()
    if email in info:
                index = info.index(email) + 1
                usr_password = info[index]
                print ("your password is", usr_password)
    else:
        print ("user not found, please register...")

if __name__ == "__main__":
    try:
        while True:
            print(''' \nPlease select an option \n
                1. Register
                2. Login
                3. Forget Password
                ''')
            option = int(input())
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forget_password()
            else:
                print("Invalid Option")
    except:
        print("An exception occurred")