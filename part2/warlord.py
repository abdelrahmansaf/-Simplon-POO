from part2.defender import Defender

class Warlord(Defender):
  def __init__(self, strength=4, life_point=100, defense=2):
    self.defense = defense
    super().__init__(strength=strength, life_point=life_point)
