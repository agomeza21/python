def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    s_artifacts = sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )
    return s_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    f_mages = list(filter(lambda mage: mage["power"] >= min_power, mages))
    return f_mages


def spell_transformer(spells: list[str]) -> list[str]:
    m_spells = list(map(lambda spell: "* " + spell + " *", spells))
    return m_spells


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    average = round(sum(map(lambda mage: mage["power"], mages)) / len(mages), 2)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": average
    }


def main() -> None:
    print("")
    print("Testing artifact sorter...")

    artifacts = [
        {'name': 'Lightning Rod', 'power': 61, 'type': 'accessory'},
        {'name': 'Light Prism', 'power': 116, 'type': 'armor'},
        {'name': 'Ice Wand', 'power': 116, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 64, 'type': 'armor'}
    ]

    sorted_artifacts = artifact_sorter(artifacts)
    for i in range(len(sorted_artifacts) - 1):
        a1 = sorted_artifacts[i]
        a2 = sorted_artifacts[i + 1]
        print(f"{a1['name']} ({a1['power']} power) comes before "
              f"{a2['name']} ({a2['power']} power)")

    print("")
    print("Testing power filter...")
    mages = [
        {'name': 'Kai', 'power': 99, 'element': 'wind'},
        {'name': 'Ember', 'power': 85, 'element': 'ice'},
        {'name': 'Morgan', 'power': 75, 'element': 'shadow'},
        {'name': 'River', 'power': 58, 'element': 'earth'},
        {'name': 'Morgan', 'power': 96, 'element': 'earth'}
    ]
    min_power = 80
    filter_mages = power_filter(mages, min_power)
    print(f"Mages whith power >= {min_power}:")
    for mage in filter_mages:
        print(f"{mage['name']} ({mage['power']})")

    print("")
    print("Testing spell transformer...")
    spells = ['freeze', 'shield', 'darkness', 'flash']

    mage_spells = spell_transformer(spells)
    print(" ".join(mage_spells))

    print("")
    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(stats)
    print("")


if __name__ == "__main__":
    main()
