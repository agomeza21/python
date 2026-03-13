class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Cactus", 15, 120),
        Plant("Sunflower", 32, 12),
        Plant("Tulip", 7, 4),
        Plant("Oak", 200, 500)
        ]
    print("=== Plant Factory Output ===")
    count = 0
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
        count = count + 1
    print("")
    print(f"Total plants created:{count}")


if __name__ == "__main__":
    main()
