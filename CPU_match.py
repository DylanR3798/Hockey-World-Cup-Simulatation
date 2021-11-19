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
        