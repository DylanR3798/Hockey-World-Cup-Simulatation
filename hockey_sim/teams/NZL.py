from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Manchester = Goalkeeper('Devon Manchester', 74, 78, 71, 70)
Hilton = Outfield_Player('Blair Hilton', 'DF', 56, 78, 71, 70, 73, 72)
Archibald = Outfield_Player('Ryan Archibald', 'MF', 79, 65, 78, 77, 75, 72)
Child = Outfield_Player('Simon Child', 'MF', 67, 72, 75, 73, 68, 76)
Shaw = Outfield_Player('Bradley Shaw', 'FW', 76, 62, 77, 75, 74, 79)

NZL = Team('New Zealand', Manchester, Hilton, Archibald, Child, Shaw)