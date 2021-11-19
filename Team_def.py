from .Outfield_Player import *
from .Goalkeeper import *
from.Team import *

Vivaldi = Goalkeeper('Juan Vivaldi', 83, 77, 72, 82)
Peillat = Outfield_Player('Gonzalo Peillat', 'DF', 70, 89, 78, 73, 79, 67)
Ortiz = Outfield_Player('Ignacio Ortiz', 'MF', 79, 78, 77, 80, 75, 81)
Rey = Outfield_Player('Matias Rey', 'MF', 81, 77, 74, 72, 87, 72)
Vila = Outfield_Player('Lucas Vila', 'FW', 87, 50, 80, 82, 74, 85)

ARG = Team('Argentina', Vivaldi, Peillat, Ortiz, Rey, Vila)

Charter = Goalkeeper('Andrew Charter', 84, 80, 75, 78)
Dawson = Outfield_Player('Mattew Dawson', 'DF', 74, 86, 80, 79, 80, 81)
Wickham = Outfield_Player('Tom Wickham', 'MF', 79, 78, 80, 82, 80, 81)
Edwards = Outfield_Player('Jeremy Edwards', 'MF', 80, 81, 76, 82, 80, 75)
Craig = Outfield_Player('Tom Craig', 'FW', 95, 65, 81, 82, 77, 80)

AUS = Team('Australia', Charter, Dawson, Wickham, Edwards, Craig)

Mantler = Goalkeeper('Michael Mantler', 64, 67, 62, 69)
Podpera = Outfield_Player('Mathias Podpera', 'DF', 63, 74, 67, 64, 65, 68)
Binder = Outfield_Player('Oliver Binder', 'MF', 76, 70, 62, 74, 66, 67)
Schmidt = Outfield_Player('Bernhard Schmidt', 'MF', 68, 77, 71, 67, 66, 76)
Bele = Outfield_Player('Robert Bele', 'FW', 76, 68, 69, 87, 62, 68)

AUT = Team('Austria', Mantler, Podpera, Binder, Schmidt, Bele)

Vanasch = Goalkeeper('Vincent Vanasch', 80, 77, 70, 79)
Briels = Outfield_Player('Thomas Briels', 'DF', 68, 87, 75, 70, 75, 71)
Boccard = Outfield_Player('Gautheir Boccard', 'MF', 75, 77, 79, 78, 76, 80)
Dockier = Outfield_Player('Sebastian Dockier', 'MF', 79, 78, 70, 71, 81, 70)
Charlier = Outfield_Player('Cedric Charlier', 'FW', 82, 68, 74, 79, 71, 82)

BEL = Team('Belgium', Vanasch, Briels, Boccard, Dockier, Charlier)

Pinner = Goalkeeper('George Pinner', 76, 77, 74, 79)
Dixon = Outfield_Player('Adam Dixon', 'DF', 45, 77, 79, 65, 81, 52)
Middleton = Outfield_Player('Barry Middleton', 'MF', 75, 81, 79, 76, 77, 73)
Martin = Outfield_Player('Harry Martin', 'MF', 79, 78, 73, 79, 81, 78)
Jackson = Outfield_Player('Ashley Jackson', 'FW', 85, 65, 74, 77, 73, 78)

ENG = Team('England', Pinner, Dixon, Middleton, Martin, Jackson)

Cortes = Goalkeeper('Francisco Cortes', 79, 74, 79, 69)
Enrique = Outfield_Player('Sergio Enrique', 'DF', 51, 79, 77, 73, 79, 69)
Alegre = Outfield_Player('David Alegre', 'MF', 75, 68, 75, 73, 74, 76)
Carrera = Outfield_Player('Jardi Carrera', 'MF', 71, 73, 76, 74, 79, 78)
Lleonart = Outfield_Player('Xavi Lleonart', 'FW', 78, 50, 70, 78, 77, 85)

ESP = Team('Spain', Cortes, Enrique, Alegre, Carrera, Lleonart)

Jacobi = Goalkeeper('Niclas Jacobi', 80, 73, 78, 77)
Butt = Outfield_Player('Linus Butt', 'DF', 60, 87, 76, 75, 70, 75)
Tompertz = Outfield_Player('Moritz Tompertz', 'MF', 70, 69, 73, 80, 77, 73)
Herzbruch = Outfield_Player('Timm Herzbruch', 'MF', 81, 73, 72, 74, 75, 73)
Grambusch = Outfield_Player('Tom Grambusch', 'FW', 78, 68, 72, 73, 72, 74)

GER = Team('Germany', Jacobi, Butt, Tompertz, Herzbruch, Grambusch)

Carless = Goalkeeper('Ben Carless', 68, 65, 66, 67)
Kyriakides = Outfield_Player('Dan Kyriakides', 'DF', 63, 74, 67, 63, 66, 65)
Cornick = Outfield_Player('Andrew Cornick', 'MF', 67, 66, 68, 63, 69, 65)
Brignull = Outfield_Player('Liam Brignull', 'MF', 62, 69, 65, 69, 67, 65)
Furlong = Outfield_Player('Gareth Furlong', 'FW', 77, 59, 66, 64, 67, 63)

