class Plant:
    def __init__(self, name: str, height: int, plant_age: int):
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self):
        self.height += 1

    def age(self):
        self.plant_age += 1

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def main() -> None:
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Cactus", 15, 120)
    count = -1
    plants = [plant1, plant2]
    for plant in plants:
        for i in range(1, 8):
            print(f"=== Day {i} ===")
            plant.get_info()
            plant.grow()
            plant.age()
            count = count + 1
        print(f"Growth this week: +{count}")


if __name__ == "__main__":
    main()
