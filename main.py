# main file for running

from user_actions import search_teams_menu, view_favorites

def display_main_menu():
    print("\nWelcome to the Sports Team Tracker!")
    print("\nThis is the place to be to track all of your favorite teams and have the information about them all in one place!")
    print("\nWhat would you like to do?\n")
    print("1. Search for Teams")
    print("2. View Favorite Teams")
    print("3. Exit Program")

def main():
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
