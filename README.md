# Hockey-World-Cup-Simulation
A python-based Hockey simulation with live in-game commentary of events.

# Intoduction

*HOCKEY WORLD CUP: THE GAME*

In this game you will get to create a team and play against real life national hockey teams in a knockout cup format. To start you are going to need to create players which can be done by using our Outfield_Player and Goalkeeper functions. Once the players are created you are going to need to select 1 Goalkeeper and 4 Outfield Players to form your team, using the Team function. After that, all that's left to do is enter your team into the draw to see who your opponent is, there are 4 rounds (Round of 16, Quarter Finals, Semi Finals and the Final).

Let's get you started!

## Creating a Player

To create a player you are gonna need to assign a nickname for them to be called by.

>> Smith = 

Outfield players require a full name (string) and a position (string) of "DF", "MF" or "FW". They also have 6 attributes to be filled Attacking, Defending, Fitness, Pace, Passing, Skill. Each attribute's points can be up to 100 however the overall points cannot exceed 480. This what a completed Outfield Player should look like:

>> Smith = Outfield_Player("John Smith", "DF", 42, 85, 78, 83, 76, 56)

Goalkeepers only require a full name (string) and only have 4 attributes Reflexes, Jumping, Bravery, Kicking. Each attribute's points can again be up to 100 however the overall points cannot exceed 320. This is what a completed Goalkeeper should look like:

>> Doe = Goalkeeper("John Doe", 65, 79, 81, 75)

## Creating a Team

The team will need to be assigned an abbreviation so it can be called.

>> CHC =  

You need 5 players to create a team - 1 Goalkeeper, 4 Outfield Players. There are no limits on formation but it is recommended that a balance between defence and attack gives the best results. The Team function requires a full name (string) and your players must be entered in the formation you want them in from back to front. This what a completed Team looks like:

>> Doe = Goalkeeper("John Doe", 65, 79, 81, 75)
>> Smith = Outfield_Player("John Smith", "DF", 42, 85, 78, 83, 76, 56)
>> Green = Outfield_Player("Bob Green", "MF", 75, 73, 80, 79, 84, 53)
>> Red = Outfield_Player("James Red", "FW", 82, 56, 81, 80, 82, 75)
>> Blue = Outfield_Player("Mike Blue", "FW", 87, 39, 80, 83, 67, 84)

>> CHC = Team('Cardiff Hockey Club', Doe, Smith, Green, Red, Blue')

## The Cup


>> round_of_16_draw(CHC)

>> Match(CHC, SHC)

>> quarter_finals_draw(CHC)
>> semi_finals_draw(CHC)

>>World_Cup_Final(CHC)
