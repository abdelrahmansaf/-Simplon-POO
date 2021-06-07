from part2.fight import fight
from part2.knight import Knight
from part2.vampire import *


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
        unit_1.Vam() 
      if isinstance(unit_1,Knight) and len(army2)>1:
        army2[1].damaged(unit_1.knight1())
      print(f'army={unit_1._life} unit_1 army')
      print(f'army2={unit_2._life} unit_2 army2')
      print(f'health {unit_1.health} ')

      if unit_2.isalive() == False:
        army2.pop()
        if len(army2) == 0:
          return True
        unit_2 = army2[0]
        

      unit_1.damaged(unit_2.strength)
      if isinstance(unit_2, Vampire):
        unit_2.Vam() 
      if isinstance(unit_2,Knight) and len(army)>1:
        army[1].damaged(unit_2.knight1())
      print('----------------')
      print(f'army={unit_1._life} unit_1 army')
      print(f'army2={unit_2._life} unit_2 army2')
      print(f'health {unit_1.health} ')

      if not unit_1.isalive():
        army.pop()
        if len(army) == 0:
          return False
        unit_1 = army[0]


    # while True:
    #   ret = fight(unit_1, unit_2)
    
    #   if not ret:
    #     if isinstance(unit_2,Knight) and len(army)>1:
    #      army[1].damaged(unit_2.knight1())
    #     unit_1 = army.pop()          
        # if len(army) == 0:
        #   return False
        # unit_1 = army[0]

    #   if ret :
    #     if isinstance(unit_1,Knight) and len(army2)>1:
    #       print(f'army= {unit_1._life} unit_1 army')
    #       print(f'army2= {unit_2._life} unit_2 army2')
    #       print(f'army2= {army2[0]} army2[1]')
    #       army2[1].damaged(unit_1.knight1())
    #     unit_2 = army2.pop()
    #     if len(army2) == 0:
    #       return True
    #     unit_2 = army2[0]