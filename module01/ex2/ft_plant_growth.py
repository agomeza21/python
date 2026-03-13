class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.plant_age += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Cactus", 15, 120)
    plants = [plant1, plant2]
    for plant in plants:
        count = -1
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            plant.get_info()
            plant.grow()
            plant.age()
            count = count + 1
        print(f"Growth this week: +{count}")


if __name__ == "__main__":
    main()
