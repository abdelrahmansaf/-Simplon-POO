from part2.knight import Knight
from part2.vampire import Vampire
from part2.healer import Healer
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
    while unit_1.isalive():
      unit_2.damaged(unit_1.strength)
      if isinstance(unit_1, Vampire):
        unit_1.vam()
      if isinstance(unit_1, Knight) and len(army2) > 1:
        army2[1].damaged(unit_1.knight1())
      if len(army) > 1 and isinstance(army[1], Healer):
        if army[0]:
          army[0].heal()
      if not unit_2.isalive():
        army2.pop()
        if len(army2) == 0:
          return True
        else:
          unit_2 = army2[0]

      unit_1.damaged(unit_2.strength)
      if isinstance(unit_2, Vampire):
        unit_2.Vam()

      if isinstance(unit_2, Knight) and len(army) > 1:
        army[1].damaged(unit_2.knight1())

      if len(army2) > 1 and isinstance(army2[1], Healer):

        if army2[0]:
          army2[0].heal()

      if not unit_1.isalive():
        army.pop()
        if len(army) == 0:
          print('rip army')
          return False
        unit_1 = army[0]
