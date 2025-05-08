import time
import random

class MatchSimulator:
    def __init__(self, team1, team2, live=True):
        self.team1 = team1
        self.team2 = team2
        self.live = live
        self.minute = 1
        self.team1_score = 0
        self.team2_score = 0
        self.potency = self._calculate_potency()
        self.team1players = [team1.player2.name, team1.player3.name, team1.player4.name, team1.player5.name]
        self.team2players = [team2.player2.name, team2.player3.name, team2.player4.name, team2.player5.name]
        self.probs = [0.1, 0.225, 0.225, 0.45]
        self.goal_comments = [" with just the keeper to beat!", " hits it from the top of the D.", " there to tap it in at the back post."]
        self.probs2 = [0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1]

    def _calculate_potency(self):
        return ((self.team1.attacking + self.team2.attacking) *
                (self.team1.defending + self.team2.defending)) / \
               (10 * (self.team1.overall + self.team2.overall) ** 2)

    def _scoring_chance(self):
        t1_chance = random.randint(1, self.team1.overall)
        t2_chance = random.randint(1, self.team2.overall)
        if t1_chance > t2_chance:
            return self.team1
        elif t2_chance > t1_chance:
            return self.team2
        else:
            return random.choice([self.team1, self.team2])

    def _choose_player(self, players):
        return random.choices(players, weights=self.probs, k=1)[0]

    def _commentary(self, attacking_team, defending_team):
        atk_players = [attacking_team.player2.name, attacking_team.player3.name, attacking_team.player4.name, attacking_team.player5.name]
        def_players = [defending_team.player2.name, defending_team.player3.name, defending_team.player4.name, defending_team.player5.name]

        atk_player = self._choose_player(atk_players)
        def_player = self._choose_player(def_players)

        GSFPC = [' with just the keeper to beat!', ' hits it from the top of the D.', ' there to tap it in at the back post.']
        PFCC = [' in possession at the moment passing it round the back.', ' win a long corner.', ' under pressure now.']
        PFPC = [' plays a long ball forward', ' cuts in from the right.', ' cuts in from the left.']
        PEPPC = [' goes round ', ' intercepts the ball due to a poor pass by ']
        APFPC = [' centres it from the baseline.', ' slaps it to the back post.', ' wins a penalty corner.']

        possessioncomlist = [
            atk_player + random.choice(PFPC),
            attacking_team.name + random.choice(PFCC),
            'Lovely bit of skill from ' + atk_player + ' to get out of a sticky situation.',
            'Great pass from ' + atk_player,
            atk_player + random.choice(PEPPC) + def_player,
            atk_player + random.choice(APFPC),
            atk_player + random.choice(GSFPC),
            atk_player + ' gives away a foul in the D! Penalty corner to ' + defending_team.name
        ]

        if self.live:
            print(" ".join(random.choices(possessioncomlist, weights=self.probs2, k=1)))
            print()
            time.sleep(1)

    def _simulate_goal_attempt(self, attacking_team, defending_team, attacking_players):
        attack_strength = random.randint(1, attacking_team.attacking) * self.potency
        defense_strength = random.randint(1, defending_team.defending)

        if attack_strength > defense_strength:
            scorer = self._choose_player(attacking_players)
            comment = random.choice(self.goal_comments)
            if self.live:
                print(scorer + comment)
                print()
                print(f"{scorer} {self.minute}'")
                print()
                time.sleep(1)
            return True
        return False

    def _simulate_minute(self):
        attacking_team = self._scoring_chance()
        if attacking_team == self.team1:
            if self.minute % 5 == 0:
                self._commentary(self.team1, self.team2)
            if self._simulate_goal_attempt(self.team1, self.team2, self.team1players):
                self.team1_score += 1
        else:
            if self.minute % 5 == 0:
                self._commentary(self.team2, self.team1)
            if self._simulate_goal_attempt(self.team2, self.team1, self.team2players):
                self.team2_score += 1

    def _golden_goal(self):
        if self.live:
            print("It's all square after full time. Golden goal begins!")
            print()
        while self.team1_score == self.team2_score:
            self._simulate_minute()
            self.minute += 1
            if self.live:
                time.sleep(0.5)

    def simulate(self):
        if self.live:
            print("Push-Back\n")
        while self.minute <= 70:
            self._simulate_minute()
            self.minute += 1
            if self.live:
                time.sleep(0.5)
            if self.minute == 35 and self.live:
                print(f"Half-time: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}\n")
                time.sleep(2)
        if self.live:
            print(f"Full-time: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}\n")
        if self.team1_score == self.team2_score:
            self._golden_goal()
        if self.live:
            winner = self.team1 if self.team1_score > self.team2_score else self.team2
            print(f"{winner.name} have won it in extra time! Final Score: {self.team1.name} {self.team1_score} - {self.team2_score} {self.team2.name}\n")
        return self.team1 if self.team1_score > self.team2_score else self.team2
