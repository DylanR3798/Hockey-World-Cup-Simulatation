from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Cortes = Goalkeeper('Francisco Cortes', 79, 74, 79, 69)
Enrique = Outfield_Player('Sergio Enrique', 'DF', 51, 79, 77, 73, 79, 69)
Alegre = Outfield_Player('David Alegre', 'MF', 75, 68, 75, 73, 74, 76)
Carrera = Outfield_Player('Jardi Carrera', 'MF', 71, 73, 76, 74, 79, 78)
Lleonart = Outfield_Player('Xavi Lleonart', 'FW', 78, 50, 70, 78, 77, 85)

ESP = Team('Spain', Cortes, Enrique, Alegre, Carrera, Lleonart)