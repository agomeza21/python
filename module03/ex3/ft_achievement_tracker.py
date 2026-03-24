import random


def gen_player_achievements(all_achivements: list) -> set:
    ach_set = set(random.sample(all_achivements, random.randint(1, 20)))
    return ach_set


def main() -> None:
    all_achivements = [
        "Boss Slayer", "Speed Runner", "Survivor", "Master Explorer",
        "Treasure Hunter", "First Steps", "Sharp Mind", "Unstoppable",
        "Untouchable", "Crafting Genius", "World Savior", "Strategist",
        "Collector Supreme", "Hidden Path Finder", "Dragon Tamer",
        "Night Owl", "Pacifist", "Completionist", "Ghost", "Legend"
    ]
    print("=== Achievement Tracker System ===")
    print("")
    alice = gen_player_achievements(all_achivements)
    bob = gen_player_achievements(all_achivements)
    charlie = gen_player_achievements(all_achivements)
    dylan = gen_player_achievements(all_achivements)
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print("")
    print(f"All distinct achievements: {alice | bob | charlie | dylan}")
    print("")
    print(f"Common achievements: {alice & bob & charlie & dylan}")
    print("")
    print(f"Only Alice has: {alice - bob - charlie - dylan}")
    print(f"Only Bob has: {bob - alice - charlie - dylan}")
    print(f"Only Charlie has: {charlie - bob - alice - dylan}")
    print(f"Only Dylan has: {dylan - charlie - bob - alice}")
    print("")
    print(f"Alice is missing: {set(all_achivements) - alice}")
    print(f"Bob is missing: {set(all_achivements) - bob}")
    print(f"Charlie is missing: {set(all_achivements) - charlie}")
    print(f"Dylan is missing: {set(all_achivements) - dylan}")


if __name__ == "__main__":
    main()
