import random

import time

class Goalkeeper():
    
    """A definition that produces the attributes for a goalkeeper on the basis of the players overall rating"""
    
    def __init__(self, name, reflexes, jumping, bravery, kicking):
        
        self.name = name
        self.reflexes = reflexes
        self.jumping = jumping
        self.bravery = bravery
        self.kicking = kicking
        self.overall = int((reflexes + jumping + bravery + kicking)/4)
        self.maxipgk = 320
        
        if self.reflexes + self.jumping + self.bravery + self.kicking > self.maxipgk:
            raise ValueError("Points maximum exceeded! You points maximum is " + str(self.maxipgk))
        if self.reflexes > 100:
            raise ValueError("Attacking Points maximum exceeded! You Attacking Points maximum is 100")
        if self.jumping > 100:
            raise ValueError("Defending Points maximum exceeded! You Defending Points maximum is 100")
        if self.bravery > 100:
            raise ValueError("Fitness Points maximum exceeded! You Fitness Points maximum is 100")
        if self.kicking > 100:
            raise ValueError("Pace Points maximum exceeded! You Pace Points maximum is 100")
            
    def __repr__(self):
        
        return repr((self.name, self.reflexes, self.jumping, self.bravery, self.kicking))

class Outfield_Player():
    
    """ A class for a player, Attributes: Name (a string), Position (a definition, string), Overall (a string)  """
    
    def __init__(self, name, position, attacking, defending, fitness, pace, passing, skill):
        
        self.name = name
        self.position = position
        self.attacking = attacking
        self.defending = defending
        self.fitness = fitness
        self.pace = pace
        self.passing = passing
        self.skill = skill
        self.overall = int((attacking + defending + fitness + pace + passing + skill)/6)
        self.maxip = 480 
        
        if self.attacking + self.defending + self.fitness + self.pace + self.passing + self.skill > self.maxip:
            
            raise ValueError("Points maximum exceeded! You points maximum is " + str(self.maxip))
        if self.attacking > 100:
            raise ValueError("Attacking Points maximum exceeded! You Attacking Points maximum is 100")
        if self.defending > 100:
            raise ValueError("Defending Points maximum exceeded! You Defending Points maximum is 100")
        if self.fitness > 100:
            raise ValueError("Fitness Points maximum exceeded! You Fitness Points maximum is 100")
        if self.pace > 100:
            raise ValueError("Pace Points maximum exceeded! You Pace Points maximum is 100")
        if self.passing > 100:
            raise ValueError("Passing Points maximum exceeded! You Passing Points maximum is 100")
        if self.skill > 100:
            raise ValueError("Skill Points maximum exceeded! You Skill Points maximum is 100")
        if self.position not in ['DF','MF','FW']:
            raise ValueError("Position not valid. Select from " + "'DF','MF','FW'")
            
    def __repr__(self):
        
        return repr((self.name, self.position, self.attacking, self.defending, self.fitness, self.pace, self.passing, self.skill))

class Team:
    
    """ A class for creating a team with an attacking, defending and overall attribute"""

    def __init__(self, name, player1, player2, player3, player4, player5):

        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.player3 = player3
        self.player4 = player4
        self.player5 = player5

        self.overall = int((player1.overall + player2.overall + player3.overall + player4.overall + player5.overall)/5) 
        self.defending = int((player1.overall + player2.defending + player3.defending + player4.defending + player5.defending)/5)
        self.attacking = int((player2.attacking + player3.attacking + player4.attacking + player5.attacking)/4) 

    def __repr__(self):

        return repr((self.name, self.overall, self.player1, self.player2, self.player3, self.player4, self.player5))

Vivaldi = Goalkeeper('Juan Vivaldi', 83, 77, 72, 82)
Peillat = Outfield_Player('Gonzalo Peillat', 'DF', 70, 89, 78, 73, 79, 67)
Ortiz = Outfield_Player('Ignacio Ortiz', 'MF', 79, 78, 77, 80, 75, 81)
Rey = Outfield_Player('Matias Rey', 'MF', 81, 77, 74, 72, 87, 72)
Vila = Outfield_Player('Lucas Vila', 'FW', 87, 50, 80, 82, 74, 85)

