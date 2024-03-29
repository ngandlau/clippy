import main.src.clippy as clippy
from main.src.lootbox import Lootbox

def test_clippy_can_greet():
    clpy = clippy.Clippy("Nils")
    assert clpy.greet() == "Hello Nils, I'm Clippy!"

def test_clippy_can_farewell():
    clpy = clippy.Clippy("Nils")
    assert clpy.farewell() == "Goodbye, old friend!"

def test_clippy_can_attack():
    gormsen, gandlau = clippy.Clippy("Nils"), clippy.Clippy("Nils")
    lootbox = Lootbox()
    gormsen.equip_weapon(lootbox.draw_random_weapon())
    gandlau_life_before = gandlau.life
    gormsen.attack(gandlau)
    assert gandlau.life < gandlau_life_before