from part2.warrior import Warrior
class Vampire(Warrior):
  """Warrior is first fighter you can create
  """
  def __init__(self, strength=4, life_point=40, vampirism=50):
    """
    :param strenght: damage that will inflict the warrior
    :param life_point: Maximum life point that warrior can hold
    """
    super().__init__(strength=strength, life_point=life_point)
    self.vampirism = vampirism

  def vam(self):
    """
    vampirism attribute as an integer (50 for 50%)
    """
    self._life += self.strength * self.vampirism // 100
    if self._life > 40:
      self._life = 40
    return self._life

  def heal(self):
    """
    add 2 hp if health <39
    max health 40
    """
    if self._life < 39:
      self._life = self._life + 2
    elif self._life == 39:
      self._life = self._life  + 1