ARG = Team('Argentina', Vivaldi, Peillat, Ortiz, Rey, Vila)

Charter = Goalkeeper('Andrew Charter', 84, 80, 75, 78)
Dawson = Outfield_Player('Mattew Dawson', 'DF', 74, 86, 80, 79, 80, 81)
Wickham = Outfield_Player('Tom Wickham', 'MF', 79, 78, 80, 82, 80, 81)
Edwards = Outfield_Player('Jeremy Edwards', 'MF', 80, 81, 76, 82, 80, 75)
Craig = Outfield_Player('Tom Craig', 'FW', 95, 65, 81, 82, 77, 80)

AUS = Team('Australia', Charter, Dawson, Wickham, Edwards, Craig)

Mantler = Goalkeeper('Michael Mantler', 64, 67, 62, 69)
Podpera = Outfield_Player('Mathias Podpera', 'DF', 63, 74, 67, 64, 65, 68)
Binder = Outfield_Player('Oliver Binder', 'MF', 76, 70, 62, 74, 66, 67)
Schmidt = Outfield_Player('Bernhard Schmidt', 'MF', 68, 77, 71, 67, 66, 76)
Bele = Outfield_Player('Robert Bele', 'FW', 76, 68, 69, 87, 62, 68)

AUT = Team('Austria', Mantler, Podpera, Binder, Schmidt, Bele)

Vanasch = Goalkeeper('Vincent Vanasch', 80, 77, 70, 79)
Briels = Outfield_Player('Thomas Briels', 'DF', 68, 87, 75, 70, 75, 71)
Boccard = Outfield_Player('Gautheir Boccard', 'MF', 75, 77, 79, 78, 76, 80)
Dockier = Outfield_Player('Sebastian Dockier', 'MF', 79, 78, 70, 71, 81, 70)
Charlier = Outfield_Player('Cedric Charlier', 'FW', 82, 68, 74, 79, 71, 82)

BEL = Team('Belgium', Vanasch, Briels, Boccard, Dockier, Charlier)

Pinner = Goalkeeper('George Pinner', 76, 77, 74, 79)
Dixon = Outfield_Player('Adam Dixon', 'DF', 45, 77, 79, 65, 81, 52)
Middleton = Outfield_Player('Barry Middleton', 'MF', 75, 81, 79, 76, 77, 73)
Martin = Outfield_Player('Harry Martin', 'MF', 79, 78, 73, 79, 81, 78)
Jackson = Outfield_Player('Ashley Jackson', 'FW', 85, 65, 74, 77, 73, 78)

ENG = Team('England', Pinner, Dixon, Middleton, Martin, Jackson)

Cortes = Goalkeeper('Francisco Cortes', 79, 74, 79, 69)
Enrique = Outfield_Player('Sergio Enrique', 'DF', 51, 79, 77, 73, 79, 69)
Alegre = Outfield_Player('David Alegre', 'MF', 75, 68, 75, 73, 74, 76)
Carrera = Outfield_Player('Jardi Carrera', 'MF', 71, 73, 76, 74, 79, 78)
Lleonart = Outfield_Player('Xavi Lleonart', 'FW', 78, 50, 70, 78, 77, 85)

ESP = Team('Spain', Cortes, Enrique, Alegre, Carrera, Lleonart)

Jacobi = Goalkeeper('Niclas Jacobi', 80, 73, 78, 77)
Butt = Outfield_Player('Linus Butt', 'DF', 60, 87, 76, 75, 70, 75)
Tompertz = Outfield_Player('Moritz Tompertz', 'MF', 70, 69, 73, 80, 77, 73)
Herzbruch = Outfield_Player('Timm Herzbruch', 'MF', 81, 73, 72, 74, 75, 73)
Grambusch = Outfield_Player('Tom Grambusch', 'FW', 78, 68, 72, 73, 72, 74)

