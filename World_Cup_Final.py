import time

import random

from .match import commentary, scoring_chance

def World_Cup_Final(team1, team2):
    
    minute = 1
    
    team1players = [team1.player2.name, team1.player3.name, team1.player4.name, team1.player5.name]
    team2players = [team2.player2.name, team2.player3.name, team2.player4.name, team2.player5.name]
    probs = [0.1,0.225,0.225,0.45]
    team1score = []
    team2score = []
    GSFPC = [" with just the keeper to beat!"," hits it from the top of the D."," there to tap it in at the back post."]

    
    potentacy = ((team1.attacking+team2.attacking)*(team1.defending+team2.defending))/(10*(team1.overall+team2.overall)**2)
    
    print("Welcome to the final of the Hockey World Cup")
    print()
    
    while minute <= 70:
        
        attackingteam = scoring_chance(team1, team2)
        
        if attackingteam is team1.name:
            
            if minute % 5 == 0:
                
                commentary(team1, team2)
                print()
                time.sleep(1)
                
            team1goal = random.randint(1, team1.attacking)*potentacy
            team2defend = random.randint(1, team2.defending)
            
            if team1goal > team2defend:
                
                team1score.append("team1")
                scorer1 = str(random.choices(team1players, weights=probs)).replace('[','').replace(']','').replace("'",'')
                comment1 = str(random.choices(GSFPC)).replace('[','').replace(']','').replace("'",'')
                scorercommentary = str(scorer1 + comment1) 
                print(scorercommentary)
                print() 
                time.sleep(1)
                print(scorer1, minute,"'")
                print() 
                time.sleep(1)
                
        if attackingteam is team2.name:
            
            if minute % 5 == 0:
                
                commentary(team2, team1)
                print()
                time.sleep(1)
               
            team2goal = random.randint(1, team2.attacking)*potentacy
            team1defend = random.randint(1, team1.defending)
            
            if team2goal > team1defend:
            
                team2score.append("team2")
                scorer2 = str(random.choices(team2players, weights=probs)).replace('[','').replace(']','').replace("'",'')
                comment1 = str(random.choices(GSFPC)).replace('[','').replace(']','').replace("'",'')
                scorercommentary = str(scorer2 + comment1)                    
                print(scorercommentary)
                print() 
                time.sleep(1)
                print("                    ", minute,"'", scorer2)
                print() 
                time.sleep(1)
                
        minute += 1
        time.sleep(0.5)
        
        if minute == 35:
            
            print("Half-time: ", team1.name, len(team1score)," - ", len(team2score),team2.name)
            time.sleep(5)
            print()
            print("We are underway here for the second half of this World Cup Final between", team1.name, "and", team2.name)
            time.sleep(2)    
            print() 
    
    if len(team1score) > len(team2score):
        
        print("Unbelievable!", team1.name, "are World Champions!!!")
    
    if len(team2score) > len(team1score):
        
        print("Unbelievable!", team2.name, "are World Champions!!!")
       
    print("Full-time: ", team1.name, len(team1score)," - ", len(team2score),team2.name)
    print()
    time.sleep(1)

    if len(team1score) == len(team2score):
        
        print("It's all square here after full time. We are going to golden goal!")
        
        while len(team1score) == len(team2score):
            
            attackingteam = scoring_chance(team1, team2)
            
            if attackingteam is team1.name:
                
                if minute % 5 == 0:
                
                    commentary(team2, team1)
                    print()
                    time.sleep(1)

                team1goal = random.randint(1, team1.attacking)*potentacy
                team2defend = random.randint(1, team2.defending)
                if team1goal > team2defend:
                    team1score.append("team1")
                    scorer1 = str(random.choices(team1players, weights=probs)).replace('[','').replace(']','').replace("'",'')
                    comment1 = str(random.choices(GSFPC)).replace('[','').replace(']','').replace("'",'')
                    scorercommentary = str(scorer1 + comment1)
                    print(scorercommentary)
                    print() 
                    time.sleep(1)
                    print(scorer1, minute,"'")
                    print() 
                    time.sleep(1)
                    
            if attackingteam is team2.name:

                if minute % 5 == 0:
                
                    commentary(team2, team1)
                    print()
                    time.sleep(1)

                team2goal = random.randint(1, team2.attacking)*potentacy
                team1defend = random.randint(1, team1.defending)
                if team2goal > team1defend:
                    team2score.append("team2")
                    scorer2 = str(random.choices(team2players, weights=probs)).replace('[','').replace(']','').replace("'",'')
                    comment1 = str(random.choices(GSFPC)).replace('[','').replace(']','').replace("'",'')
                    scorercommentary = str(scorer2 + comment1)                      
                    print(scorercommentary)
                    print() 
                    time.sleep(1)
                    print("                    ", minute,"'", scorer2)
                    print()
                    time.sleep(1)
                    
            minute += 1
            time.sleep(0.5)
            
        if len(team1score) > len(team2score):
            
            print(team1.name, "have won the World Cup in extra time unbelievable scenes!!")
            
        if len(team1score) < len(team2score):
            
            print(team2.name, "have won the World Cup in extra time unbelievable scenes!!")

        print("Final Score: ", team1.name, len(team1score)," - ", len(team2score),team2.name)