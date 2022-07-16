import random
from typing import Dict, List, Tuple
from src.weapon import Bazooka, Fist, Sword, Weapon

class Lootbox:
    weapons_in_lootbox: List[Weapon] = [Fist(), Sword(), Bazooka()]
    occurence_probs: Dict[str, Tuple[Weapon, float]] = None

    def __init__(self):
        self.occurence_probs = self._occurrence_probabilities()

    def _occurrence_probabilities(self) -> Dict[str, str]:
        """
        For each weapon, calculate its probability of randomly drawing
        that weapon when opening the lootbox.

        Return: 
            {
                'bazooka': 0.6666,
                'sword': 0.3333
            }
        """
        rarities = [w.get_rarity() for w in self.weapons_in_lootbox]
        occurence_probs = {}
        for w in self.weapons_in_lootbox:
            occurence_prob = w.get_rarity() / sum(rarities)
            occurence_probs[w.get_name()] = (w, occurence_prob)
        return occurence_probs

    def draw_random_weapon(self) -> Weapon:
        weapons = []
        probs = []
        for weapon_name in self.occurence_probs:
            weapon_object, weapon_prob = self.occurence_probs[weapon_name]
            weapons.append(weapon_object)
            probs.append(weapon_prob)
        drawn_weapon = random.choices(weapons, weights=probs)[0]
        return drawn_weapon

if __name__ == '__main__':
    pass