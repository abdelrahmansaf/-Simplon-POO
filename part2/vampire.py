# from part2.vampire import Vampire
from part2.warrior import Warrior
from part2.army import Army
# from part2.battlefield import Battlefield

class Vampire(Warrior):
  """Warrior is first fighter you can create."""

  def __init__(self, strength=4, life_point=40,vampirism=50):
    """
    :param strenght: damage that will inflict the warrior
    :param life_point: Maximum life point that warrior can hold
    """
    super().__init__(strength=strength, life_point=life_point)
    self.vampirism=vampirism


  def Vam(self):
    self._life +=self.strength *self.vampirism //100
    if self._life>40:
      self._life=40
    return self._life

