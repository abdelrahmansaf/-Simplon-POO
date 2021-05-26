from part1.fight import fight
class Battlefield():
  """
  Battlefield used to battle two armys against each other
  """

  def simpleFight(self, army, army2):
    """
    :param army: First army
    :param army2: Second army
    :return bool: Did the first army won ?
    """
    unit_1 = army[0]
    unit_2 = army2[0]
    while True:
      ret = fight(unit_1, unit_2)
      if not ret:
        unit_1 = army.pop()
        if len(army) == 0:
          return False
        unit_1 = army[0]
      else:
        unit_2 = army2.pop()
        if len(army2) == 0:
          return True

        unit_2 = army2[0]
