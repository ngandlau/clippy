# Abstract Interface
from dataclasses import dataclass
from main.src.rarity import Rarity
    

class Weapon:
    def get_base_attack(self):
        pass

    def get_rarity(self):
        pass

    def get_name(self):
        pass

@dataclass
class Fist(Weapon):
    base_attack: int = 1
    name: str = "fist"
    rarity: int = Rarity.ABUNDANT.value

    def get_base_attack(self):
        return self.base_attack

    def get_rarity(self):
        return self.rarity

    def get_name(self):
        return self.name

@dataclass
class Sword(Weapon):
    base_attack: int = 2
    name: str = "sword"
    rarity: int = Rarity.COMMON.value

    def get_base_attack(self):
        return self.base_attack

    def get_rarity(self):
        return self.rarity

    def get_name(self):
        return self.name

@dataclass
class Bazooka(Weapon):
    base_attack: int = 99
    name: str = "bazooka"
    rarity: int = Rarity.RARE.value

    def get_base_attack(self):
        return self.base_attack

    def get_rarity(self):
        return self.rarity

    def get_name(self):
        return self.name


