'#capacitor.py'

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    try:
        print("Testing Creature with healing capability")
        factory = HealingCreatureFactory()
        print(" base:")

        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())
        print(base.heal())
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.heal())
    except Exception as e:
        print(f"An error occurred during healing capability test: {e}")


def test_transform() -> None:
    try:
        print("Testing Creature with transform capability")
        factory = TransformCreatureFactory()
        print(" base:")

        base = factory.create_base()
        evolved = factory.create_evolved()

        print(base.describe())
        print(base.attack())
        print(base.transform())
        print(base.attack())
        print(base.revert())
        print(" evolved:")
        print(evolved.describe())
        print(evolved.attack())
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())
    except Exception as e:
        print(f"An error occurred during transform capability test: {e}")


if __name__ == "__main__":
    test_healing()
    print("")
    test_transform()
