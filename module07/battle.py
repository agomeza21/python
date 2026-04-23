'#battle.py'
from ex0 import FlameFactory, AquaFactory, CreatureFactory


def verify_factory(factory: CreatureFactory) -> None:
    try:
        print("Testing factory")

        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())

        print(evolved.describe())
        print(evolved.attack())
    except Exception as e:
        print(f"An error occurred while testing the factory: {e}")


def battle_creatures(f1: CreatureFactory, f2: CreatureFactory) -> None:
    try:
        print("Testing battle")

        creature_1 = f1.create_base()
        creature_2 = f2.create_base()

        print(creature_1.describe())
        print(" vs.")
        print(creature_2.describe())
        print(" fight!")
        print(creature_1.attack())
        print(creature_2.attack())
    except Exception as e:
        print(f"Battle error: {e}")


if __name__ == "__main__":
    verify_factory(FlameFactory())
    print("")
    verify_factory(AquaFactory())
    print("")
    battle_creatures(FlameFactory(), AquaFactory())
