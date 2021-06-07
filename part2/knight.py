from part2.warrior import Warrior
# from part2.battlefield import *

class Knight(Warrior):

    def __init__(self, strength=6, life_point=50):

      super().__init__(strength=strength, life_point=life_point)
      # if self._life>50:
      #       self._life=50

    def knight1(self):
      self.strength = self.strength + round(self.strength) // 2
      return self.strength
0
      
            

            
