from datetime import datetime

def register(found):
    username = input("Enter your username: ")
    for char in username:
        if char == ';': 
            print("Your username can't contain the following character: ;")
            found = False
            return False
    with open("accountdetails.txt", "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(";")
            if username == saved_username:
                print("An account with this username already exists!")
                return False
    file.close()

    password = input("Enter your password: ")
    for char in password:
        if char == ';': 
            print("Your username can't contain the following character: ;")
            found = False
            return False
        
    found = True
    file = open("accountdetails.txt", "a")
    file.write(username + ";" + password + "\n")
    file.close()

   
    if found == True:
        print("Account registed successfully. Welcome " + username + "!")
    else:
        print("Error registering account.")
    return found

def login(found):
    
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
        return True
    else:
        print("Invalid Username or Password!")
        return False

def main():


    found = False
    while (found == False):
        time = datetime.now()
        
        option = input("Enter an option: \n1. Register\n2. Login\n3. Exit Program\n")
        if (option == '1'):
            found = register(found)
            if found == True:
                current_time = time.strftime("%H:%M:%S")
                current_date = time.strftime("%m/%d/%Y")
                print("Register timestamp: " + current_time + "\nRegister date: " + current_date)
        elif (option == '2'):
            found = login(found)
            if found == True:
                current_time = time.strftime("%H:%M:%S")
                current_date = time.strftime("%m/%d/%Y")
                print("Login timestamp: " + current_time + "\nLogin date: " + current_date)
        elif(option == '3'):
            print("")
            exit()
        else:
            print("That is not a valid option!")
            

    
if __name__ == '__main__':
    main()
