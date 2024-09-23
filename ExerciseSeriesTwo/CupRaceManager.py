# Problem 2
# A cup race system manager

import random

teams = input("Enter the name of teams: (example: team1_team2_team3_...etc): ").split('_')
teams_remaining = []
round_counter = 1
while True:
    print(f"--- Round {round_counter} ---")
    while len(teams) > 0:
        if len(teams) == 1:
            # if only one team remains without any rival, it'll get to the next round!
            teams_remaining.append(teams[0])
            teams.clear()
        teamRight = random.choice(teams)
        teams.remove(teamRight)
        teamLeft = random.choice(teams)
        teams.remove(teamLeft)
        print(f'Match: Team {teamRight} vs {teamLeft}')
        winner = random.choice([teamRight, teamLeft])
        print(f'Winner: Team {winner}')
        teams_remaining.append(winner)
    if len(teams_remaining) == 1:
        print(f'winner of the tournament: Team {teams_remaining[0]}')
        # exit condition of the infinite loop
        break
    print("Teams remaining:")
    for t in teams_remaining:
        print(f"- Team {t}")
    round_counter += 1
    teams = teams_remaining
    teams_remaining = []

