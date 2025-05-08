from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Furness = Goalkeeper('Ben Furness', 68, 65, 66, 67)
McTavish = Outfield_Player('Dan McTavish', 'DF', 63, 74, 67, 63, 66, 65)
Gilmour = Outfield_Player('Andrew Gilmour', 'MF', 67, 66, 68, 63, 69, 65)
Adam = Outfield_Player('Liam Adam', 'MF', 62, 69, 65, 69, 67, 65)
McTominay = Outfield_Player('Gareth McTominay', 'FW', 77, 59, 66, 64, 67, 63)

SCO = Team('Scotland', Furness, McTavish, Gilmour, Adam, McTominay)