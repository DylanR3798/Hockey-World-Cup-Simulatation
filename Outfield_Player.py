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