GER = Team('Germany', Jacobi, Butt, Tompertz, Herzbruch, Grambusch)

Carless = Goalkeeper('Ben Carless', 68, 65, 66, 67)
Kyriakides = Outfield_Player('Dan Kyriakides', 'DF', 63, 74, 67, 63, 66, 65)
Cornick = Outfield_Player('Andrew Cornick', 'MF', 67, 66, 68, 63, 69, 65)
Brignull = Outfield_Player('Liam Brignull', 'MF', 62, 69, 65, 69, 67, 65)
Furlong = Outfield_Player('Gareth Furlong', 'FW', 77, 59, 66, 64, 67, 63)

WAL = Team('Wales', Carless, Kyriakides, Cornick, Brignull, Furlong)

Pieterse = Goalkeeper('Erasmus Pieterse', 75, 69, 74, 71)
Malgraff = Outfield_Player('Ignatius Malgraff', 'DF', 74, 64, 70, 75, 65, 69)
Madsen = Outfield_Player('Lloyd Madsen', 'MF', 65, 67, 66, 73, 79, 70)
Paton = Outfield_Player('Wade Paton', 'MF', 66, 73, 68, 65, 66, 68)
Hykes = Outfield_Player('Julian Hykes', 'FW', 79, 65, 72, 68, 79, 66)

RSA = Team('South Africa', Pieterse, Malgraff, Madsen, Paton, Hykes)

Singh = Goalkeeper('Harmanpreet Singh', 79, 72, 77, 74)
Tirkey = Outfield_Player('Dipsan Tirkey', 'DF', 61, 79, 75, 78, 68, 70)
Sharma = Outfield_Player('Nilakanta Sharma', 'MF', 72, 68, 72, 79, 78, 74)
Qureshi = Outfield_Player('Armaan Qureshi', 'MF', 76, 68, 77, 72, 75, 73)
Yousuf = Outfield_Player('Affan Yousuf', 'FW', 80, 70, 70, 74, 76, 73)

IND = Team('India', Singh, Tirkey, Sharma, Qureshi, Yousuf)

Harte = Goalkeeper('David Harte', 71, 77, 73, 68)
Gormley = Outfield_Player('Ronan Gormley', 'DF', 69, 77, 72, 70, 71, 68)
Watt = Outfield_Player('Michael Watt', 'MF', 61, 78, 79, 77, 73, 70)
Cargo = Outfield_Player('Chris Cargo', 'MF', 80, 64, 71, 74, 67, 73)
Bell = Outfield_Player('Jonny Bell', 'FW', 84, 59, 73, 80, 71, 84)

IRL = Team('Ireland', Harte, Gormley, Watt, Cargo, Bell)

Othman = Goalkeeper('Hafizuddin Othman', 74, 72, 68, 70)
Rahim = Outfield_Player('Razie Rahim', 'DF', 70, 71, 71, 72, 69, 73)
Hassan = Outfield_Player('Azi Hassan', 'MF', 77, 73, 76, 71, 74, 72)
Saari = Outfield_Player('Fitri Saari', 'MF', 76, 71, 67, 68, 70, 72)
Saabah = Outfield_Player('Shahril Saabah', 'FW', 71, 73, 75, 70, 76, 73)

MAL = Team('Malaysia', Othman, Rahim, Hassan, Saari, Saabah)

Ali = Goalkeeper('Amjad Ali', 66, 71, 67, 68)
Mahmood = Outfield_Player('Abu Mahmood', 'DF', 63, 73, 70, 78, 67, 63)
Shaked = Outfield_Player('Ammad Shaked', 'MF', 79, 69, 69, 66, 69, 74)
Ashfaq = Outfield_Player('Nawaz Ashfaq', 'MF', 68, 70, 69, 74, 63, 79)
Abbas = Outfield_Player('Tasawar Abbas', 'FW', 79, 63, 68, 77, 69, 77)

PAK = Team('Pakistan', Ali, Mahmood, Shaked, Ashfaq, Abbas)

