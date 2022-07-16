import src.weapon as weapon

def test_weapon_has_base_attack():
    sword = weapon.Sword()
    assert sword.get_base_attack() == 2