WAL = Team('Wales', Carless, Kyriakides, Cornick, Brignull, Furlong)

Pieterse = Goalkeeper('Erasmus Pieterse', 75, 69, 74, 71)
Malgraff = Outfield_Player('Ignatius Malgraff', 'DF', 74, 64, 70, 75, 65, 69)
Madsen = Outfield_Player('Lloyd Madsen', 'MF', 65, 67, 66, 73, 79, 70)
Paton = Outfield_Player('Wade Paton', 'MF', 66, 73, 68, 65, 66, 68)
Hykes = Outfield_Player('Julian Hykes', 'FW', 79, 65, 72, 68, 79, 66)

RSA = Team('South Africa', Pieterse, Malgraff, Madsen, Paton, Hykes)

Singh = Goalkeeper('Harmanpreet Singh', 79, 72, 77, 74)
Tirkey = Outfield_Player('Dipsan Tirkey', 'DF', 61, 79, 75, 78, 68, 70)
Sharma = Outfield_Player('Nilakanta Sharma', 'MF', 72, 68, 72, 79, 78, 74)
Qureshi = Outfield_Player('Armaan Qureshi', 'MF', 76, 68, 77, 72, 75, 73)
Yousuf = Outfield_Player('Affan Yousuf', 'FW', 80, 70, 70, 74, 76, 73)

IND = Team('India', Singh, Tirkey, Sharma, Qureshi, Yousuf)

Harte = Goalkeeper('David Harte', 71, 77, 73, 68)
Gormley = Outfield_Player('Ronan Gormley', 'DF', 69, 77, 72, 70, 71, 68)
Watt = Outfield_Player('Michael Watt', 'MF', 61, 78, 79, 77, 73, 70)
Cargo = Outfield_Player('Chris Cargo', 'MF', 80, 64, 71, 74, 67, 73)
Bell = Outfield_Player('Jonny Bell', 'FW', 84, 59, 73, 80, 71, 84)

IRL = Team('Ireland', Harte, Gormley, Watt, Cargo, Bell)

Othman = Goalkeeper('Hafizuddin Othman', 74, 72, 68, 70)
Rahim = Outfield_Player('Razie Rahim', 'DF', 70, 71, 71, 72, 69, 73)
Hassan = Outfield_Player('Azi Hassan', 'MF', 77, 73, 76, 71, 74, 72)
Saari = Outfield_Player('Fitri Saari', 'MF', 76, 71, 67, 68, 70, 72)
Saabah = Outfield_Player('Shahril Saabah', 'FW', 71, 73, 75, 70, 76, 73)

MAL = Team('Malaysia', Othman, Rahim, Hassan, Saari, Saabah)

Ali = Goalkeeper('Amjad Ali', 66, 71, 67, 68)
Mahmood = Outfield_Player('Abu Mahmood', 'DF', 63, 73, 70, 78, 67, 63)
Shaked = Outfield_Player('Ammad Shaked', 'MF', 79, 69, 69, 66, 69, 74)
Ashfaq = Outfield_Player('Nawaz Ashfaq', 'MF', 68, 70, 69, 74, 63, 79)
Abbas = Outfield_Player('Tasawar Abbas', 'FW', 79, 63, 68, 77, 69, 77)

PAK = Team('Pakistan', Ali, Mahmood, Shaked, Ashfaq, Abbas)

Manchester = Goalkeeper('Devon Manchester', 74, 78, 71, 70)
Hilton = Outfield_Player('Blair Hilton', 'DF', 56, 78, 71, 70, 73, 72)
Archibald = Outfield_Player('Ryan Archibald', 'MF', 79, 65, 78, 77, 75, 72)
Child = Outfield_Player('Simon Child', 'MF', 67, 72, 75, 73, 68, 76)
Shaw = Outfield_Player('Bradley Shaw', 'FW', 76, 62, 77, 75, 74, 79)

NZL = Team('New Zealand', Manchester, Hilton, Archibald, Child, Shaw)

Stockmann = Goalkeeper('Jaap Stockmann', 79, 75, 78, 78)
Schuurman = Outfield_Player('Glenn Schuurman', 'DF', 63, 85, 77, 74, 68, 67)
Verga = Outfield_Player('Valetin Verga', 'MF', 72, 73, 74, 75, 75, 76)
Hertzberger = Outfield_Player('Jeroen Hertzberger', 'MF', 78, 78, 72, 73, 80, 71)
Pruyser = Outfield_Player('Micro Pruyser', 'FW', 83, 68, 72, 76, 72, 80)

NED = Team('Netherlands', Stockmann, Schuurman, Verga, Hertzberger, Pruyser)

