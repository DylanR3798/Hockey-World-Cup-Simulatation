from hockey_sim.players.goalkeeper import Goalkeeper
from hockey_sim.players.outfield_player import Outfield_Player
from hockey_sim.teams.team import Team

Othman = Goalkeeper('Hafizuddin Othman', 74, 72, 68, 70)
Rahim = Outfield_Player('Razie Rahim', 'DF', 70, 71, 71, 72, 69, 73)
Hassan = Outfield_Player('Azi Hassan', 'MF', 77, 73, 76, 71, 74, 72)
Saari = Outfield_Player('Fitri Saari', 'MF', 76, 71, 67, 68, 70, 72)
Saabah = Outfield_Player('Shahril Saabah', 'FW', 71, 73, 75, 70, 76, 73)

MAL = Team('Malaysia', Othman, Rahim, Hassan, Saari, Saabah)