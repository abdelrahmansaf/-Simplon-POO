class Army():
  """Army hold all fighter ready to battle."""

  def __init__(self):
    """Create an Empty Army"""
    self._army = []

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
    sume = 0
    while number > sume:
      self._army.append(cls())
      sume = sume + 1

  def pop(self):
    """return the first soldier of the army"""
    return self._army.pop(0)
