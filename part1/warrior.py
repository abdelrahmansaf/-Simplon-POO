
class Warrior:
  """Warrior is first fighter you can create."""

  def __init__(self, strength=5, life_point=50):
    """
    :param strenght: damage that will inflict the warrior
    :param life_point: Maximum life point that warrior can hold
    """
    self.strength = strength
    self._alive = life_point > 0
    self._life = life_point

  @property
  def health(self):
    """
    Health property. update _alive state.
    """
    if self._life <= 0:
      self._life = 0

    return self._life

  def presentation(self):
    """
    String representing the Warrior
    """
    msg = "{} {} life point and {} strength."
    return msg.format("Warrior", self.health, self.strength)

  def damaged(self, dmg):
    """
    methods called when warrior receive damaged. Update _alive and _life..

    :param dmg: damage received.
    """
    if dmg > self._life:
      self._life = 0
    elif dmg < 0:
      dmg = dmg
    else:
      self._life = self._life - dmg

  def isalive(self):
    """:return bool: is Warrior Alive"""
    if self._life <= 0:
      self._alive = False
    return self._alive
