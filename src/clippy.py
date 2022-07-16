from __future__ import annotations
from src.weapon import Weapon, Weapons

class Clippy():
    def __init__(self):
        self.weapon = self.__draw_random_weapon()
        self.life = 10

    def __draw_random_weapon(self):
        return Weapons.get_random_weapon()

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
    print('hello world!')
