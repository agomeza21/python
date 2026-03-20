class Plant:
    """Represents a generic plant with name, height, and age.."""
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        """Initializes a plant with its basic attributes."""
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        """Returns True if the given number of days is more than a year."""
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        """Creates and returns an anonymous plant with default values."""
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        """Increases the plant height by 1cm."""
        self.height += 1.0
        self._stats._grow_calls += 1

    def age(self) -> None:
        """Increases the plant age by 1 day."""
        self.plant_age += 1
        self._stats._age_calls += 1

    def show(self) -> None:
        """Displays the plant information."""
        print(f"{self.name}: {self.height:.1f}cm, {self.plant_age} days old")
        self._stats._show_calls += 1

    class Stats:
        """Stores statistical data for a plant."""
        def __init__(self) -> None:
            """Initializes all counters to zero."""
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def display(self) -> None:
            """Displays the statistics."""
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, {self._show_calls} show")

class Flower(Plant):
    """Plant with a flower that can bloom, inherits from Plant."""
    def __init__(self, name: str, height: float, plant_age: int, color: str) -> None:
        """Initializes a flower with its characteristic color."""
        super().__init__(name, height, plant_age)
        self.color = color
        self._blooming = False

    def bloom(self) -> None:
        """Sets the flower blooming state to True."""
        self._blooming = True
    
    def show(self) -> None:
        """Displays the flower information including color and blooming state."""
        super().show()
        print(f"Color: {self.color}")
        if self._blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    """Flowering plant that holds seeds once bloomed, inherits from Flower."""
    def __init__(self, name: str, height: float, plant_age: int,
                 color: str, seeds: int = 0) -> None:
        """Initializes a seed with its number of seeds."""
        super().__init__(name, height, plant_age, color)
        self.seeds = seeds

    def show(self) -> None:
        """Displays the seed information including number of seeds."""
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    """Tree that can generate shade, inherits from Plant."""
    def __init__(self, name: str, height: float, plant_age: int,
                 trunk_diameter: float) -> None:
        """Initializes a tree with the diameter of its trunk."""
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def produce_shade(self) -> None:
        """Prints the shade produced by the tree based on its dimensions."""
        print(f"Tree {self.name} now produces a shade of "
              f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")
        self._stats._shade_calls += 1
    def show(self) -> None:
        """Displays the tree information including trunk diameter."""
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    class Stats(Plant.Stats):
        """Extends Plant.Stats with shade production tracking."""
        def __init__(self) -> None:
            """Initializes all counters including shade calls."""
            super().__init__()
            self._shade_calls = 0

        def display(self) -> None:
            """Displays the statistics including shade calls."""
            super().display()
            print(f"{self._shade_calls} shade")


def display_stats(plant: Plant) -> None:
    """Displays the statistics for any kind of plant."""
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


def main() -> None:
    """Entry point of the program."""
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_stats(rose)
    print(f"[asking the {rose.name.lower()} to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stats(oak)
    print(f"[asking the {oak.name.lower()} to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print(f"[make {sunflower.name.lower()} grow, age and bloom]")
    for i in range(30):
        sunflower.grow()
    for i in range(20):
        sunflower.age()
    sunflower.bloom()
    sunflower.seeds = 42
    sunflower.show()
    display_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    main()
