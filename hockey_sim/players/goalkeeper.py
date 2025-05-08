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