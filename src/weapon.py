# Abstract Interface
from dataclasses import dataclass
from enum import IntEnum
import random


class Rarity(IntEnum):
    RARE = 1
    COMMON = 2
    ABUNDANCE = 3


class Weapon:
    def get_base_attack(self):
        pass

    def get_rarity(self):
        pass

    def get_name(self):
        pass


@dataclass
class Sword(Weapon):
    base_attack: int = 2
    name: str = "sword"
    rarity: int = Rarity.COMMON

    def get_base_attack(self):
        return self.base_attack

    def get_rarity(self):
        return self.rarity

    def get_name(self):
        return self.name


@dataclass
class Bazooka(Weapon):
    base_attack: int = 99999999
    name: str = "bazooka"
    rarity: Rarity = Rarity.RARE

    def get_base_attack(self):
        return self.base_attack

    def get_rarity(self):
        return self.rarity

    def get_name(self):
        return self.name


class Weapons:
    all_weapons = [Bazooka(), Sword()]

    @staticmethod
    def get_random_weapon():
        all_weapons = [Bazooka(), Sword()]
        return random.choice(all_weapons)
