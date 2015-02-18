import random

def battle_menu(hero):
  print '''BATTLE MENU:
  1 = Run away
  2 = Use patience
  3 = Make up an excuse to leave'''
  print '-'*75  

#The entire battle sequence is in this block. It throws to other functions for specific conditions.
def battle(hero, challenge):
  print "How do you plan to bypass this {}?\n".format(challenge.name)
  battle_menu(hero)
  battle_choice = raw_input("What will you do?:  "  )
  
  # Player tries to run
  if battle_choice == "1":    
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.energy:   
      battle_success(hero)
      hero.energy -= 1
    if challenge.energy <= player_roll:
      hero.energy -= 2
      battle_failure(hero, challenge)
  
  # Player uses patience
  if battle_choice == "2":    
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.patience:
      battle_success(hero)
      hero.patience -= 1
    if challenge.patience <= player_roll:
      hero.patience -= 2
      battle_failure(hero, challenge)

  # Player tries to make up an excuse
  if battle_choice == "3":    
    player_roll = random.randint(0,100)
    print player_roll
    if player_roll <= challenge.excuse_detection:
      battle_success(hero)
      hero.excuses -= 1
    if challenge.excuse_detection <= player_roll:
      hero.excuses -= 1
      battle_failure(hero, challenge)

  # This is a failsafe in case my loop never ends   <---------------delete when working
  if battle_choice == "exit":
    return False
  # Player doesn't type a 1, 2, or 3
  else:
    print "Please enter a number 1, 2, or 3"
    battle(hero, challenge)

# User wins the fight
def battle_failure(hero, challenge):
  print "Oh nooo!! It didn't work!!"
  current_stats(hero)
  if continue_game = False:
    defeat()
  else:
    battle(hero, challenge)

# User loses the fight
def battle_success(hero):
  print"YOU HAVE BEATEN YOUR OPPONENT!!!!"
  hero.opponents_beaten += 1
  current_stats(hero)
  if continue_game = False:
    player_wins()

# Called when needing to display current teacher status
def current_stats(hero):  
  print '''
Here are the current stats for %s:
  Energy: %d 
  Patience: %d
  Excuses: %d

And you have beaten %d opponents''' % (hero.name, hero.energy, hero.patience, hero.excuses, hero.opponents_beaten)

# Player loses entire game
def defeat(hero):
  print '''
  You have tried your best but cannot go further without rest.
  After going into the fetal position for a few moments, you 
  accidently fall asleep and wake up several hours later. There
  is no use trying to get out, the doors have been locked long
  ago. Picking yourself up slowly, you head back to your 
  classroom to sleep under your desk.

  GAME OVER'''
  print '-'*75
  print '-'*75
  print '-'*75

# Called after each encounter with an opponent
def hallway_update(hero): 
  if continue_game = False:
    print '-'*75
    print "HALLWAY  {}".format(str(hero.opponents_beaten  + 1))
    print '-'*75

def player_wins():
    print '-'*75
    print '''
    YOU'VE ESCAPED! 
    Go out and live your life!
    The game starts over in a few short days....

    GAME OVER'''
    print '-'*75
    print '-'*75
    print '-'*75


