from __future__ import annotations

import math


class Clippy():
    def __init__(self):
        self.weapon = None
        self.life = 10

    def equip_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def greet(self):
        return "Hello Nils, I'm Clippy!"

    def farewell(self):
        return "Goodbye, old friend!"

    def attack(self, other: Clippy):
        other.life - self.weapon.get_base_attack()


if __name__ == '__main__':
    print('hello world!')
