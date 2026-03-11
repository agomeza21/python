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
    count = -1
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant1.get_info()
        plant1.grow()
        plant1.age()
        count = count + 1
    print(f"Growth this week: +{count}")


if __name__ == "__main__":
    main()
