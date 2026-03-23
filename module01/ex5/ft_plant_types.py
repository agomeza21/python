class Plant:
    """Represents a generic plant with name, height, and age.."""
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        """Initializes a plant with its basic attributes."""
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        """Increases the plant height by 1cm."""
        self.height += 1.0

    def age(self) -> None:
        """Increases the plant age by 1 day."""
        self.plant_age += 1

    def show(self) -> None:
        """Displays the plant information."""
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")


class Flower(Plant):
    """Plant with a flower that can bloom, inherits from Plant."""
    def __init__(self, name: str, height: float, plant_age: int,
                 color: str) -> None:
        """Initializes a flower with its characteristic color."""
        super().__init__(name, height, plant_age)
        self.color = color
        self._blooming = False

    def bloom(self) -> None:
        """Sets the flower blooming state to True."""
        self._blooming = True

    def show(self) -> None:
        """Displays the flower information including color
         and blooming state."""
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    """Tree that can generate shade, inherits from Plant."""
    def __init__(self, name: str, height: float, plant_age: int,
                 trunk_diameter: float) -> None:
        """Initializes a tree with the diameter of its trunk."""
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Prints the shade produced by the tree based on its dimensions."""
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and"
              f" {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        """Displays the tree information including trunk diameter."""
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    """Vegetable with harvest season and nutritional value,
      inherits from Plant."""
    def __init__(self, name: str, height: float, plant_age: int,
                 harvest_season: str) -> None:
        """Initializes a vegetable with its harvest season
          and nutritional value."""
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        """Increases the vegetable height by 2.1cm and
          nutritional value by 1."""
        self.height += 2.1
        self.nutritional_value += 1

    def age(self) -> None:
        """Increases the vegetable age by 1 day."""
        super().age()

    def show(self) -> None:
        """Displays the vegetable information including harvest
          season and nutritional value."""
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def main() -> None:
    """Entry point of the program."""
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
