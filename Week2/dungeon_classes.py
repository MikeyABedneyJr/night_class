#This builds your teacher stats to be modified throughout the game
class Player(object):
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

class Opponent(object):
  def __init__(self, name, energy, patience, excuse_detection):
    self.name = name
    self.energy = energy
    self.patience = patience
    self.excuse_detection = excuse_detection
