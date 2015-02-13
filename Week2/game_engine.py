import random

def begin(char):  #User chooses teacher subject
  print '''What kind of teacher do you want to be?
  1 = Math (++energy, -excuses)
  2 = English (++patience, -excuses)
  3 = Theater (+energy, +excuses)'''
  print '-'*75
  print '-'*75
  class_choice = raw_input("Which subject will you chose?: ")
  if class_choice == "1":
    math(char)
  elif class_choice == "2":
    english(char)
  elif class_choice == "3":
    theater(char)
  else:
    print '-'*75
    print "I didn't understand your choice. Try again"
    print '-'*75
    begin(char)

def battle_menu(char):
  print '''BATTLE MENU:
  1 = Run away
  2 = Use patience
  3 = Make up an excuse to leave'''
  print '-'*75  

def battle_success(char):
  print"You have beaten your opponent!"
  char.opponents_beaten += 1
  current_stats(char)

def battle_failure(char, challenge):
  print "Oh nooo!! It didn't work!!"
  current_stats(char)
  battle(char, challenge)

def battle(char, challenge):
  print "How do you plan to bypass this {}?\n".format(challenge.name)
  battle_menu(char)
  battle_choice = raw_input("What will you do?:  "  )
  if battle_choice == "1":    #Player tries to run
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.energy:
      battle_success(char)
      char.energy -= 1
    if challenge.energy <= player_roll:
      char.energy -= 2
      battle_failure(char, challenge)
  if battle_choice == "2":    #Player uses patience
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.patience:
      battle_success(char)
      char.patience -= 1
    if challenge.patience <= player_roll:
      char.patience -= 2
      battle_failure(char, challenge)
  if battle_choice == "3":    #Player tries to make up an excuse
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.excuse_detection:
      battle_success(char)
      char.excuses -= 1
    if challenge.excuse_detection <= player_roll:
      char.excuses -= 1
      battle_failure(char, challenge)

def current_stats(char):  #Called when needing to display current teacher status
  print '''
Here are the current stats for %s:
  Energy: %d 
  Patience: %d
  Excuses: %d

And you have beaten %d opponents''' % (char.name, char.energy, char.patience, char.excuses, char.opponents_beaten)

def hallway_update(char): #Called after each encounter with an opponent
  if char.opponents_beaten < 10:
    print '-'*75
    print "HALLWAY  {}".format(str(char.opponents_beaten  + 1))
    print '-'*75
  else:
    print "YOU'VE ESCAPED! WOOOOHOOOOOOOO!!!"   


#Adding/removing stats for choice of what type of teacher
def math(char):
  char.energy += 4
  char.excuses -= 2
  print "You've chosen to be a math teacher..."

def english(char):
  char.patience += 4
  char.excuses -= 2
  print "You've chosen to be an english teacher..."

def theater(char):
  char.energy += 2
  char.excuses += 2
  print "You've chosen to be a theater teacher..."