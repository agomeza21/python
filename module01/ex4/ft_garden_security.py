class SecurePlant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height:.0f}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self.get_height():.1f}cm,"
              f" {self.get_age()} days old")


def main() -> None:
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    plant1.show()
    print("")
    plant1.set_height(25)
    plant1.set_age(30)
    print("")
    plant1.set_height(-5)
    plant1.set_age(-3)
    print("")
    print("Current state: ", end="")
    plant1.show()


if __name__ == "__main__":
    main()
