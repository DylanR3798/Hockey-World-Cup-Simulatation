from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Pinner = Goalkeeper('George Pinner', 76, 77, 74, 79)
Dixon = Outfield_Player('Adam Dixon', 'DF', 45, 77, 79, 65, 81, 52)
Middleton = Outfield_Player('Barry Middleton', 'MF', 75, 81, 79, 76, 77, 73)
Martin = Outfield_Player('Harry Martin', 'MF', 79, 78, 73, 79, 81, 78)
Jackson = Outfield_Player('Ashley Jackson', 'FW', 85, 65, 74, 77, 73, 78)

ENG = Team('England', Pinner, Dixon, Middleton, Martin, Jackson)