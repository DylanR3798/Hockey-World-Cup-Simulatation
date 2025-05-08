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