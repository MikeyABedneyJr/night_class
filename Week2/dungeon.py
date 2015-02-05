import random

#This builds your teacher stats to be modified throughout the game
class Player():
	def __init__(self, name, energy, patience, excuses, opponents_beaten):
		self.name = name
		self.energy = energy
		self.patience = patience
		self.excuses = excuses
		self.opponents_beaten = opponents_beaten

	def description(self):
		print '''
You are Teacher %s and here are your stats:
	Energy: %d 
	Patience: %d
	Excuses: %d''' % (self.name, self.energy, self.patience, self.excuses)
		print '-'*75
		print '-'*75

class Opponent():
	def __init__(self, name, energy, patience, excuse_detection):
		self.name = name
		self.energy = energy
		self.patience = patience
		self.excuse_detection = excuse_detection

def begin():	#User chooses teacher subject
	print '''What kind of teacher do you want to be?
	1 = Math (++energy, -excuses)
	2 = English (++patience, -excuses)
	3 = Theater (+energy, +excuses)'''
	print '-'*75
	print '-'*75
	class_choice = raw_input("Which subject will you chose?: ")
	if class_choice == "1":
		math()
	elif class_choice == "2":
		english()
	elif class_choice == "3":
		theater()
	else:
		print '-'*75
		print "I didn't understand your choice. Try again"
		print '-'*75
		begin()

def battle_menu():
	print '''BATTLE MENU:
	1 = Run away
	2 = Use patience
	3 = Make up an excuse to leave'''
	print '-'*75	

def battle_success():
	print"You have beaten your opponent!"
	char.opponents_beaten += 1
	current_stats()

def battle_failure():
	print "Well, that didn't work. What now?"
	battle()

def battle(char, challenge):
	print "How do you plan to bypass this {}?\n".format(challenge)
	battle_menu()
	battle_choice = raw_input("What will you do?")
	if battle_choice == "1":
		player_roll = random.randint(0,100)
		print player_roll
		if player_roll <= challenge.energy:
			battle_success()
		if challenge.energy <= player_roll:
			char.energy -= 2
			battle_failure()





def current_stats():	#Called when needing to display current teacher status
	print '''
Here are the current stats for %s:
	Energy: %d 
	Patience: %d
	Excuses: %d

And you have beaten %d opponents''' % (char.name, char.energy, char.patience, char.excuses, char.opponents_beaten)

def hallway_update():	#Called after each encounter with an opponent
	if char.opponents_beaten < 10:
		print '-'*75
		print "HALLWAY  {}".format(str(char.opponents_beaten  + 1))
		print '-'*75
	else:
		print "YOU'VE ESCAPED! WOOOOHOOOOOOOO!!!"		


#Adding/removing stats for choice of what type of teacher
def math():
	char.energy += 4
	char.excuses -= 2
	print "You've chosen to be a math teacher..."

def english():
	char.patience += 4
	char.excuses -= 2
	print "You've chosen to be an english teacher..."

def theater():
	char.energy += 2
	char.excuses += 2
	print "You've chosen to be a theater teacher..."

#Beginning storyline
print '-'*75
print '''
You are a teacher at the end of a looong week.
Your goal is to escape the building with ANY amount 
of energy, patience & excuses. You must reach the
exit before running out of any of these attributes
or else the doors will lock and you will have to 
sleep under your desk...which is what they think you 
do anyway...
'''
print '-'*75

#User choses name that gets sent to Player() to create attributes
char_name = raw_input("What is your teacher/player's name?: ")
char = Player(char_name, 7, 7, 7, 0)
char.description()

#Generate 4 types of opponents
studentOpp = Opponent("student", 40, 90, 80)
parentOpp = Opponent("parent", 20, 80, 60)
coworkerOpp = Opponent("coworker", 90, 50, 50)
adminOpp = Opponent("administrator", 30, 30, 20)

#Run function to choose teacher subject to modify attribute values
begin()

#Show user updated stats after subject selection
current_stats()
print '-'*75
print '-'*75
print '''The bell has run, classes have been dismissed, and
you are ready for this week to be over. You eagerly
open the door and take your first steps toward the exit...'''

hallway_update()

print char
print studentOpp
print coworkerOpp

# chance_encounter = random.randint(1,100)
# if 1 <= chance_encounter <= 100:
# 	print 'Teacher {}! I have a quick question for you!'.format(char_name)
# 	battle(char, studentOpp)