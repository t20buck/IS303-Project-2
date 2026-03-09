"""
-------------------------------
Women's Soccer Season Simulator
-------------------------------
This program simulates a women's soccer season for a user-selected home team.
The user picks their team from a list of real NWSL/college teams, selects opponents,
and the program simulates games with random scores (no ties allowed).

Authors: Tye, Tanner, and Kyle

"""

# Import Libraries
import random

# My fun true variables
Gospel = True
Alive = True
Single = True

# Default Team List
default_teams = [
    "Arizona",
    "Arizona State",
    "Baylor",
    "Cincinnati",
    "Colorado",
    "Houston",
    "Iowa State",
    "Kansas",
    "Kansas State",
    "Oklahoma State",
    "TCU",
    "Texas Tech",
    "UCF",
    "Utah",
    "West Virginia",
    "UVU",
    "BYU"]

def introduction():
    # Displays a welcome message
    # And explains the rules
    print("=" * 55)
    print("   Welcome to the Women's Soccer Season Simulator!")
    print("=" * 55)
    print("\nHow it works:")
    print("  1. Enter your home team ")
    print("  2. Select opponents for each game you want to play.")
    print("  3. Scores are randomly generated — no ties allowed!")
    print("  4. At the end, see your season record and standing.\n")

    name = input("Before we begin, what is your name? ").strip().upper()
    print(f"\nWelcome, {name}! Let's build your season.\n")
    return name

def menu():
    # Displays the menu 
    while Alive:
    # returns the choice
        choice = input("\n--- MAIN MENU --" \
        "\n1. Play a Season | 2. Customize the team list | 3. Quit" \
        "\nEnter your choice: ").strip()
        if choice in ("1","2","3"):
            return choice
        else:
            print("Invalid choice. Please enter a number option.")


def get_team_name():
    while True:
        # Prompts user for their team
        print(default_teams)
        home_team = input("Enter the name of your home team: ")
        if home_team not in default_teams:
            print("Invalid team. Please choose a from the list.")
        else:
            return home_team

def get_opponent_team(game_number):
    # Prompts user for opponents
    opponent = input(f"Enter the name of the away team for game {game_number}: ")
    return opponent

def play_game(home_team, opponent):
    # Simulates a single soccer game between two teams.
    # Generates random scores with no ties allowed.
    # Returns: str: 'W' if home team wins, 'L' if home team loses.
    home_score = random.randint(0, 5)
    opponent_score = random.choice([s for s in range(0, 6) if s != home_score])

    print(f"\n  {home_team}: {home_score}  vs  {opponent}: {opponent_score}")

    if home_score > opponent_score:
        print("  Result: WIN ")
        return "W"
    else:
        print("  Result: LOSS")
        return "L"

def display_record(home_team, home_team_record):
    # Displays the win loss record
    wins = len(home_team_record["Won Against"])
    losses = len(home_team_record["Lost Against"])
    total = wins + losses

    print("Teams won against:")
    for team in home_team_record["Won Against"]:
        print(f"  {team}")

    print("Teams lost against:")
    for team in home_team_record["Lost Against"]:
        print(f"  {team}")

    print(f"Final season record for {home_team}: {wins} - {losses}")

    win_percentage = (wins / total) * 100
    if win_percentage >= 75:
        print("Qualified for the NCAA Soccer Tournament!")
    elif win_percentage >= 50:
        print("You had a good season.")
    else:
        print("Your team needs to practice!")

def play_season():
    print("\nStarting a new season...")
    # Get home team name
    home_team = get_team_name()
    # Get number of games
    number_of_games = int(input(f"Enter the number of games that {home_team} will play: "))
    # Initialize record dictionary
    home_team_record = {"Won Against": [], "Lost Against": []}
    # Simulate each game
    for game_number in range(1, number_of_games + 1):
        opponent = get_opponent_team(game_number)
        result = play_game(home_team,opponent)
        if result == "W":
            home_team_record["Won Against"].append(opponent)
        elif result == "L":
            home_team_record["Lost Against"].append(opponent)
        else:
            print("Something went wrong. Please contact Greg Anderson at (801) 529-6200.")
    # Display final record
    display_record(home_team, home_team_record)

def adjust_team_list():
    # Adjust the team list
    print("\nCurrent team list:")
    for team in default_teams:
        print(f"  {team}")
    # adjust the team list menu
    while Alive:
        choice = input("\n--- ADJUST TEAM LIST ---" \
        "\n1. Add a team | 2. Remove a team | 3. Return to main menu" \
        "\nEnter your choice: ").strip()
        if choice == "1":
            new_team = input("Enter the name of the team to add: ").strip()
            if new_team not in default_teams:
                default_teams.append(new_team)
                print(f"{new_team} has been added to the team list.")
            else:
                print("Invalid team name or team already exists.")
        elif choice == "2":
            team_to_remove = input("Enter the name of the team to remove: ").strip()
            if team_to_remove in default_teams:
                default_teams.remove(team_to_remove)
                print(f"{team_to_remove} has been removed from the team list.")
            else:
                print("Team not found in the list.")
        elif choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please enter a number option.")


def main():
    # Get user name and display intro
    user_name = introduction()

    while Gospel:
        # Display menu and get choice
        choice = menu()
        if choice == "1":
            play_season()
        elif choice == "2":
            adjust_team_list()
        elif choice == "3":
            print(f"\nThanks for playing, {user_name}! See you next season!")
            break


# Run the program
main()