# main file for running

from user_actions import search_teams_menu, view_favorites
from login_actions import login, create_account, validate, logout

def login_menu():
    print("Welcome to the NFL Team Tracker Application! Please log in or create an account to continue.")
    while True:
        print("\n1. Log In")
        print("2. Create Account")
        print("3. Exit Program")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            token = login(username, password)
            if token:
                print("Login successful!")
                return token
            else:
                print("Login failed. Please try again.")
        elif choice == "2":
            username = input("New username: ")
            password = input("New password: ")
            new_account = create_account(username, password)
            if new_account:
                print("Account created successfully. Now you can login!")
            else:
                print("Account creation failed. Try a different username and password combo.")
        elif choice == "3":
            print("Closing Application, goodbye!")
            exit()
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def display_main_menu():
    print("\nWelcome to the NFL Team Tracker!")
    print("\nThis is an application to follow all your favorite NFL teams and stay updated on their team information including stadium information, historical results, and statistics - all in one easily accessible app!")
    print("\nWhat would you like to do?\n")
    print("1. Search for Teams")
    print("2. View Favorite Teams")
    print("3. Exit Program")

def main():
    token = login_menu()
    while True:
        display_main_menu()
        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            search_teams_menu()
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            print("Thanks for using the Sports Score Tracker, have a good day!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
