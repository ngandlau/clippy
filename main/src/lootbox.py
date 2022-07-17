import random
from typing import Dict, List
from main.src.weapon import Bazooka, Fist, Sword, Weapon

class Lootbox:
    weapons_in_lootbox: List[Weapon] = None
    weapon_names: List[str] = None
    occurence_probs: Dict[str, float] = None

    def __init__(self):
        self.weapons_in_lootbox = [Fist(), Sword(), Bazooka()]
        self.weapon_names = [w.get_name() for w in self.weapons_in_lootbox]
        self.occurence_probs = self.__calculate_occurrence_probabilities()

    def __calculate_occurrence_probabilities(self) -> Dict[str, float]:
        """self-explanatory"""
        rarities = [w.get_rarity() for w in self.weapons_in_lootbox]
        occurence_probs = {}
        for w in self.weapons_in_lootbox:
            occurence_prob = w.get_rarity() / sum(rarities)
            occurence_probs[w.get_name()] = occurence_prob
        return occurence_probs

    def draw_random_weapon(self) -> Weapon:
        weapons, probs = [], []
        for i, weapon_name in enumerate(self.weapon_names):
            weapon_object = self.weapons_in_lootbox[i]
            weapon_prob = self.occurence_probs[weapon_name]
            weapons.append(weapon_object)
            probs.append(weapon_prob)
        drawn_weapon = random.choices(weapons, weights=probs)[0]
        return drawn_weapon