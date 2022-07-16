import src.weapon as weapon

def test_weapons_are_drawn_randomly():
    n_samples = 1000
    samples = [weapon.Weapons.get_random_weapon().name for i in range(n_samples)]
    soll_probs = {
        'sword': 0.5,
        'bazooka': 0.5
    }
    assert fuzzy_check(samples, soll_probs, threshold=0.05) is True
    

def test_weapon_has_base_attack():
    sword = weapon.Sword()
    assert sword.get_base_attack() == 2

def fuzzy_check(samples, soll_probs, threshold=0.1):
    # ist-Verteilung
    n_total = len(samples)
    unique_weapons = set(samples)

    ist_probs = {}
    for w in unique_weapons:
        n = samples.count(w)
        ist_probs[w] = n / n_total # relative frequency

    # compare ist with soll
    diffs = []
    for w in unique_weapons:
        ist_prob = ist_probs[w]
        soll_prob = soll_probs[w]
        diff = soll_prob - ist_prob
        diffs.append(diff)

    is_within_threshold = [abs(d) < threshold for d in diffs]
    if all(is_within_threshold):
        return True
    else:
        return False
    
    


    








