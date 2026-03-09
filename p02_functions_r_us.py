"""This program simulates the results of soccer games for a specified home team.
It prompts the user for the home team name and the number of games to simulate,
then generates random scores for each game and displays the results.
Author: Kyle Pinkney, Tye Buckley, """

import random

# Get user input for home team and number of games
home_team = input("Enter the name of your home team: ")
number_of_games = int(input(f"Enter the number of games that {home_team} will play: "))

# Initialize lists and dictionary to store game data
opponent_teams = []
opponent_scores = []
home_team_scores = []
home_team_record = {"Won Against": [], "Lost Against": []}

# Simulate each game
for game_number in range(number_of_games):
    opponent_teams.append(input(f"Enter the name of the away team for game {game_number + 1}: "))
    home_score = random.randint(0, 3)
    opponent_score = random.choice([i for i in range(0, 4) if i != home_score])
    home_team_scores.append(home_score)
    opponent_scores.append(opponent_score)
    print(f"{home_team}'s score: {home_score} - {opponent_teams[game_number]}'s score: {opponent_score}")

# Determine win/loss record
for i in range(number_of_games):
    if home_team_scores[i] > opponent_scores[i]:
        home_team_record["Won Against"].append(opponent_teams[i])
    else:
        home_team_record["Lost Against"].append(opponent_teams[i])

# Display results
wins = 0 
losses = 0

print("Teams won against:")
for i in range(len(opponent_teams)):
    if opponent_teams[i] in home_team_record["Won Against"]:
        print(f"  {opponent_teams[i]}")
        wins += 1

print("Teams lost against:")
for i in range(len(opponent_teams)):
    if opponent_teams[i] in home_team_record["Lost Against"]:
        print(f"  {opponent_teams[i]}")
        losses += 1

# Final Season Record 
print(f"Final season record: {wins} - {losses}")

win_percentage =   (wins/number_of_games)* 100
if win_percentage >= 75:
    print("Qualified for the NCAA Soccer Tournament!")
elif win_percentage >= 50:
    print("You had a good season.")
elif win_percentage < 50:
    print("Your team needs to practice!")
