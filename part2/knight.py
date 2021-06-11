from part2.warrior import Warrior
class Knight(Warrior):
  """
  calss knight mdr
  """
  def __init__(self, strength=6, life_point=50):

    super().__init__(strength=strength, life_point=life_point)

  def knight1(self):
    """
    strength /2
    """
    return round(self.strength) // 2

  def heal(self):
    """
    add 2 hp if health <39
    max health 40
    """
    if self._life < 49:
      self._life = self._life + 2
    elif self._life == 49:
      self._life = self._life + 1
