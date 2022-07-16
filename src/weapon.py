# Abstract Interface
from dataclasses import dataclass
from enum import Enum
import math

class Weapon:
    def get_base_attack(self):
        pass


@dataclass
class Sword(Weapon):
    base_attack: int = 2

    def get_base_attack(self):
        return self.base_attack


@dataclass
class Bazooka(Weapon):
    base_attack: int = 99999999

    def get_base_attack(self):
        return self.base_attack


@dataclass()
class Weapons:
    all_weapons = [Bazooka, Sword]

    @staticmethod
    def get_random_weapon(self):
        Weapon = math.random.choice(self.all_weapons)
        return Weapon()