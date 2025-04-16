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

    personal_file_name = username + "timestamp.txt"
    print(personal_file_name)

    with open("accountdetails.txt", "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(";")
            if username == saved_username and password == saved_password:
                found = True
                break
    file.close()
    if (found == True):
        print("Login Successful!")
        time = datetime.now()
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%m/%d/%Y")
        print("Login timestamp: " + current_time + "\nLogin date: " + current_date)
        file = open(personal_file_name, "a")
        file.write(current_date + " at " + current_time)
        return True
    else:
        print("Invalid Username or Password!")
        return False


def main_menu():
    print("Welcome to PikUp")
    while(1):
        choice = input("Choose an option!\n1. Find events\n2. Create event\n3. Send message\n4. Logout\n")
        if choice == '1':
            sports_choice = input("Which Sport?\n1. Basketball\n2. Soccer\n3. Football\n4. Baseball\n5. Tennis\n6. Pickleball\n7. Volleyball\n")

            continue
        elif choice == '2':
            time = datetime.now()
            sports_choice = input("Enter Sport Name\n ")
            date = input("When will this event be? (mm/dd/yyy) - (hr:mn)\n ")
            location = input("Where will this event be held?\n ")
            description = input("Enter a brief description of the event:\n")
            file_name = sports_choice + date + location + ".txt"
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%m/%d/%Y")
            file = open(file_name, "w")
            file.write("Sport: " + sports_choice+ "\nDate: " + date + "\nLocation: " + location + "\nDescription: " + description + "\nEvent created: " +current_date + " at " + current_time + "\n")
            continue
        elif choice == '3':
            print("This feature is a work on progress.")
            continue
        elif choice == '4':
            print("See you soon!")
            exit()
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
                main_menu()
        elif(option == '3'): 
            exit()
        else:
            print("That is not a valid option!")
            

    
if __name__ == '__main__':
    main()
