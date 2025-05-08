from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Singh = Goalkeeper('Harmanpreet Singh', 79, 72, 77, 74)
Tirkey = Outfield_Player('Dipsan Tirkey', 'DF', 61, 79, 75, 78, 68, 70)
Sharma = Outfield_Player('Nilakanta Sharma', 'MF', 72, 68, 72, 79, 78, 74)
Qureshi = Outfield_Player('Armaan Qureshi', 'MF', 76, 68, 77, 72, 75, 73)
Yousuf = Outfield_Player('Affan Yousuf', 'FW', 80, 70, 70, 74, 76, 73)

IND = Team('India', Singh, Tirkey, Sharma, Qureshi, Yousuf)