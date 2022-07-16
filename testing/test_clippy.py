import src.clippy as clippy
import src.weapon as weapon

def test_clippy_can_greet():
    clpy = clippy.Clippy()
    assert clpy.greet() == "Hello Nils, I'm Clippy!"

def test_clippy_can_farewell():
    clpy = clippy.Clippy()
    assert clpy.farewell() == "Goodbye, old friend!"

def test_clippy_can_attack():
    gormsen = clippy.Clippy()
    gandlau = clippy.Clippy()
    sword = weapon.Sword()
    gormsen.equip_weapon(weapon=sword)
    gandlau_life_before = gandlau.life
    gormsen.attack(gandlau)
    assert gandlau.life < gandlau_life_before
    assert gandlau.life == gandlau_life_before - 1