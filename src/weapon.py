# Abstract Interface
from dataclasses import dataclass
from enum import Enum
import random

class Weapon:
    def get_base_attack(self):
        pass


@dataclass
class Sword(Weapon):
    base_attack: int = 2
    name: str = "sword"

    def get_base_attack(self):
        return self.base_attack

@dataclass
class Bazooka(Weapon):
    base_attack: int = 99999999
    name: str = "bazooka"

    def get_base_attack(self):
        return self.base_attack

@dataclass
class Weapons:
    
    @staticmethod
    def get_random_weapon():
        all_weapons = [Bazooka(), Sword()]
        return random.choice(all_weapons)
