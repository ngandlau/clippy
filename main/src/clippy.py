from __future__ import annotations
from dataclasses import dataclass
from main.src.weapon import Weapon

@dataclass
class Clippy:
    name: str
    life: float = 10
    weapon: Weapon = None

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def greet(self):
        return "Hello Nils, I'm Clippy!"

    def farewell(self):
        return "Goodbye, old friend!"

    def attack(self, other: Clippy):
        other.life -= self.weapon.get_base_attack()
        if other.life < 0:
            other.life = 0


if __name__ == '__main__':
    pass
