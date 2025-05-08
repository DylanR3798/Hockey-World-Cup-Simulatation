import argparse
import random
from hockey_sim.teams import NED, IND, AUS, GER, BEL, ENG, ESP, ARG, RSA, PAK, NZL, IRL, WAL, AUT, MAL, SCO
from hockey_sim.tournament.tournament_manager import TournamentManager

def main():
    teams = {
        "NED": NED,
        "IND": IND,
        "AUS": AUS,
        "GER": GER,
        "BEL": BEL,
        "ENG": ENG,
        "ESP": ESP,
        "ARG": ARG,
        "RSA": RSA,
        "PAK": PAK,
        "NZL": NZL,
        "IRL": IRL,
        "WAL": WAL,
        "AUT": AUT,
        "MAL": MAL,
        "SCO": SCO
    }

    parser = argparse.ArgumentParser(description="Play the Hockey World Cup!")
    parser.add_argument("--team", help="Choose your team code", required=True)
    args = parser.parse_args()

    team_code = args.team.upper()
    user_team = teams.get(team_code)

    if not user_team:
        print("Invalid team code. Please choose from:", ", ".join(teams.keys()))
        return

    all_teams = list(teams.values())
    if user_team not in all_teams:
        all_teams.append(user_team)

    print(f"\nYou selected: {user_team.name}\n")
    tm = TournamentManager(user_team=user_team, round_of_16=all_teams)
    tm.run_tournament()

if __name__ == "__main__":
    main()