Manchester = Goalkeeper('Devon Manchester', 74, 78, 71, 70)
Hilton = Outfield_Player('Blair Hilton', 'DF', 56, 78, 71, 70, 73, 72)
Archibald = Outfield_Player('Ryan Archibald', 'MF', 79, 65, 78, 77, 75, 72)
Child = Outfield_Player('Simon Child', 'MF', 67, 72, 75, 73, 68, 76)
Shaw = Outfield_Player('Bradley Shaw', 'FW', 76, 62, 77, 75, 74, 79)

NZL = Team('New Zealand', Manchester, Hilton, Archibald, Child, Shaw)

Stockmann = Goalkeeper('Jaap Stockmann', 79, 75, 78, 78)
Schuurman = Outfield_Player('Glenn Schuurman', 'DF', 63, 85, 77, 74, 68, 67)
Verga = Outfield_Player('Valetin Verga', 'MF', 72, 73, 74, 75, 75, 76)
Hertzberger = Outfield_Player('Jeroen Hertzberger', 'MF', 78, 78, 72, 73, 80, 71)
Pruyser = Outfield_Player('Micro Pruyser', 'FW', 83, 68, 72, 76, 72, 80)

NED = Team('Netherlands', Stockmann, Schuurman, Verga, Hertzberger, Pruyser)

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
        
def create_quarterfinalists():
    return []

quarterfinalists=create_quarterfinalists()

def round_of_16_draw(team):
    
    if len(quarterfinalists) < 1:
        
        roundof16teams=[WAL,AUT,RSA,PAK,MAL,IRL,NZL,ESP,ENG,IND,GER,NED,BEL,ARG,AUS]
        roosmatchday=[]
        
        opponent = random.choice(roundof16teams)
        roundof16teams.pop(roundof16teams.index(opponent))
        otherteams= sorted(roundof16teams, key=lambda team: team.name)
        i = 0
        
        print(team.name, " v ", opponent.name)
        time.sleep(1)
        
        while i<6:
            
            otherteams.reverse()
            hometeam = otherteams.pop(int((len(otherteams)-1)/2))
            awayteam = otherteams.pop(int((len(otherteams)+1)/2))
            roosmatchday.append((hometeam, awayteam))
            print(hometeam.name, " v ", awayteam.name)
            time.sleep(1)
            i += 1
            
        lasthometeam = otherteams.pop()
        lastawayteam = otherteams.pop()
        roosmatchday.append((lasthometeam, lastawayteam))
        print(lasthometeam.name, " v ", lastawayteam.name)  
        
        teamt1,teamt2 = zip(*roosmatchday)
        team1 = list(teamt1)
        team2 = list(teamt2)
        q = 0

        print()
        print("Results:")

        while q < 7:
        
            time.sleep(1)
            print()
            roogames = CPU_match(team1.pop(), team2.pop())
            quarterfinalists.append(roogames)
            q += 1
            
    else:

        quarterfinalists.clear()
        raise ValueError('You already have the Quarter-finalists')

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


def create_finalists():
    return []

finalists =create_finalists()

def semi_finals_draw(team):

    if len(finalists) < 1:

        semifinalteams=list(semifinalists)
        fmatchday=[]
        opponent = random.choice(semifinalteams)
        semifinalteams.pop(semifinalteams.index(opponent))
        otherteams3 = sorted(semifinalteams, key=lambda team: team.name)
        i = 0

        time.sleep(1)
        print(team.name, " v ", opponent.name)

        lasthometeam = otherteams3.pop()
        lastawayteam = otherteams3.pop()
        fmatchday.append((lasthometeam, lastawayteam))
        time.sleep(1)
        print(lasthometeam.name, " v ", lastawayteam.name)  

        teamt1,teamt2 = zip(*fmatchday)
        team1 = list(teamt1)
        team2 = list(teamt2)

        print()
        print("Results:")
        print()
        semifinalgames = CPU_match(team1.pop(),team2.pop())
        finalists.append(semifinalgames)

    else:
    
        finalists.clear()
        raise ValueError('You already have the results for your finalists')

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
    
    print("Kick-Off")
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