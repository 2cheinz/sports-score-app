# user actions file for all actions that user may do

from data import AFC_TEAMS, NFC_TEAMS, user_favorites

# initial search for teams menu, view by conference or view all teams
def search_teams_menu():
    while True:
            print("\nSEARCH FOR TEAMS")
            print("\n- How would you like to search for teams to follow?")
            print("-------------------------------------------------------")
            print("1. View Teams by Conference (AFC/NFC)")
            print("2. View All Teams")
            print("3. Back to Main Menu")

            user_choice = input("Enter your choice (1-3): ")

            if user_choice == "1":
                  show_teams_by_conference()
            elif user_choice == "2":
                  show_all_teams()
            elif user_choice == "3":
                  return
            else:
                  print("Invalide Input! Please enter a number between 1-3")