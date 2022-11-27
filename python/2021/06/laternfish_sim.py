from debug import p


def simulate_fish(fish_dict, generations):
    new_fish_dict = fish_dict.copy()

    for i in range(generations):
        spawning_fish = new_fish_dict[0]
        for j in range(8):
            new_fish_dict[j] = new_fish_dict[j + 1]

        new_fish_dict[6] += spawning_fish
        new_fish_dict[8] = spawning_fish

    return new_fish_dict
