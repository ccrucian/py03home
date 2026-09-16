import random


all_ach: list[str] = [
                        "Winner", "Loser", "Hunter", "King",
                        "Wizard", "Main", "Zero", "Capitain",
                        "Teacher", "Mask", "Ready", "Contig",
                        "Genius", "Traitor", "Boss"
                    ]


def gen_player_achievement() -> set[str]:
    number: int = random.randint(5, 10)
    pick_randoms: list[str] = random.sample(all_ach, number)
    return set(pick_randoms)


players: dict[str, set[str]] = {
                        "Alice": gen_player_achievement(),
                        "Bob": gen_player_achievement(),
                        "Charlie": gen_player_achievement(),
                        "Dylan": gen_player_achievement()
                            }


def main() -> None:
    print("=== Achievement Tracker System ===")
    for player, achievement in players.items():
        print(
            f"Player {player}: {achievement}"
            )
    l_set: set[str] = set()
    for v in players.values():
        l_set = l_set.union(v)
    print(f"All distinct achievement: {l_set}")
    print()
    # for player in players:
    #    common: set[str] = l_set.intersection(players[player])
    common: set[str] = l_set.intersection(*(players[i] for i in players))
    print(f"Common: {common}")
    print("")
    for name, val in players.items():
        unique: set[str] = val.difference(*(
            players[other] for other in players if other != name
            ))
        print(f"Only {name} has: {unique}")
    print()
    for player in players:
        missing: set[str] = set(all_ach).difference(players[player])
        print(f"{player} is missing: {missing}")


if __name__ == "__main__":
    main()
