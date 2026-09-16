import random


ALL_ACH: list[str] = [
                        "Winner", "Loser", "Hunter", "King",
                        "Wizard", "Main", "Zero", "Capitain",
                        "Teacher", "Mask", "Ready", "Contig",
                        "Genius", "Traitor", "Boss"
                    ]


def gen_player_achievement() -> set[str]:
    number: int = random.randint(5, 10)
    pick_randoms: list[str] = random.sample(ALL_ACH, number)
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
    print(f"All distinct achievement: {set(ALL_ACH)}")


if __name__ == "__main__":
    main()