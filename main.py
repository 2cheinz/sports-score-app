# main file for running

from user_actions import search_teams_menu, view_favorites

def display_main_menu():
    print("\nWelcome to the NFL Team Tracker!")
    print("\nThis is an application to follow all your favorite NFL teams and stay updated on their team information including stadium information, historical results, and statistics - all in one easily accessible app!")
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
