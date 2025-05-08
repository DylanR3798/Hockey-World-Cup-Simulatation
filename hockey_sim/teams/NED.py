from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Stockmann = Goalkeeper('Jaap Stockmann', 79, 75, 78, 78)
Schuurman = Outfield_Player('Glenn Schuurman', 'DF', 63, 85, 77, 74, 68, 67)
Verga = Outfield_Player('Valetin Verga', 'MF', 72, 73, 74, 75, 75, 76)
Hertzberger = Outfield_Player('Jeroen Hertzberger', 'MF', 78, 78, 72, 73, 80, 71)
Pruyser = Outfield_Player('Micro Pruyser', 'FW', 83, 68, 72, 76, 72, 80)

NED = Team('Netherlands', Stockmann, Schuurman, Verga, Hertzberger, Pruyser)