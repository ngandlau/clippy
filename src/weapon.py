# Abstract Interface
from dataclasses import dataclass

class Weapon:
    def get_base_attack(self):
        pass

@dataclass
class Sword(Weapon):
    base_attack: int = 2

    def get_base_attack(self):
        return self.base_attack






