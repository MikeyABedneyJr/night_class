#This builds your teacher stats to be modified throughout the game
class Player():
	def __init__(self, name, energy, patience, excuses):
		self.name = name
		self.energy = energy
		self.patience = patience
		self.excuses = excuses


	def description(self):
		print '''
You are Teacher %s and here are your stats:
	Energy: %d 
	Patience: %d
	Excuses: %d''' % (self.name, self.energy, self.patience, self.excuses)
		print '-'*75
		print '-'*75


def current_stats():	#Called when needing to display current teacher status
	print '''
Here are the stats for %s:
	Energy: %d 
	Patience: %d
	Excuses: %d''' % (char.name, char.energy, char.patience, char.excuses)

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
char = Player(char_name, 7, 7, 7)
char.description()

def begin():	#User chooses teacher subject
	print 
	'''What kind of teacher do you want to be?
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
		

#Run function to choose teacher subject to modify attribute values
begin()

current_stats()
