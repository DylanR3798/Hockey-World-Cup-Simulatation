from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Jacobi = Goalkeeper('Niclas Jacobi', 80, 73, 78, 77)
Butt = Outfield_Player('Linus Butt', 'DF', 60, 87, 76, 75, 70, 75)
Tompertz = Outfield_Player('Moritz Tompertz', 'MF', 70, 69, 73, 80, 77, 73)
Herzbruch = Outfield_Player('Timm Herzbruch', 'MF', 81, 73, 72, 74, 75, 73)
Grambusch = Outfield_Player('Tom Grambusch', 'FW', 78, 68, 72, 73, 72, 74)

GER = Team('Germany', Jacobi, Butt, Tompertz, Herzbruch, Grambusch)