def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    file = open("accountdetails.txt", "a")
    file.write(username + ";" + password + "\n")
    file.close()

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    found = False

    with open("accountdetails.txt", "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(";")
            if username == saved_username and password == saved_password:
                found = True
                break
            
    if (found == True):
        print("Login Successful!")
    else:
        print("Invalid Username or Password!")

def main():
    option = input("Enter an option: \n1. Register\n2. Login\n")
    if (option == '1'):
        register()
    elif (option == '2'):
        login()
    else:
        print("That is not a valid option!")

if __name__ == '__main__':
    main()
