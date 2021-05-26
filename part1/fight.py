def fight(unit_1, unit_2):
  """
  Simple Fight function

  :param unit_1: First unit to fight
  :param unit_2: Second unit to fight
  :return bool: True if unit_1 won the fight False otherwise"""
  while unit_1.isalive():
    unit_2.damaged(unit_1.strength)
    if unit_2.isalive() == False:
      return True
    unit_1.damaged(unit_2.strength)
  return False
  
          
