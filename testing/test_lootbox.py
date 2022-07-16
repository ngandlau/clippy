import src.lootbox as lootbox

def test_lootbox_holds_weapons():
    """A lootbox must contain objects of weapons."""
    lb = lootbox.Lootbox()
    has_correct_weapon_type = [type(w) for w in lb.weapons_in_lootbox]
    assert all(has_correct_weapon_type)

def fuzzy_comparison(ist_probs, soll_probs, threshold=0.1):
    is_within_threshold = []
    for weapon_name in ist_probs:
        ist_prob = ist_probs[weapon_name]
        soll_prob = soll_probs[weapon_name]
        diff = ist_prob - soll_prob[1]
        if abs(diff) < threshold:
            is_within_threshold.append(True)
        else:
            is_within_threshold.append(False)
    return all(is_within_threshold)

def test_weapons_are_drawn_randomly():
    n_samples = 1000
    lb = lootbox.Lootbox()
    samples = [lb.draw_random_weapon().get_name() for i in range(n_samples)]

    # calculate the relative frequency of occurrence for each weapon
    relative_freqs = {}
    for weapon_name in set(samples):
        relative_freqs[weapon_name] = samples.count(weapon_name) / n_samples

    # compare the distribution of weapons of ist vs soll
    ist_probs = relative_freqs
    soll_probs = lb.occurence_probs
    is_equal = fuzzy_comparison(ist_probs, soll_probs, threshold=0.05)

    assert is_equal is True















