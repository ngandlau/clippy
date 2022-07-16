import src.clippy as clippy
import src.weapon as weapon
from src.lootbox import Lootbox

def test_clippy_can_greet():
    clpy = clippy.Clippy()
    assert clpy.greet() == "Hello Nils, I'm Clippy!"

def test_clippy_can_farewell():
    clpy = clippy.Clippy()
    assert clpy.farewell() == "Goodbye, old friend!"

def test_clippy_can_attack():
    gormsen, gandlau = clippy.Clippy(), clippy.Clippy()
    lootbox = Lootbox()
    gormsen.equip_weapon(lootbox.draw_random_weapon())
    gandlau_life_before = gandlau.life
    gormsen.attack(gandlau)
    assert gandlau.life < gandlau_life_before