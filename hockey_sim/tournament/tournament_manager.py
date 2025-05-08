import random
import time
from hockey_sim.engine.matchsimulator import MatchSimulator
from hockey_sim.engine.World_Cup_Final import World_Cup_Final

class TournamentManager:
    def __init__(self, user_team, round_of_16):
        self.user_team = user_team
        self.round_of_16_teams = round_of_16

    def cpu_match(self, team1, team2):
        sim = MatchSimulator(team1, team2, live=False)
        return sim.simulate()

    def simulate_round(self, user_team, teams, round_name):
        print(f"\n=== {round_name.upper()} DRAW ===")
        remaining_teams = list(teams)
        opponents = sorted([t for t in remaining_teams if t != user_team], key=lambda t: t.name)

        # Draw user match
        user_opponent = random.choice(opponents)
        opponents.remove(user_opponent)
        remaining_teams.remove(user_opponent)
        remaining_teams.remove(user_team)

        print(f"{user_team.name} vs {user_opponent.name}")
        user_sim = MatchSimulator(user_team, user_opponent, live=True)
        user_winner = user_sim.simulate()

        if user_winner != user_team:
            print("\nYou have been knocked out of the tournament. Better luck next time!")
            return None

        print("\nYou are through! Simulating the rest of the matches...")
        time.sleep(1)

        # Simulate all other matches
        random.shuffle(remaining_teams)
        cpu_winners = []
        for i in range(0, len(remaining_teams), 2):
            t1, t2 = remaining_teams[i], remaining_teams[i+1]
            print(f"{t1.name} vs {t2.name}")
            winner = self.cpu_match(t1, t2)
            print(f"{winner.name} wins\n")
            time.sleep(0.5)
            cpu_winners.append(winner)

        # Combine winners and shuffle for next round
        next_round_teams = [user_team] + cpu_winners
        random.shuffle(next_round_teams)

        print("\nMatchups for the next round:")
        for i in range(0, len(next_round_teams), 2):
            print(f"{next_round_teams[i].name} vs {next_round_teams[i+1].name}")
        time.sleep(1)

        return next_round_teams
    
        # Ensure even number of teams
        if len(remaining_teams) % 2 != 0:
            raise ValueError("Unexpected number of remaining teams. Cannot form pairs.")
        
    def run_tournament(self):
        qf = self.simulate_round(self.user_team, self.round_of_16_teams, "Round of 16")
        if not qf:
            return

        sf = self.simulate_round(self.user_team, qf, "Quarter Finals")
        if not sf:
            return

        fn = self.simulate_round(self.user_team, sf, "Semi Finals")
        if not fn:
            return

        print("\n=== WORLD CUP FINAL ===")
        opponent = [t for t in fn if t != self.user_team][0]
        World_Cup_Final(self.user_team, opponent)
