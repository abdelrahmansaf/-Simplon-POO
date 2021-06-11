from part2.warrior import Warrior

class Healer(Warrior):
      
  def __init__(self, strength=0, life_point=60):
    super().__init__(strength=strength, life_point=life_point)

  def heal(self):
    """
    add 2 hp if health <39
    max health 40
    """
    if self._life < 49:
      self._life = self._life + 2
    elif self._life == 49:
      self._life = self._life + 1
