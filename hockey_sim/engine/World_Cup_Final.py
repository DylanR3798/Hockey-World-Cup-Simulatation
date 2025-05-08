from hockey_sim.engine.matchsimulator import MatchSimulator

class FinalMatchSimulator(MatchSimulator):
    def simulate(self):
        print("Welcome to the final of the Hockey World Cup\n")
        while self.minute <= 70:
            self._simulate_minute()
            self.minute += 1
            if self.live:
                if self.minute == 35:
                    print(f"Half-time: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}\n")
                    print(f"We are underway here for the second half of this World Cup Final between {self.team1.name} and {self.team2.name}\n")
                    time.sleep(2)
                time.sleep(0.5)

        if self.live:
            print(f"Full-time: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}\n")

        if self.team1_score == self.team2_score:
            print("It's all square here after full time. We are going to golden goal!\n")
            self._golden_goal()

        winner = self.team1 if self.team1_score > self.team2_score else self.team2
        print(f"Unbelievable! {winner.name} are World Champions!!!\n")
        print(f"Final Score: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}")
        return winner


def World_Cup_Final(team1, team2):
    sim = FinalMatchSimulator(team1, team2, live=True)
    return sim.simulate()
