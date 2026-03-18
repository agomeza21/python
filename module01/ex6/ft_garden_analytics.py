class Plant:
    """Represents a basic plant with name and height."""
    def __init__(self, name: str, height: int) -> None:
        """Initializes a plant with name and height."""
        self.name = name
        self.height = height

    def grow(self) -> int:
        """Increases the height of the plant by 1 cm."""
        unit = 1
        self.height += unit
        return unit


class FloweringPlant(Plant):
    """Plant capable of blooming, inherits from Plant."""
    def __init__(self, name: str, height: int, color: str) -> None:
        """Initializes a flowering plant."""
        super().__init__(name, height)
        self.color = color

    @staticmethod
    def bloom() -> str:
        """Returns a string indicating that the plant is blooming."""
        return "(blooming)"


class PrizeFlower(FloweringPlant):
    """Award-winning flowering plant, inherits from FloweringPlant."""
    def __init__(self, name: str, height: int, color: str,
                 prize: int) -> None:
        """Initializes an award-winning plant."""
        super().__init__(name, height, color)
        self.prize = prize


class GardenManager:
    """Manages a garden with multiple plants and keeps global statistics."""
    total_gardens = 0

    def __init__(self, p_name: str) -> None:
        """Initializes a garden for an owner
          and increments the global counter."""
        GardenManager.total_gardens += 1
        self.p_name = p_name
        self.plants: list[Plant] = []
        self.growth = 0

    def add_plants(self, plant: Plant) -> None:
        """Adds a plant to the garden and prints confirmation."""
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.p_name}'s garden")

    def plant_growth(self) -> None:
        """Makes all plants in the garden grow and prints the progress."""
        print(f"{self.p_name} is helping all plants grow...")
        for plant in self.plants:
            self.growth = plant.grow()
            print(f"{plant.name} grew {self.growth}cm")

    def report(self) -> None:
        """Prints a report of all plants and garden statistics."""
        print("Plants in garden:")
        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.color} flowers {plant.bloom()},"
                      f" Prize points: {plant.prize}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm,"
                      f" {plant.color} flowers {plant.bloom()}")
            else:
                print(f"- {plant.name}: {plant.height}cm")
        stats = GardenManager.GardenStats(self.plants, self.growth)
        print("")
        print(f"Plants added: {stats.total_plants}, Total growth: "
              f"{stats.total_growth}cm")
        print(f"Plant types: {stats.count_plant} regular, "
              f"{stats.count_flowering} flowering, {stats.count_prize} "
              "prize flowers")

    def is_valid_height(self) -> bool:
        """Checks that all plants have a positive height."""
        for plant in self.plants:
            if plant.height < 0:
                return False
        return True

    @classmethod
    def create_garden_network(cls) -> None:
        """Prints the total number of gardens managed so far."""
        print(f"Total gardens managed: {cls.total_gardens}")

    def garden_score(self) -> int:
        """Calculates the total garden score by summing
          heights and prize points."""
        scores = 0
        for plant in self.plants:
            scores = scores + plant.height
            if isinstance(plant, PrizeFlower):
                scores = scores + plant.prize
        return scores

    class GardenStats:
        """Calculates and stores statistics for a set of plants."""
        def __init__(self, plants: list[Plant], growth: int) -> None:
            """Initializes the statistics from a list of plants."""
            self.total_plants = len(plants)
            self.count_prize = 0
            self.count_flowering = 0
            self.count_plant = 0
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    self.count_prize += 1
                elif isinstance(plant, FloweringPlant):
                    self.count_flowering += 1
                else:
                    self.count_plant += 1
            self.total_growth = growth * self.total_plants


def main() -> None:
    """Entry point of the program."""
    gardens = [
        GardenManager("Alice"),
        GardenManager("Bob")
    ]
    plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]
    plant_bob = Plant("Pine Tree", 90)
    print("=== Garden Management System Demo ===")
    print("")
    for plant in plants:
        gardens[0].add_plants(plant)
    gardens[1].add_plants(plant_bob)
    print("")
    gardens[0].plant_growth()
    print("")
    print(f"=== {gardens[0].p_name}'s Garden Report ===")
    gardens[0].report()
    print("")
    print(f"Height validation test: {gardens[0].is_valid_height()}")
    print(f"Garden scores - {gardens[0].p_name}: {gardens[0].garden_score()},"
          f" {gardens[1].p_name}: {gardens[1].garden_score()}")
    gardens[0].create_garden_network()


if __name__ == "__main__":
    main()
