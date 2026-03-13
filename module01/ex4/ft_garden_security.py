class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def set_height(self, new_height: int) -> int:
        if (new_height < 0):
            print(f"Invalid operation attempted: "
                  f"height {new_height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height updated: {self._height} [OK]")

    def set_age(self, new_age: int) -> int:
        if (new_age < 0):
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    plant1 = SecurePlant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant1.name}")
    plant1.set_height(40)
    plant1.set_age(77)
    plant1.set_height(-5)
    print(f"Current plant: {plant1.name} ({plant1.get_height()}cm, "
          f"{plant1.get_age()} days)")


if __name__ == "__main__":
    main()
