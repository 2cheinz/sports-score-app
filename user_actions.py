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

# search option for viewing teams by conference
def show_teams_by_conference():
    while True:
        print("\nVIEW TEAMS BY CONFERENCE")
        print("\n- Select a conference, AFC or NFC to view teams from the selected conference")
        print("--------------------------------------\n")
        print("1. AFC")
        print("2. NFC")
        print("3. Back to Search Menu")

        conference_choice = input("\nEnter your choice (1-3): ")

        if conference_choice == "1":
            print("\nAFC TEAMS\n")
            for team in AFC_TEAMS:
                    print(f"- {team}")
            decision = input("\nType the team name EXACTLY as is to follow them. Press 3 to return to the conference menu: ")
            if decision in AFC_TEAMS:
                 add_to_favorites(decision)
            elif decision == "3":
                search_teams_menu()
            else:
                 print("Invalid Selection. Try Again!")
        elif conference_choice == "2":
            print("\nNFC TEAMS\n")
            for team in NFC_TEAMS:
                    print(f"- {team}")
            decision = input("\nType the team name EXACTLY as is to follow them. Press 3 to return to the conference menu: ")
            if decision in NFC_TEAMS:
                 add_to_favorites(decision)
            elif decision == "3":
                search_teams_menu()
            else:
                 print("Invalid Selection. Try Again!")
        elif conference_choice == "3":
            return
        else:
            print("Invalid Selection. Try Again")
        
def show_all_teams():
    while True:
        print("\nViewing All NFL Teams")
        print("\n-------------------------------\n")
        ALL_TEAMS = AFC_TEAMS + NFC_TEAMS
        for team in ALL_TEAMS:
            print(f"- {team}")
        
        decision = input("\nType the team name EXACTLY as is to follow them. Press 3 to return to the conference menu: ")
        
        if decision in ALL_TEAMS:
            add_to_favorites(decision)
        elif decision == "3":
            return
        else:
            print("\nInvalid Selection. Try Again!")
        

def add_to_favorites(team_name):
    if team_name in user_favorites:
        print(f"{team_name} is already in your favorite teams list!")
    else:
        user_favorites.append(team_name)
        print(f"{team_name} has been added to your favorite teams list!")
    input("\nPress 'Enter' to return to the view all teams menu: ")


def view_favorites():
    while True:
        print("\nYOUR FAVORITE TEAMS")
        print("---------------------------\n")

        if not user_favorites:
            print("You have not followed any teams yet.")
            input("\nPress Enter to return to the main menu: ")
            return

        for team in user_favorites:
            print(f"- {team}")

        print("\nOptions:")
        print("1. View team info (COMING IN A LATER SPRINT - MICROSERVICE)")
        print("2. Unfollow a team")
        print("3. Back to Main Menu")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            team_name = input("Enter the FULL name of the team you want to view more info for: ")
            if team_name in user_favorites:
                print(f"\nStadium Info for {team_name}:")
                print("Stadium: Placeholder Stadium")
                print("Location: Placeholder City, State")
                print("Capacity: 65,000 (estimated)")
                print("\n(Note: Actual stadium data will be added in a future update.)")
            else:
                print("The team you selected is not in your favorites, try again!")
            input("\nPress Enter to return to the main menu")
        elif choice == "2":
            team_name = input("Enter the FULL name of the team to unfollow: ")
            if team_name in user_favorites:
                print(f"\nYou've selected to unfollow {team_name}. You will no longer be able to receive updates or be able to view them in your favorites list.\n")
                confirm = input(f"Are you sure you want to unfollow {team_name}? (yes/no): ")
                if confirm == "yes":
                    user_favorites.remove(team_name)
                    print(f"{team_name} has been removed from your favorites.")
                else:
                    print("Canceled.")
            else:
                print("That team is not in your favorites.")
            input("\nPress 'Enter' to return to the 'Favorites' menu: ")
        elif choice == "3":
            return
        else:
            print("Invalid Selection. Try Again (select 1-3).")
            

            
