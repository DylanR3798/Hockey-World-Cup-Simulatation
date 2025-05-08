from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Vivaldi = Goalkeeper('Juan Vivaldi', 83, 77, 72, 82)
Peillat = Outfield_Player('Gonzalo Peillat', 'DF', 70, 89, 78, 73, 79, 67)
Ortiz = Outfield_Player('Ignacio Ortiz', 'MF', 79, 78, 77, 80, 75, 81)
Rey = Outfield_Player('Matias Rey', 'MF', 81, 77, 74, 72, 87, 72)
Vila = Outfield_Player('Lucas Vila', 'FW', 87, 50, 80, 82, 74, 85)

ARG = Team('Argentina', Vivaldi, Peillat, Ortiz, Rey, Vila)