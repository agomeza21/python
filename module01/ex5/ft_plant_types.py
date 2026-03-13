class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} provides {self.trunk_diameter * 50} square "
              "meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===")
    print("")
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 45, 80, "blue")
        ]
    for flower in flowers:
        print(f"{flower.name} (Flower): {flower.height}cm, {flower.age} days,"
              f" {flower.color} color")
        flower.bloom()
        print("")
    print("")
    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 350, 3280, 80)
        ]
    for tree in trees:
        print(f"{tree.name} (Tree): {tree.height}cm, {tree.age} days,"
              f" {tree.trunk_diameter}cm diameter")
        tree.produce_shade()
        print("")
    print("")
    vegetables = [
        Vegetable("Tomatoe", 80, 90, "summer", "C"),
        Vegetable("Potato", 75, 20, "winter", "D")
        ]
    for vegetable in vegetables:
        print(f"{vegetable.name} (Vegetable): {vegetable.height}cm,"
              f" {vegetable.age} days, {vegetable.harvest_season} harvest")
        print(f"{vegetable.name} is rich in vitamin "
              f"{vegetable.nutritional_value}")
        print("")


if __name__ == "__main__":
    main()
