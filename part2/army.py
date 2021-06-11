from part2.healer import Healer
from part2.warlord import Warlord
from part2.knight import Knight
class Army():
  """
  Army hold all fighter ready to battle.
  """
  def __init__(self):
    """Create an Empty Army"""
    self._army = []
    self._warlord = False
    self._knight = False

  def __getitem__(self, item):
    """
    :param item: index
    :return : the Instance of a fighter.
    :raise : IndexError
    """
    return self._army[item]

  def __len__(self):
    """
    Builtin len
    """
    return len(self._army)

  def addUnits(self, cls, number=1):
    """
    Add to the army

    :param cls: Class to be instancied
    :param number: Number of instance to create
    """
    counter = 0
    if cls == Warlord and number > 1:
      number = 1
    for i in self._army:
      if isinstance(i, Warlord):
        number = 0
    while number > counter:
      self._army.append(cls())
      counter = counter + 1

  def pop(self):
    """return the first soldier of the army"""
    return self._army.pop(0)

  def inWarlord(self):
    """
    return True if Warlord in Army
    """
    for i in self._army:
      if isinstance(i, Warlord):
        self._warlord = True
    return self._warlord

  def moveUnits(self):
    """removing all the Healers and the Knights from army
    insert knight on the first of army if exist
    insert the Healers right behind the Knight
    if there was no Knight and there is a Warlord
    so the Warlord will be the first element in Army"""
    counter_h = 0
    counter_k = 0
    if self._warlord:
      for i in self._army:
        if isinstance(i, Healer):
          counter_h = counter_h + 1
          self._army.pop(self._army.index(i))
        elif isinstance(i, Knight):
          self._army.pop(self._army.index(i))
          counter_k = counter_k + 1
          self._knight = True
    while self._knight and counter_k >= 1:
      self._army.insert(0, Knight())
      counter_k = counter_k - 1
    while counter_h >= 1:
      self._army.insert(1, Healer())
      counter_h = counter_h - 1
    for i in self._army:
      if counter_k == 0 and isinstance(self._army[0], Healer) and self.inWarlord() and not isinstance(i, Healer):
        self._army.pop(self._army.index(i))
        self._army.insert(0, i)
        break
