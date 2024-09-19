#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void reg_account();
bool login(char *user, char *pass);
void send_message(char *username);

int main() {

    char username[50];
    char password[50];

    bool success;
    printf("Choose an option\n1. Register an account\n2. Login\n");
    int choice;
    scanf("%d", &choice);

    switch(choice) {
        case 1:
            reg_account();
            printf("Account Registered Successfully!\n");
            break;
        case 2:
            success = login(username, password);
            if (success == true) {
                printf("What would you like to do?\n1. Send message\n2. See Stats\n3. Logout\n");
                int decision;
                scanf("%d", &decision);
                switch (decision)
                {
                case 1:
                    send_message(username);
                    break;
                case 2:
                    //see_stats(username);
                    printf("This part is under construction for now\n");
                    break;
                case 3:
                    printf("Logging out... See you soon!\n");
                    break;
                default:
                    printf("That's Not An Option");
                    break;
                }
                
            }
            else {
                printf("Invalid Login.\n");
            }
            break;
        default:
            printf("Invalid option.\n");
            break;
    }
    

    return 0;
}


void reg_account() {

    //int ch;
    char user[40];
    char pass[30];

    printf("Enter a username: ");
    scanf(" %39s", user);
    
    printf("Enter a password: ");
    scanf(" %29s", pass);
    
    FILE *fp2 = fopen("username.txt", "r");
    if (fp2 == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    //grabs username from login to check if account with user already exists
    char buffer[40];
    while (fgets(buffer, sizeof(buffer), fp2)) {
        char existing_user[40];
        
        // Parse the username from the line
        if (sscanf(buffer, "%39[^:]:", existing_user) == 1) {
            if (strcmp(user, "jezzy") == 0) {
                printf("That's My Username!\n");
                exit(1);
             }
            else if (strcmp(user, existing_user) == 0) {
                printf("Account with this username already exists!\n");
                exit(1);
            }
        }
    }
    
    fclose(fp2);
    fp2 = NULL;

    FILE *fp = fopen("username.txt", "a");

    if (fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

   
    
        
    if ((strcmp(user, buffer) == 0)) {
        printf("Account with this username already exists!\n");
        exit(1);
    }
     
 
    printf("Welcome %s!\n", user);


    fprintf(fp, "%s: &&!!%s##$$\n", user, pass);
    //fscanf(fp, "%s: &&!!%s##$$\n", user, pass);

    fclose(fp);
    fp = NULL;

}

bool login(char *user, char *pass) {

    int ch;
    bool logged = false;
    char username[40];
    char passkey[30];

    char userfile[40];
    char passfile[30]; 
    
    FILE *fp = fopen("username.txt", "r");

    if (fp == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    printf("Enter your username: ");
    scanf(" %39s", username);
    
    printf("Enter your password: ");
    scanf(" %29s", passkey);

    strcpy(user, username);

    //fscanf(fp, "%[^:]: &&!!%[^#]##$$", userfile, passfile);

    //printf("%s %s\n", userfile, passfile);

    char buffer[100];
    while (fgets(buffer, sizeof(buffer), fp)) {
        userfile[0] = '\0';
        passfile[0] = '\0';
        if (sscanf(buffer, "%39[^:]: &&!!%29[^#]##$$\n", userfile, passfile) == 2) {
            if (strcmp(username, userfile) == 0 && strcmp(passkey, passfile) == 0) {
                logged = true;
                break; // Exit loop if match found
            }
        }
    }

    fclose(fp);
    fp = NULL;

    if (logged == true) {
        printf("\nLogin successful.\n");
        printf("Welcome %s!\n\n", user);
    }


    return logged;

}

void send_message(char *username) {

    FILE *fp = fopen("username.txt", "r");
    if (fp == NULL) {
        printf("Error opening file! (send_message)\n");
        exit(1);
    }

    int index = 0;
    char buffer[40];
    printf("Who would you like to send a message to (type username)?\n");
    while (fgets(buffer, sizeof(buffer), fp)) {
        char existing_user[40];
        
        // Parse the username from the line
        if (sscanf(buffer, "%39[^:]:", existing_user) == 1) {
            printf("%d: %s\n", index + 1, existing_user);
            index++;
        }

    }
    fclose(fp);
    fp = NULL;

    char recip[40];
    scanf(" %39s", recip);
    printf("recip: %s\n", recip);

    if ((strcmp(username, recip)) == 0) {
        printf("You can't message yourself (yet)\n");
        return;
    }

    char inputfile[120];
    strcpy(inputfile, username);
    strcat(inputfile, "-");
    strcat(inputfile, recip);
    strcat(inputfile, "-");
    strcat(inputfile, "convo.txt");
    //printf("input: %s\n", inputfile);

    FILE *fp2 = fopen(inputfile, "a");
    if (fp2 == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    char message[500];
    printf("Write Message (500 character limit): ");
    scanf(" %499s", message); // fix this, it only reads one word

    fprintf(fp2, "From (user) %s: %s\n", username, message);



}




//Encrypted file password is the filename itself
