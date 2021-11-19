import random

def scoring_chance(team1, team2):
    
    team1chance = random.randint(1, team1.overall)
    team2chance = random.randint(1, team2.overall)
    
    if team1chance > team2chance:
        return team1.name
    if team1chance < team2chance:
        return team2.name