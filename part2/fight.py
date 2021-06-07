from part2.vampire import Vampire

def fight(unit_1, unit_2):
  """
  Simple Fight function
  :param unit_1: First unit to fight
  :param unit_2: Second unit to fight
  :return bool: True if unit_1 won the fight False otherwise"""
  while unit_1.isalive():
    unit_2.damaged(unit_1.strength)
    if isinstance(unit_1, Vampire):
      unit_1.Vam() 
    
    if unit_2.isalive() == False:
      return True
    
    unit_1.damaged(unit_2.strength)
    if isinstance(unit_2,Vampire):
      unit_2.Vam()

  return False

  
          
