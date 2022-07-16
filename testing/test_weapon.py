from src.weapon import Sword

def test_weapon_has_base_attack():
    sword = Sword()
    assert sword.get_base_attack() == 2