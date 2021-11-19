from .Team_def import *

from .match import scoring_chance

from.round_of_16_draw import *

import time

def CPU_match(team1, team2):
    
    minute = 1
    team1players = [team1.player2.name, team1.player3.name, team1.player4.name, team1.player5.name]
    team2players = [team2.player2.name, team2.player3.name, team2.player4.name, team2.player5.name]
    team1score = []
    team2score = []
    potentacy = ((team1.attacking+team2.attacking)*(team1.defending+team2.defending))/(10*(team1.overall+team2.overall)**2)
    
    while minute <= 70:
        
        attackingteam = scoring_chance(team1, team2)
        if attackingteam is team1.name:
            team1goal = random.randint(1, team1.attacking)*potentacy
            team2defend = random.randint(1, team2.defending)
            if team1goal > team2defend:
                team1score.append('team1')
        if attackingteam is team2.name:
            team2goal = random.randint(1, team2.attacking)*potentacy
            team1defend = random.randint(1, team1.defending)
            if team2goal > team1defend:
                team2score.append('team2')
        minute += 1
        
    if len(team1score) != len(team2score):
            
            print(team1.name, len(team1score)," - ", len(team2score),team2.name)
   
    else:
                
        while len(team1score) == len(team2score):
            
            attackingteam = scoring_chance(team1, team2)
            
            if attackingteam is team1.name:

                team1goal = random.randint(1, team1.attacking)*potentacy
                team2defend = random.randint(1, team2.defending)
                if team1goal > team2defend:
                    team1score.append("team1")
                    
            if attackingteam is team2.name:

                team2goal = random.randint(1, team2.attacking)*potentacy
                team1defend = random.randint(1, team1.defending)
                if team2goal > team1defend:
                    team2score.append("team2")
                    
            minute += 1
            
            if len(team1score) != len(team2score):
                print(team1.name, len(team1score)," - ", len(team2score),team2.name, " (after extra-time)")
                break
            
         
    if len(team1score) < len(team2score):
        
        return team2
    
    if len(team1score) > len(team2score):
        
        return team1

def create_semifinalists():
    return []

semifinalists=create_semifinalists()

def quarter_finals_draw(team):

    if len(semifinalists) < 1:

        quarterfinalteams=list(quarterfinalists)
        sfmatchday=[]
        opponent = random.choice(quarterfinalteams)
        quarterfinalteams.pop(quarterfinalteams.index(opponent))
        otherteams2 = sorted(quarterfinalteams, key=lambda team: team.name)
        i = 0

        print(team.name, " v ", opponent.name)
        time.sleep(1)

        while i<2:

            otherteams2.reverse()
            hometeam = otherteams2.pop(int((len(otherteams2)-1)/2))
            awayteam = otherteams2.pop(int((len(otherteams2)+1)/2))
            sfmatchday.append((hometeam, awayteam))
            print(hometeam.name, " v ", awayteam.name)
            time.sleep(1)
            i += 1

        lasthometeam = otherteams2.pop()
        lastawayteam = otherteams2.pop()
        sfmatchday.append((lasthometeam, lastawayteam))
        print(lasthometeam.name, " v ", lastawayteam.name)  
        teamt1,teamt2 = zip(*sfmatchday)
        team1 = list(teamt1)
        team2 = list(teamt2)
        q = 0

        print()
        print("Results:")  

        while q < 3:
            
            time.sleep(1)
            print()          
            quarterfinalgames = CPU_match(team1.pop(),team2.pop())
            semifinalists.append(quarterfinalgames)
            q += 1
            
    else:

        semifinalists.clear()
        raise ValueError('You already have the Semi-finalists')   
