from .Team_def import *

import time

import random

def commentary(team, otherteam):
    
    teamplayers = [team.player2.name, team.player3.name, team.player4.name, team.player5.name]
    otherteamplayers = [otherteam.player2.name, otherteam.player3.name, otherteam.player4.name, otherteam.player5.name]
    probs = [0.1,0.225,0.225,0.45]
    probs2 = [0.1,0.2,0.2,0.2,0.2,0.1,0.1,0.1]

    
    GSFPC = [' with just the keeper to beat!',' hits it from the top of the D.',' there to tap it in at the back post.']
    PFCC = [' in possesion at the moment passing it round the back.', ' win a long corner.', ' under pressure now.']
    PFPC = [' plays a long ball forward', ' cuts in from the right.', ' cuts in from the left.']
    PEPPC = [' goes round ', ' intercepts the ball due to a poor pass by ']
    APFPC = [' centres it from the baseline.',' slaps it to the back post.',' wins a penalty corner.']

    teamplayer = str(random.choices(teamplayers, weights=probs, k=1)).replace('[','').replace(']','').replace("'",'')
    otherteamplayer = str(random.choices(otherteamplayers, weights=probs, k=1)).replace('[','').replace(']','').replace("'",'')
    goalscoring1 = str(random.choices(GSFPC)).replace('[','').replace(']','').replace("'",'')
    possession2 = str(random.choices(PFCC)).replace('[','').replace(']','').replace("'",'')
    possession1 = str(random.choices(PFPC)).replace('[','').replace(']','').replace("'",'')
    possession6 = str(random.choices(APFPC)).replace('[','').replace(']','').replace("'",'')
    possession5 = str(random.choices(PEPPC)).replace('[','').replace(']','').replace("'",'')
    
    scoringchancecom1 = teamplayer + goalscoring1
    possessioncom3 = 'Lovely bit of skill from ' + teamplayer + ' to get out of a sticky situation.'            
    possessioncom2 = team.name + possession2
    possessioncom1 = teamplayer + possession1
    possessioncom4 = 'Great pass from ' + teamplayer
    possessioncom5 = teamplayer + possession5 + otherteamplayer
    possessioncom6 = teamplayer + possession6
    scoringchancecom2 = teamplayer + ' gives away a foul in the D! Penalty corner to ' + otherteam.name
    
    possessioncomlist = [possessioncom1, possessioncom2, possessioncom3, possessioncom4, possessioncom5, possessioncom6, scoringchancecom1, scoringchancecom2]
    
    print(" ".join(random.choices(possessioncomlist, weights=probs2, k=1)))

def scoring_chance(team1, team2):
    
    team1chance = random.randint(1, team1.overall)
    team2chance = random.randint(1, team2.overall)
    
    if team1chance > team2chance:
        return team1.name
    if team1chance < team2chance:
        return team2.name

def Match(team1, team2):
    
    """Simulates a match in real-time with teams inputted, if there is a draw at the end of the game the result will be decided by a next goal wins format"""
    minute = 1
    
    team1players = [team1.player2.name, team1.player3.name, team1.player4.name, team1.player5.name]
    team2players = [team2.player2.name, team2.player3.name, team2.player4.name, team2.player5.name]
    probs = [0.1,0.225,0.225,0.45]
    team1score = []
    team2score = []
    GSFPC = [" with just the keeper to beat!"," hits it from the top of the D."," there to tap it in at the back post."]

    
    potentacy = ((team1.attacking+team2.attacking)*(team1.defending+team2.defending))/(10*(team1.overall+team2.overall)**2)
    
    print("Push-Back")
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
            print("We are underway here for the second half of", team1.name, " v ", team2.name)
            time.sleep(2)    
            print() 
            
    print("Full-time: ", team1.name, len(team1score)," - ", len(team2score),team2.name)
    print()
    time.sleep(2)
    
    if len(team1score) == len(team2score):
        
        print("It's all square here after full time. We are going to golden goal!")
        print()

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
            
            print(team1.name, "have won it in extra time unbelievable scenes!")
            print()

        if len(team1score) < len(team2score):
            
            print(team2.name, "have won it in extra time unbelievable scenes!")
            print()

        print("Final Score: ", team1.name, len(team1score)," - ", len(team2score),team2.name)