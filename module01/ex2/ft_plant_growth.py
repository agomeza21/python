class Plant:
    def __init__(self, name: str, height: float, plant_age: int, growth_rate: float = 0.8) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")
    plant1 = Plant("Rose", 25.0, 30, growth_rate=0.8)
    plant2 = Plant("Cactus", 15.0, 120, growth_rate=0.2)
    plants = [plant1, plant2]
    for plant in plants:
        initial_height = plant.height
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            plant.show()
            plant.grow()
            plant.age()
            growth = plant.height - initial_height
        print(f"Growth this week: {growth:.0f}cm\n")


if __name__ == "__main__":
    main()
