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