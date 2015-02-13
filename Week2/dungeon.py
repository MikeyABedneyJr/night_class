import random

import game_engine as ge
import dungeon_classes as dc

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
char = dc.Player(char_name, 7, 7, 7, 0)
char.description()

#Generate 4 types of opponents.  Stats are ordered as: energy, patience, excuse_detection
studentOpp = dc.Opponent("student", 40, 90, 80)
parentOpp = dc.Opponent("parent", 20, 80, 60)
coworkerOpp = dc.Opponent("coworker", 90, 50, 50)
adminOpp = dc.Opponent("administrator", 30, 30, 20)

#Run function to choose teacher subject to modify attribute values
ge.begin(char)

#Show user updated stats after subject selection
ge.current_stats(char)
print '-'*75
print '-'*75
print '''The bell has run, classes have been dismissed, and
you are ready for this week to be over. You eagerly
open the door and take your first steps toward the exit...'''

while char.opponents_beaten < 10:
	ge.hallway_update(char)
	chance_encounter = random.randint(1,100)
	if 1 <= chance_encounter <= 50:
		print 'Teacher {}! I have a quick question for you...'.format(char_name)
		ge.battle(char, studentOpp)
	if 51 <= chance_encounter <=70:
		print 'Excuse me, teacher {}? I need to talk to you about my child...'.format(char_name)
		ge.battle(char, parentOpp)
	if 71 <= chance_encounter <=90:
		print 'Hey {}. Do you have a second?...'.format(char_name)
		ge.battle(char, coworkerOpp)
	if 91 <= chance_encounter <=100:
		print "I've been looking for you {}. I need you to...".format(char_name)
		ge.battle(char, adminOpp)